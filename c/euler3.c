#include <stdio.h>
#include <math.h>


int is_prime(int num)
{
	int i = 0;
	
	for(i = 2; i < num; i++) {
		if(num % i == 0) {
			return 1;
		}
	}
	
	return 0;
}



int main()
{
	long limit = 13195;
	int n = 2;
	
	for(n = 2; n < limit; n++) {
		if(limit % n == 0) {
			if(is_prime(n) == 0) {
				printf("%d\n", n);
			}
		}
	}

	return 0;
}	
