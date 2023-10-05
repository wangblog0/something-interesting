#include <stdio.h>

int main(void)
{
    int item_number, month, day, year;
    float unit_price;

    printf("Please enter the item number : ");
    scanf("%d", &item_number);

    printf("Please enter the unit price : ");
    scanf("%f", &unit_price);

    printf("Please enter the purchase (mm/dd/yyyy) : ");
    scanf("%d/%d/%d", &month, &day, &year);

    printf("Item\t\t unit\t\t purchase\n\t\t number\t\t price\n");
    printf("%d\t\t $%7.2f\t %.2d/%.2d/%.4d", item_number, unit_price, month, day, year);

    return 0;
}
