#include<stdio.h>
int main(void)
{
    int money;

    printf("Please enter an acount : ");
    scanf("%d",&money);

    printf("$20 bills: %d\n", money/20);
    money = money % 20;

    printf("$10 bills: %d\n", money/10);
    money = money % 10;

    printf("$5 bills: %d\n", money/5);
    money = money % 5;

    printf("$1 bills: %d\n", money);

    return 0;

}
