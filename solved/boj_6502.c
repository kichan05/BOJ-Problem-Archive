#include <stdio.h>
#include <math.h>

int main() {
    int r, w, l, maxH;
    
    int i = 1;
    
    while(1) {
        scanf("%d %d %d", &r, &w, &l);
        if(r == 0)
            break;
        
        maxH = sqrt(4 * r * r - w * w);
        
        printf("Pizza %d ", i);
        if(l <= maxH)
            printf("fits on the table.\n");
        else
            printf("does not fit on the table.\n");
            
        i++;
    }

    return 0;
}
