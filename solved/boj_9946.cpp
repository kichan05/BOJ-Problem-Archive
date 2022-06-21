#include <string.h>
#include <stdio.h>

int main(){
    for(int i = 0; 1; i++){
        int num1['z' - 'a' + 1] = {0, };
        int num2['z' - 'a' + 1] = {0, };
        char str[1001];
        int result = 1;
        
        scanf("%s", str);
        
        for(int j = 0; str[j]; j++){
            num1[str[j] - 'a'] += 1;
        }
        
        scanf("%s", str);
        
        for(int j = 0; str[j]; j++){
            num2[str[j] - 'a'] += 1;
        }
        
        if(!strcmp(str, "END")) break;
        
        
        for(int j = 'a'; j <= 'z' && result; j++){
            result = num1[j - 'a'] == num2[j - 'a'];
        }
        
        if(result)
            printf("Case %d: same\n", i + 1);
        else
            printf("Case %d: different\n", i + 1);
    }

    return 0;
}
