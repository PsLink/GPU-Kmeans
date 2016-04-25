/** 
 * Single device for pair counts
 *
 */

#include "GPUGenie.h"

#include <assert.h>
#include <vector>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
using namespace GPUGenie;

FILE *outFile;

int main(int argc, char* argv[])
{
    unsigned long long startTime,endTime;
    string dataFile = "lshdata.csv";
    string queryFile = "lshdata.csv";

    outFile = fopen("output.txt","w");

    vector<vector<int> > queries;
    vector<vector<int> > curQueries;

    vector<vector<int> > data;
    inv_table * table = NULL;
    unsigned int table_num;
    GPUGenie_Config config;

    bool reFlag = false;

    config.dim = 100;
    config.count_threshold = -100;
    config.num_of_topk = 20;
    config.hashtable_size = config.dim*config.num_of_topk*1.5;
    config.query_radius = 0;
    config.use_device = 1;
    config.use_adaptive_range = false;
    config.selectivity = 0.0f;

    config.query_points = &curQueries;
    config.data_points = &data;

    config.use_load_balance = true;
    config.posting_list_max_length = 6400;
    config.multiplier = 1.5f;
    config.use_multirange = false;

    config.data_type = 0;
    config.search_type = 0;
    config.max_data_size = 0;

    config.num_of_queries = 1000;

    read_file(data, dataFile.c_str(), -1);
    read_file(queries, queryFile.c_str(), -1);

    if (!reFlag) {
        preprocess_for_knn_csv(config, table);

        /* store the table */
        table_num = table[0].get_total_num_of_table();
        cout << "table number:" << table_num << endl;
        assert(inv_table::write("table_binaryfile.dat", table));
        delete[] table;
    }


    inv_table* _table;
    assert(inv_table::read("table_binaryfile.dat", _table));

    vector<int> result;
    vector<int> result_count;
    int bound;

    startTime = getTime();

    for (int i=0; i<queries.size(); i+=config.num_of_queries) {
        result.clear();
        result_count.clear();
        curQueries.clear();

        bound = queries.size();
        if (i+config.num_of_queries < queries.size()) bound = i+config.num_of_queries;

        for (int j=i; j<bound; j++) {
            vector<int> tmp;
            tmp.clear();
            for (int k=0; k<config.dim; k++)
                tmp.push_back(queries[j][k]);
            curQueries.push_back(tmp);
        }

        config.query_points = &curQueries;
        knn_search_after_preprocess(config, _table, result, result_count);
        reset_device();

        //fprintf(outFile,"batch %d: \n",i); 
        for (int i=0; i<result.size(); i++) {
            fprintf(outFile,"%d , %d\n",result[i],result_count[i]);
            if ((i+1)%config.num_of_topk == 0) fprintf(outFile,"\n"); 
        }

    }

    endTime = getTime();

    cout << getInterval(startTime,endTime) << endl;

    reset_device();
    delete[] _table;
    return 0;
}
