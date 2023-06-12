#include <stdio.h>

int main () {
    int arr[] = {40,10,60,7};
    int* ptr = arr;
    int temp = *ptr;
    for(int i = 1; i<4;i++){
        if(temp < *(ptr+i)){
            temp = *(ptr+i);
        }
    } 
    printf("%d",temp);
}