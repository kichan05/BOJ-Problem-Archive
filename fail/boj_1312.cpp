#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  int A, B, N;

  scanf("%d %d %d", &A, &B, &N);

  printf("%lld", (long long int)((double)A / B * pow(10, N)) % 10);
}
