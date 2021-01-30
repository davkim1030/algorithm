#include<iostream>

using namespace std;

int main(void){
	int t, h, w, n;

	cin >> t;
	for (int i = 0; i < t; i++){
		cin >> h >> w >> n;
		int a, b;
		b = n / h + 1;
		a = n % h;
		if (a == 0){
			a = h;
			b--;	
		}
		if (b <= 9)
			cout << a << "0" << b << "\n";
		else
			cout << a << b << "\n";
	}
	return (0);
}
