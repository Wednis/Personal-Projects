#include <stdio.h>

int main()
{
    int n, i;
    printf("Input the number of elements in the array: "); 
    scanf("%d", &n);
    int arr[n];
    printf("Input the elements of the array: \n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    int upCount = 0, downCount = 0;
    for (i = 0; i < n; i++)
    {
        if (arr[i] % 2 == 0)
        {
            downCount++;
        }
        else
        {
            upCount++;
        }
    }
    int upArray[upCount], downArray[downCount];
    int upIndex = 0, downIndex = 0;
    for (i = 0; i < n; i++)
    {
        if (arr[i] % 2 == 0)
        {
            downArray[downIndex++] = arr[i];
        }
        else
        {
            upArray[upIndex++] = arr[i];
        }
    }
    for (i = 0; i < upCount-1; i++)            //升序 
    {
        for (int j = 0; j < upCount-i-1; j++)
        {
            if (upArray[j] > upArray[j+1])
            {
                int temp = upArray[j];
                upArray[j] = upArray[j+1];
                upArray[j+1] = temp;
            }
        }
    }
    for (i = 0; i < downCount-1; i++)          //降序 
    {
        for (int j = 0; j < downCount-i-1; j++)
        {
            if (downArray[j] < downArray[j+1])
            {
                int temp = downArray[j];
                downArray[j] = downArray[j+1];
                downArray[j+1] = temp;
            }
        }
    }
    printf("\nAscending order: ");
    for (i = 0; i < upCount; i++)
    {
        printf("%d ", upArray[i]);
    }
    printf("\nDescending order: ");
    for (i = 0; i < downCount; i++)
    {
        printf("%d ", downArray[i]);
    }
    return 0;
}
