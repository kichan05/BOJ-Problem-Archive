#include <iostream>

using namespace std;

long long int num[91];

long long int fibo(int n){
    if(n == 0)
        return 0;
        
    if(n == 1)
        return 1;
    
    if(num[n] > 0)
        return num[n];
        
    num[n] = fibo(n - 1) + fibo(n - 2);
        
    return num[n];
}

int main(){
    int n;
    scanf("%d", &n);
    
    printf("%lld\n", fibo(n));
    
    // for(int i = 2; i <= n; i++)
    //     printf("%d %lld\n", i, fibo(i));

    return 0;
}
