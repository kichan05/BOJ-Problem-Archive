#include <iostream>

using namespace std;

int sums[1024][1024];

int main(){
    int N, M, n, x1, y1, x2, y2, sum = 0;
    scanf("%d %d", &N, &M);
    
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= N; j++) {
            scanf("%d", &n);
            
            sums[i][j] = sums[i][j - 1] + n;
        }
    }
    
    // for(int i = 1; i <= N; i++){
    //     for(int j = 1; j <= N; j++){
    //         printf("%d ", sums[i][j]);
    //     }
    //     printf("\n");
    // }
    
    
    // printf("\n");
    // printf("\n");
    
    while(M--){
        sum = 0;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        
        for(int j = x1; j <= x2; j++){
            // printf("%d %d,\t", sums[j][x2], sums[j][x1 - 1]);
            sum += sums[j][y2] - sums[j][y1 - 1];
        }
        // printf("\n");
        
        printf("%d\n", sum);
    }
    

    return 0;
}
