#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int count, sum1 = 0, sum2 = 0, n;

  scanf("%d", &count);

  while(count--){
    scanf("%d", &n);

    sum1 += (n / 30 + 1) * 10;
    sum2 += (n / 60 + 1) * 15;
  }


  if(sum1 > sum2){
    printf("M %d", sum2);
  }
  else if(sum1 < sum2) printf("Y %d", sum1);
  else printf("Y M %d", sum1);
}
