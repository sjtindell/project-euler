#include <stdio.h>

int main(int argc, char *argv[])
{
	int tmp = 0;
	int a = 0;
	int b = 1;
	int sum = 0;

	while (b < 4000000) {
		tmp = a;
		a = b;
		b += tmp;
		if (b < 4000000 && b % 2 == 0) {
			sum += b;
			}
	}

	printf("sum: %d\n", sum);

	return 0;
}

