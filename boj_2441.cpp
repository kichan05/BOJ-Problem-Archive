#include <iostream>

using namespace std;

int main() {
    int N, _N;
    scanf("%d", &N);
    
    _N = N;
    
    // N + i =_N
    
    while(N > 0){
        for(int i = 0; i < _N - N; i++) printf(" ");
        for(int i = 0; i < N; i++) printf("*");
        
        printf("\n");
        N--;
    }
}
