#include <iostream>

using namespace std;

int main(){
    int N, v, count = 0;
    int nums[101];
    
    scanf("%d", &N);
    
    for(int i = 0; i < N; i++) scanf("%d", nums + i);
    
    scanf("%d", &v);
    
    for(int i = 0; i < N; i++) {
        if(nums[i] == v) count++;
    }
    
    printf("%d", count);
    

    return 0;
}
