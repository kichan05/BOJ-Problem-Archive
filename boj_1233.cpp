#include <iostream>

using namespace std;

int count[60] = {};

int main() {
    int s1, s2, s3, sum = 0;
    
    scanf("%d %d %d", &s1, &s2, &s3);
    
    for(int i = 1; i <= s1; i++){
        for(int j = 1; j <= s2; j++){
            sum = 0;
            for (int k = 1; k <= s3; k++){
                sum = i + j + k;
                count[sum]++;
            }
        }
    }
    
    int max = 0, maxIdx = 0;
    
    for(int i = 1; i < 60; i++){
        if(max < count[i]) {
            max = count[i];
            maxIdx = i;
        }
    }
    
    printf("%d", maxIdx);
}
