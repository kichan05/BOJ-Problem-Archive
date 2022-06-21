#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {  
  int mun, _mun, length = 0, i, isFirst = 1;

  scanf("%d", &_mun);
  mun = _mun;

  while(mun != 0){
    length++;
    mun /= 10;
  }

  mun = _mun;

  while(--length >= 0){
    int num = 0;
    int nums[10] = {};
    i = mun / (int)pow(10, length);
    

    while(i >= 2){
      nums[num++] = i % 2;

      i /= 2;
    }

    nums[num++] = i;
    
    mun %= (int)pow(10, length);

    if (!isFirst) {
      for(int i = 0; i < 3 - num; i++){
        printf("0");
      }
    }

    while(--num >= 0){
      printf("%d", nums[num]);
    }

    // printf("\n");

    isFirst = 0;
  }
}
