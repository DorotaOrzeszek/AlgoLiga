#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

string dec2revbin(int n) {
// returns reversed binary representation of n
	string b; // n as binary
	int r;	// remainder
	stringstream temp; // temporary digit container
	while (true) {
		r = n % 2;
		n = n / 2;
		if (n == 0 && r == 0) {
			break;
		}
		temp << r;
	}
	b = temp.str();
	if (b == "") {	// for case n = 0
		b = "0";
	}
	return b; 	
}

int bin2dec(string s) {
// returns decimal representation of binary s
	int d = 0;	// will contain s as decimal
	for (int i = s.size()-1; i >= 0; i--) {
		int c = s.at(i) - '0';
		// calculating powers of 2
		int power = s.size()-1-i;
		int p = 1;
		for (int j = 0; j < power; j++) {
			p *= 2;
		}
		d += c * p;
	}
	return d;
}

int main () {
	int num;
	cout << "Enter Numbers" << '\n';
	while(cin >> num) {
		string revbinarynum = dec2revbin(num);
		cout << bin2dec( revbinarynum ) << "\n";	
	}
}
