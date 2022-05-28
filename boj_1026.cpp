#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  int N;
  int A[101] = {};
  int B[101] = {};

  scanf("%d", &N);

  for(int i = 0; i < N; i++) scanf("%d", A + i);
  for(int i = 0; i < N; i++) scanf("%d", B + i);

  sort(A, A + N);
  sort(B, B + N, greater<>());

  int sum = 0;
  for(int i = 0; i < N; i++){
    //printf("%d * %d = %d\n", A[i], B[i], A[i] * B[i]);
    sum += A[i] * B[i];
  }

  printf("%d", sum);
}
