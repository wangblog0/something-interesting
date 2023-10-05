#include<stdio.h>

int main(void)
{
    int r;
    double pi=3.1415926, volumn;

    printf("Please enter the radius of a aphere: r = ");
    scanf("%d", &r);

    volumn = 4.0f/3.0f * pi * r * r * r;

    printf("The volumn of the aphere is: %f\n",volumn);

    return 0;
}
