#include <stdio.h>

void encontrarIndices(int nums[], int tam, int target) {
    for (int i = 0; i < tam - 1; i++) {
        for (int j = i + 1; j < tam; j++) {
            if (nums[i] + nums[j] == target) {
                printf("Los indices que suman %d son: %d y %d\n", target, i, j);
                return;  
            }
        }
    }
    printf("No se encontraron dos números que sumen %d\n", target);
}

int main() {
    
    int nums[] = {2, 7, 11, 15};  
    int target;
    int tam = sizeof(nums) / sizeof(nums[0]);

    printf("Introduce el valor de target: ");
    scanf("%d", &target);

    encontrarIndices(nums, tam, target);

return 0;
}

