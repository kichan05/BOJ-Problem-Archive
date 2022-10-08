#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int N;
    
    scanf("%d", &N);
    
    if(N >= 0){
        int i;
    
        for(i = 0; N != 0; i++){
            N /= 2;
        }
        
        printf("%d", max(i, 1));
    }
    else {
        printf("32");
    }

    return 0;
}
