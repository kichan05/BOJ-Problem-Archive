#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int H, M, A, hp;

  scanf("%d %d", &H, &M);
  scanf("%d", &A);

  M += A;

  hp = M / 60;
  M = M % 60;
  
  H += hp;
  H %= 24;

  printf("%d %d", H, M);
  
}
