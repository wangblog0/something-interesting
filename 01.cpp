#include<stdio.h>
int main(void)
{
    float loan, rate, monthly_rate, payment;

    printf("Please enter an amount of loan : ");
    scanf("%f",&loan);

    printf("Please enter the rate : ");
    scanf("%f",&rate);

    printf("Please enter your monthly payment : ");
    scanf("%f", &payment);

    monthly_rate = rate/100.00f/12.00f;

    loan = loan - payment + monthly_rate * loan;
    printf("Balance remaining after first payment = $%.2f\n", loan);

    loan = loan - payment + monthly_rate * loan;
    printf("Balance remaining after second payment = $%.2f\n", loan);

    loan = loan - payment + monthly_rate * loan;
    printf("Balance remaining after third payment = $%.2f\n", loan);

    return 0;
}
