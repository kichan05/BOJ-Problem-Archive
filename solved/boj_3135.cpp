#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main(){
    int A, B, N, ns[6], n;
    
    scanf("%d %d", &A, &B);
    scanf("%d", &N);
    
    int minDiff = abs(A - B);
    
    for(int i = 0; i < N; i++){
        scanf("%d", &n);
        
        minDiff = min(minDiff, abs(B - n));
    }
    
    if(minDiff != abs(A - B))
        minDiff++;
        
    printf("%d", minDiff);
    

    return 0;
}
