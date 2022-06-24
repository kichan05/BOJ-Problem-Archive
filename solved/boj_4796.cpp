#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    int L, P, V;
    
    for(int i = 1; ; i++){
        
        scanf("%d %d %d", &L, &P, &V);
        
        if(L + P + V == 0) break;
        
        printf("Case %d: %d\n", i, V / P * L + min(V % P, L));
        
    }

    return 0;
}
