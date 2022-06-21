#include <iostream>
#include <cmath>

using namespace std;

int main() {
    int N, sum = 0;
    scanf("%d", &N);
    
    for (int i = 0; i < 5; i++){
        sum += pow(N % 10, 5);
        N /= 10;
    }
    
    printf("%d", sum);
}
