#include <iostream>
#include <algorithm> 

using namespace std;

int isSame(int* arr1, int* arr2, int length){
  for(int i = 0; i < length; i++){
    if(arr1[i] != arr2[i]) return 0;
  }

  return 1;
}

int main() {
  int nums[8], _nums[8];

  for(int i = 0; i < 8; i++) {
    scanf("%d", nums + i);
    _nums[i] = nums[i];
  }

  sort(nums, nums + 8);
  if(isSame(nums, _nums, 8)){
    printf("ascending");
    return 0;
  }
  
  sort(nums, nums + 8, greater<int>());
  if(isSame(nums, _nums, 8)){
    printf("descending"); 
    return 0;
  }

  printf("mixed");

  return 0;
}
