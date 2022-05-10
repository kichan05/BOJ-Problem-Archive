#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  long long int N, F;
  long long int N_;



  scanf("%lld %lld", &N, &F);
  N_ = N / 100 * 100;
  // printf("%lld\n", N_);
  
  for(int i = 0; i < 100; i++){
    if((long long int)(N_ + i) % F == 0.0) {
        printf("%02d", i);
        break;
      }
  }
}

