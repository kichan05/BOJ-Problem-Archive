#include <stdio.h>
#include <math.h>

int main() {
    int N, K, currentValue, j;
    int A[10000];
    
    scanf("%d %d", &N, &K);
    for(int i = 0; i < N; i++)
        scanf("%d", A + i);
        
    for(int i = 1; i < N; i++){
        // printf("===%d===\n", i);
        currentValue = A[i];
        j = i - 1;
        
        while(j >= 0 && A[j] > currentValue) {
            A[j + 1] = A[j];
            K--;
            if(K == 0){
                printf("%d", A[j]);
                return 0;
            }
            j--;
        }
        if(j != i - 1){
            A[j + 1] = currentValue;
            K--;
            
            if(K == 0){
                printf("%d", currentValue);
                return 0;
            }
        }
    }
    printf("-1");
    return 0;
}
