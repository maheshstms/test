#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n; 
    scanf("%d",&n);
    int a[n][n];
    int priSum = 0;
    int secSum = 0;
    for(int a_i = 0; a_i < n; a_i++){
       for(int a_j = 0; a_j < n; a_j++){
          
          scanf("%d",&a[a_i][a_j]);
       }
    }
    
    for(int a_i = 0; a_i < n; a_i++){
       priSum += a[a_i][a_i];
    }
    
    for(int a_i = 0, a_j=n-1; a_i < n; a_i++, a_j--){
          secSum += a[a_i][a_j];
    }

    printf("%d\n", abs(priSum - secSum));
    return 0;
}
