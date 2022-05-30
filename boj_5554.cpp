#include <iostream>

using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    printf("%d\n%d", (a + b + c + d) / 60, (a + b + c + d) % 60); 
}
