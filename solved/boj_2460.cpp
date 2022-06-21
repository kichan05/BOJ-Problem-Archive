#include <iostream>

using namespace std;

int main() {
    int in, out, sum = 0, max = 0;
    
    for(int i = 0; i < 10; i++){
        scanf("%d %d", &out, &in);
        
        sum -= out;
        sum += in;

        // printf("sum : %d\n", sum);
      
        if(max < sum){
            max = sum;
        }
    }
    
    printf("%d", max);
}
