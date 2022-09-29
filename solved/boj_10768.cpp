#include <iostream>

using namespace std;

int main(){
    int month, day;
    
    scanf("%d", &month);
    scanf("%d", &day);
    
    if(2 > month or (month == 2 && day < 18))
        printf("Before");
    else if(month == 2 && day == 18)
        printf("Special");
    else
        printf("After");

    return 0;
}
