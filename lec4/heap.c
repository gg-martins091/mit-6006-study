#include <stdio.h>
#include <stdlib.h>

void print_array(int* a, int size) {
        for(int i = 0; i < size; i++) {
                printf("%d, ", a[i]);
        }
	printf("\n");
}

void max_heapify(int* a, int i, int size) {
	int left = (2 * i) + 1; // this is zero indexed
	int right = (2*i) + 2; // this is zero indexed
	int largest = i;

	// return because this is a leaf
	if (left > size || right > size) {
		return;
	}

	if (a[left] > a[i]) {
		largest = left;
	}

	if (a[right] > a[largest]) {
		largest = right;
	}

	if (largest != i) {
		int tmp = a[i];
		a[i] = a[largest];
		a[largest] = tmp;
		max_heapify(a, largest, size);
	}
}

int main(int argc, char **argv) {
        int a[] = {9, 1, 3, 5, 2, 0, 4, 8, 12};
	int size = sizeof(a)/sizeof(int);
        int heap[size];
	printf("Starting with array: \n");
	print_array(a, size);

	// build a max heap by heapifying each subtree
        for(int i = (size / 2) - 1; i >= 0; i--) {
                max_heapify(a, i, size);
        }

	printf("Max heap: \n");
	print_array(a, size);
}
