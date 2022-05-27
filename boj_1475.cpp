#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int nums[10] = {};

int main() {
  int N, count = 0;
  
  scanf("%d", &N);

  while(N > 0){
    int n = N % 10;

    if(nums[n] > 0) nums[n]--;
    else if(n == 6 && nums[9] > 0) nums[9]--;
    else if(n == 9 && nums[6] > 0) nums[6]--;
    else {
      count++;
      for(int i = 0; i < 10; i++){
        if(i != n) nums[i]++;
      }
    }
    
    N /= 10;
  }

  printf("%d", count);
}
