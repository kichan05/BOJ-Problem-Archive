#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int H, M, S, A, p;

  scanf("%d %d %d %d", &H, &M, &S, &A);
  
  S += A;
  p = S / 60;
  S %= 60;

  M += p;
  p = M / 60;
  M %= 60;

  H += p;
  H %= 24;

  printf("%d %d %d", H, M, S);
  
}
