#include <stdio.h>
#include <stdlib.h>
#include "common.h"

void swap_two_integers(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

void print_integer_array(int arr[], int n)
{
    for (int i = 0; i < n; ++i)
        printf("%d ", arr[i]);
    
    printf("\n");
}