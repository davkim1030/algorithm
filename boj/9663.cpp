#include <iostream>

using namespace std;

void	n_queen(int n, int *answer, int v[], int x)
{
	for (int i = 0; i < x; i++)
		if (v[x] == v[i] || abs(v[i] - v[x]) == abs(i - x))
			return ;
	if (x == n - 1)
	{
		*answer += 1;
		return ;
	}
	for (int i = 0; i < n; i++)
	{
		v[x + 1] = i;
		n_queen(n, answer, v, x + 1);
	}
}

int		main()
{
	int n;
	int *v;
	int *answer = (int *)malloc(sizeof(int));

	cin >> n;
	v = (int *)malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
		v[i] = -1;

	*answer = 0;
	for (int i = 0; i < n; i++)
	{
		v[0] = i;
		n_queen(n, answer, v, 0);
	}
	cout << *answer << endl;
}
