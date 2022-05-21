#include <iostream>
#include <algorithm> 
#include <cmath>

using namespace std;

int is(int num){
  int n;
  
  while(num > 0){
    n = num % 10;
    if(n != 4 && n != 7) return 0;

    num /= 10;
  }

  return 1;
}

int main() {
  int N;

  scanf("%d", &N);

  for(int i = N; i > 0; i--){
    if(is(i)){
      printf("%d", i);
      break;
    }
  }
}
