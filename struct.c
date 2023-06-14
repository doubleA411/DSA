#include <stdio.h>


    struct Student {
        int rollNumber;
        char name[50];
        float marks;
    };

int main(){
    struct Student arr[5];
    for(int i = 0; i<5; i++){
        printf("Details of Student %d \n",i+1);
        printf("Roll number of %d \n",i+1);
        scanf("%d",&arr[i].rollNumber);
        printf("Name of %d \n", i + 1);
        scanf("%s", &arr[i].name);
        printf("Mark of %d \n", i + 1);
        scanf("%f", &arr[i].marks);
        printf("----------------------------------- \n");
    }

    for(int j = 0;j<5;j++){
        printf("Student %d \n",j+1);
        printf("Roll number : %d \n",arr[j].rollNumber);
        printf("Name : %s \n",arr[j].name);
        printf("Mark : %f \n", arr[j].marks);
    }

}


