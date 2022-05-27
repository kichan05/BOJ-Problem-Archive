#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

long long int sum_(long long int num){
  long long int sum = 0;
  while(num > 0){
    // printf("s : %d\n", num);
    sum += (long long int)(num % 10);
    num /= 10;
  }

  return sum;
}

int main() {
  long long int X, count = 0;

  scanf("%lld", &X);
//   printf("c : %lld\n", X);

  while(X >= 10){
    X = sum_(X);
    // printf("d : %lld\n", X);
    count++;
  }

  printf("%lld\n", count);

  if(X % 3 == 0) printf("YES");
  else printf("NO");
}
