#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int		main(void)
{
	int			n;
	int			tmp;
	vector<int>	list;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		cin >> tmp;
		list.push_back(tmp);
	}
	sort(list.begin(), list.end());
	tmp = 0;
	for (int i = 1; i <= n; i++)
		tmp += i * list[list.size() - i];
	cout << tmp << "\n";
	return (0);
}
