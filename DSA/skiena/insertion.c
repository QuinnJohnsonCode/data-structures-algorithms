#include <stdio.h>
#include "common.h"

void insertion_sort(int arr[], int n);


int main(void)
{
    int arr[5] = { 4, 7, 3, 1, 6 };
    int n = 5;

    printf("PRESORT: ");
    print_integer_array(arr, n);

    // Perform Sort
    insertion_sort(arr, n);

    printf("POSTSORT: ");
    print_integer_array(arr, n);

    return 0;
}

void insertion_sort(int arr[], int n)
{
    int i, j;

    for (i = 1; i < n; ++i)
    {
        j = i;
        while ((j > 0) && (arr[j] < arr[j - 1]))
        {
            swap_two_integers(&arr[j], &arr[j - 1]);
            j--;
        }
    }
}
