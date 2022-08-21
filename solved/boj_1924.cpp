#include <iostream>

using namespace std;

int main(){
    int x, y, count = 0;
    
    scanf("%d %d", &x, &y);
    
    for(int i = 1; i < x; i++){
        if(i == 2){
            count += 28;
            // printf("%d %d\n", i, 28);
        }
        else if(i == 4 or i == 6 or i == 9 or i == 11){
            count += 30;
            // printf("%d %d\n", i, 30);
        }
        else{
            count += 31;
            // printf("%d %d\n", i, 31);
        }
    }
    
    count += y;
    
    // printf("%d  ", count);  
    
    if(count % 7 == 0)
        printf("SUN");
    else if(count % 7 == 1)
        printf("MON");
    else if(count % 7 == 2)
        printf("TUE");
    else if(count % 7 == 3)
        printf("WED");
    else if(count % 7 == 4)
        printf("THU");
    else if(count % 7 == 5)
        printf("FRI");
    else if(count % 7 == 6)
        printf("SAT");

    return 0;
}
