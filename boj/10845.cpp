#include <iostream>
#include <deque>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int main(void)
{
	int n;

	scanf("%d\n", &n);
	deque<int> q;
	for (int i = 0; i < n; i++)
	{
		char tmp[12];
		scanf("%s", tmp);
		if (strcmp(tmp, "front") == 0)
		{
			if (q.size() == 0)
				printf("-1\n");
			else
				printf("%d\n", q.front());
		}
		else if (strcmp(tmp, "back") == 0)
		{
			if (q.size() == 0)
				printf("-1\n");
			else
				printf("%d\n", q.back());
		}
		else if (strcmp(tmp, "size") == 0)
			printf("%d\n", q.size());
		else if (strcmp(tmp, "empty") == 0)
			printf("%d\n", q.empty());
		else if (strcmp(tmp, "pop") == 0)
		{
			if (q.size() == 0)
				printf("-1\n");
			else
			{
				printf("%d\n", q.front());
				q.pop_front();
			}
		}
		else
		{
			int t;
			scanf("%d\n", &t);
			q.push_back(t);
		}

	}
	return 0;
}
