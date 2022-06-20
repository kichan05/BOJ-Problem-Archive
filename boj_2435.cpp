#include <iostream>
#include <algorithm>

using namespace std;

long long int sums[101] = {0,};

int main(){
    long long int N, K, n, mx = -9999999;
    
    scanf("%lld %lld", &N, &K);
    
    for(int i = 1; i <= N; i++){
        scanf("%lld", &n);
        
        sums[i] = n + sums[i - 1];
        
        if(i < K){
            
        }
        else {
            n = sums[i] - sums[i - K];
            
            mx = max(n, mx);
            
            // printf("%d : %d\n", i, n);
        }
    }
    
    printf("%lld", mx);
    

    return 0;
}
