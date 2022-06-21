#include <iostream>

using namespace std;

int Rev(int _N){
    int N = _N;
    int reuslt = 0;
    
    while(N != 0){
        reuslt += N % 10;
        reuslt *= 10;
        N /= 10;
    }
    
    return reuslt / 10;
}

int main()
{
    int X, Y;
    
    scanf("%d %d", &X, &Y);
    
    printf("%d", Rev(Rev(X) + Rev(Y)));
    

    return 0;
}
