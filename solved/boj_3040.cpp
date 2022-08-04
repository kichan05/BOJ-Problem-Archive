#include <iostream>

using namespace std;

int main(){
    int nums[10];
    int sum = 0;
    
    for (int i = 0; i < 9; i++){
        scanf("%d", nums + i);
        sum += nums[i];
    }
    
    for(int i = 0; i < 8; i++){
        for (int j = i + 1; j < 9; j++){
            // printf("%d %d\n", i, j);
            if(sum - nums[i] - nums[j] == 100){
                
                for (int k = 0; k < 9; k++){
                    if(k != i && k != j){
                        printf("%d\n", nums[k]);
                    }
                }
                
            }
        }
    }
    

    return 0;
}
