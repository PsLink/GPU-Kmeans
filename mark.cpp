#include <stdio.h>
#include <iostream>
#include <string>// C++ strings
#include <cstdlib>
using namespace std;// make std:: available

FILE * fin=fopen("oData.txt","r");
FILE * fmark=fopen("group.txt","r");
FILE * fout=fopen("mData.txt","w");

const int maxPts = 1000000;
const int dim = 128;

short mark[4000005];
short data[200];
int main() {

  // Generate random cornered center
  for (int i=0; i<maxPts; i++) {
    fscanf(fmark,"%hd",&mark[i]);
  }
  fclose(fmark);
  for (int i=0; i<maxPts; i++) {
    // find the center for i^th data
    for (int d=0; d<dim; d++) {
      fscanf(fin,"%hd",&data[d]); 
    }
    fprintf (fout,"%d",mark[i]);
    for (int d=0; d<dim; d++) {
      fprintf(fout," %d",data[d]);
    }
    fprintf (fout, "\n");
    if (i % 1000 == 0) cout << i << endl;
  }
}
