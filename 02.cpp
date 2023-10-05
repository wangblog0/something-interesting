#include<stdio.h>
int main(void)
{
    double x, f;

    printf("Please enter a value for x = ");
    scanf("%lf", &x);

    f=((((3*x+2)*x-5)*x-1)*x+7)*x-6;

    printf("%.5lf\n",f);

    return 0;
}
