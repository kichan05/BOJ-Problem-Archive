#include <iostream>

using namespace std;

int main() {
    int N, sum = 0, conCount = 1, n;
    
    scanf("%d", &N);
    
    while(N--){
        scanf("%d", &n);
        
        if(n) {
            sum += conCount++;
        }
        else {
            conCount = 1;
        }
    }
    
    printf("%d", sum);
}
