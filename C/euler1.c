#include <stdio.h>

int main(int argc, char *argv[])
{
	int sum = 0;
	int i = 0;

	for (i = 1; i < 1000; i++) {
		if (i % 3 == 0) {
			sum += i;
		}

		else if (i % 5 == 0) {
			sum += i;
		}
	}

	printf("Sum: %d\n", sum);

	return 0;
}
