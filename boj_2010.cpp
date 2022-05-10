#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int N, sum = 0, n;

  scanf("%d", &N);

  while(N--){
    scanf("%d", &n);

    sum += n - 1;

    if(N == 0) sum++;
  }

  printf("%d", sum);
  
}
