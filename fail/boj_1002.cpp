#include <iostream>
#include <cmath>

using namespace std;

int main() {
    long long int T, x1, y1, r1, x2, y2, r2;
    long long int d1, d2;
    
    scanf("%d", &T);
    
    while(T--){
        scanf("%lld %lld %lld %lld %lld %lld", &x1, &y1, &r1, &x2, &y2, &r2);
        
        d1 = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2));
        d2 = r1 + r2;
        
        // printf("%d : ", T + 1);
        
        if(x1 == x2 && y1 == y2 && r1 != r2) printf("0\n");
        else if(x1 == x2 && y1 == y2 && r1 == r2) printf("-1\n");
        else if(d1 > d2) printf("0\n");
        else if(d1 == d2) printf("1\n");
        else if(d1 < d2) printf("2\n");
        else printf("0\n");
        
    }
}
