#include <iostream>

using namespace std;

int main() {
    int N;
    
    scanf("%d", &N);
    
    while(N > 0){
        for(int i = 0; i < N; i++){
            printf("*");
        }
        printf("\n");
        N--;
    }
}
