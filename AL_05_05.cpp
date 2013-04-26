#include <iostream>
using namespace std;

int divisible(int x, int y, int z) {
	int d = 0;	// number of integers divisible by z
	for (int i = x; i <= y; i++) {
		if (i % z == 0) {
			d++;
		}
	}
	return d;
}

int main() {

	int a, b; // divisors
	cin >> a;
	cin >> b;
	int sp, sk; // range limits
	int answer;
	while (true) {
		cin >> sp;
		cin >> sk;
		answer = divisible(sp,sk,a) + divisible(sp,sk,b) - divisible(sp,sk,a*b);
		cout << answer << "\n";
	}

}

