#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
  int D, H, W;
  float a;

  scanf("%d %d %d", &D, &H, &W);
  a = sqrt((float)pow(D, 2) / (pow(H, 2) + pow(W, 2)));
  cout << floor(H * a) << " " << floor(W * a);
}
