#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <sys/time.h>
#include <unistd.h>
#include <limits.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>
// #include "kmeanslib.h"



int main(){
    int a[16];
    #pragma acc copy(a)
    #pragma acc parallel for reduction(+:a)
    for (int j=0; j<)
    return 0;
}