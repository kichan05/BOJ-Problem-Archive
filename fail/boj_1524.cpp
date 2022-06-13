#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int T, result = 1;
    
    scanf("%d", &T);
    
    while(T--){
        int N, M, n, _N, _M;
        int s[1000001] = {};
        int b[1000001] = {};
        
        scanf(" %d %d", &N, &M);
        _N = N;
        _M = M;
        
        for(int i = 0; i < N; i++){
            scanf("%d", s + i);
        }
        for(int i = 0; i < M; i++){
            scanf("%d", b + i);
        }
        
        // for(int i = 0; i < N; i++) printf("%d, ", s[i]);
        // printf("\n");
        // for(int i = 0; i < M; i++) printf("%d, ", b[i]);
        // printf("\n");
        
        // for(int i = 0; i < _N; i++) printf("%d, ", s[i]);
        //     printf("\n");
        // for(int i = 0; i < _M; i++) printf("%d, ", b[i]);
        //     printf("\n");
        //     printf("\n");
        
        while(1){
            sort(s, s + N);
            sort(b, b + M);
            
            if(s[0] < b[0]){
                // printf("s의 %d 삭제\n", s[0]);
                s[0] = 300000001;
                N--;
            }
            else if(s[0] >= b[0]){
                // printf("b의 %d 삭제\n", b[0]);
                b[0] = 300000001;
                M--;
            }
            else{
                // printf("에러\n");
            }
            
            // for(int i = 0; i < _N; i++) printf("%d, ", s[i]);
            // printf("\n");
            // for(int i = 0; i < _M; i++) printf("%d, ", b[i]);
            // printf("\n");
            // printf("\n");
            
            
            if(N == 0 || M == 0) break;
        }
        
        if(N != 0){
            printf("S\n");
        }
        else {
            printf("B\n");
        }
    }

    return 0;
}
