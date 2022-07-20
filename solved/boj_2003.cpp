#include <iostream>

using namespace std;

int sums[10001];

int main(){
    int N, M, n, count = 0;
    
    scanf("%d %d", &N, &M);
    
    for(int i = 1; i <= N; i++){
        scanf("%d", &n);
        sums[i] = sums[i - 1] + n;
        
        
        for(int j = 0; j < i; j++){
            // printf("%d %d %d %d ", i, j, sums[i], sums[j]);
            if(sums[i] - sums[j] == M){
                // printf("*");
                count++;
            }
            
            // printf("\n");
        }
    }
    
    printf("%d", count);

    return 0;
}
