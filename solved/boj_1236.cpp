#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int N, M, rowCount, colCount;
    int row[51] = {0,};
    int col[51] = {0,};
    
    char sel;
    
    scanf("%d %d", &N, &M);
    
    rowCount = N;
    colCount = M;
    
    for(int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            scanf(" %c", &sel);
            
            if(sel == 'X'){
                // printf("%d %d\n", i, j);
                if(row[i] == 0){
                    row[i] = 1;
                    rowCount--;
                }
                
                if(col[j] == 0){
                    col[j] = 1;
                    colCount--;
                }
            }
        }
    }
    
    
    printf("%d\n", max(rowCount, colCount));
    // printf("%d\n", rowCount);
    // printf("%d\n", colCount);
    
    

    return 0;
}
