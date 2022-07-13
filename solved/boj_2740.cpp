#include <iostream>

using namespace std;

int main(){
    int N, M, K;
    int num1[101][101] = {};
    int num2[101][101] = {};
    
    scanf("%d %d", &N, &M);
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++)
            scanf("%d", &(num1[i][j]));
    }
    
    scanf("%d %d", &M, &K);
    
    for(int i = 0; i < M; i++){
        for(int j = 0; j < K; j++)
            scanf("%d", &(num2[i][j]));
            
    }
    
    // for(int i = 0; i < M; i++){
    //     for(int j = 0; j < K; j++)
    //         printf("%d ", (num2[i][j]));
            
    //     printf("\n");
    // }
    
    for(int i = 0; i < N; i++){
        // num1에 행 하나를 선택
        
        // printf("num1 행 : %d\n", i);
        for(int j = 0; j < K; j++){
            // num2에 열 하나를 선택
            
            // printf("num2 열 : %d\n", j);
            
            int sum = 0;
            for(int k = 0; k < M; k++){
                // printf("num1 열, num2 행 : %d\n", k);
                // printf("[%d][%d], [%d][%d]\n", i, k, k, j);
                
                sum += (num1[i][k] * num2[k][j]);
                // printf("%d * %d = %d, %d\n", num1[i][k], num2[k][j], num1[i][k] * num2[k][j], sum);
            }
            
            printf("%d ", sum);
            
        }
        
        printf("\n");
    }
    
    

    return 0;
}
