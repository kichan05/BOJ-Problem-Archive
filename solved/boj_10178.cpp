#include <iostream>

using namespace std;

int main(){
    int T, c, v;
    
    scanf("%d", &T);
    while(T--){
        scanf("%d %d", &c, &v);
        
        printf("You get %d piece(s) and your dad gets %d piece(s).\n", c / v, c % v);
    }

    return 0;
}
