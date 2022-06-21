#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
  int nums[5] = {};
  int result = 1;

  for(int i = 0; i < 5; i++) scanf("%d", nums + i);

  while(1){
    // printf("%d : ", result);
    int sum = 0;

    for(int i = 0; i < 5; i++){
      sum += (result % nums[i] == 0);
    }

    if(sum >= 3){
      printf("%d", result);
      break;
    }

    // printf("x %d\n", sum);
    result++;
  }
}
