#include <iostream>
#include <algorithm> 
#include <cmath>

using namespace std;

int sum(int N){
  int sum;
  sum = N;

  while(N > 0){
    sum += N % 10;
    N /= 10;
  }

  return sum;
}

int main() {
  int N, init = 0;

  scanf("%d", &N);

  for(int i = 0; i < N; i++){
    if(sum(i) == N) {
      init = i;
      break;
    }
  }

  printf("%d", init);
}
