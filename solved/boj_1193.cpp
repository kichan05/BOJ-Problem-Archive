#include <iostream>

using namespace std;

int main(){
    int X, count = 0, parent = 0, child = 0, rowCount = 0;
    scanf("%d", &X);
    
    for(int i = 2; ; i++){
        rowCount++;
        if(rowCount % 2 == 0){
            for(int c = 1; i - c  >= 1; c++){
                count++;
                // printf("%d %d %d/%d\n", rowCount, count, c, i - c);
                
                if(count == X){
                    child = c;
                    parent = i - c;
                    break;
                }
            }
        }
        else{
            for(int c = i - 1; c >= 1; c--){
                count++;
                // printf("%d %d %d/%d\n", rowCount, count, c, i - c);
                
                if(count == X){
                    child = c;
                    parent = i - c;
                    break;
                }
            }
        }
        
        if(count == X)
            break;
    }
    
    printf("%d/%d", child, parent);

    return 0;
}
