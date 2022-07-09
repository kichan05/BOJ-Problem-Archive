#include <iostream>

using namespace std;

int main(){
    int N, M, n;
    int arr1[101][101];
    
    scanf("%d %d", &N, &M);
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            scanf("%d", &arr1[i][j]);
        }
    }
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            scanf("%d", &n);
            
            arr1[i][j] += n;
        }
    }
    
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            printf("%d ", arr1[i][j]);
        }
        printf("\n");
    }
    
    
    

    return 0;
}
