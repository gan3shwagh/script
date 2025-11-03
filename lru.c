#include <stdio.h>

int main() {
    int pages[50], frames[10], temp[10];
    int n, f, i, j, k, pos, faults = 0;

    printf("Enter number of pages: ");
    scanf("%d", &n);

    printf("Enter page sequence:\n");
    for(i = 0; i < n; i++)
        scanf("%d", &pages[i]);

    printf("Enter number of frames: ");
    scanf("%d", &f);

    for(i = 0; i < f; i++)
        frames[i] = -1;

    printf("\nPage\tFrames\n");

    for(i = 0; i < n; i++) {
        int flag = 0;

        for(j = 0; j < f; j++) {
            if(frames[j] == pages[i]) {
                flag = 1;
                break;
            }
        }

        if(flag == 0) {
            for(j = 0; j < f; j++) {
                temp[j] = -1;
            }

            for(j = i - 1, k = 1; j >= 0; j--) {
                for(int m = 0; m < f; m++) {
                    if(frames[m] == pages[j] && temp[m] == -1) {
                        temp[m] = k++;
                    }
                }
            }

            int max = -1;
            for(j = 0; j < f; j++) {
                if(temp[j] > max) {
                    max = temp[j];
                    pos = j;
                }
            }

            frames[pos] = pages[i];
            faults++;
        }

        printf("%d\t", pages[i]);
        for(j = 0; j < f; j++) {
            if(frames[j] != -1)
                printf("%d ", frames[j]);
            else
                printf("- ");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults = %d\n", faults);
    return 0;
}
#gcc lru.c -o lru
#./lru
