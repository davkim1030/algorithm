#include <iostream>
#include <vector>

using namespace std;

void getP(int n, int m, int idx, vector<int> total, vector<bool> & cache, vector<int> list)
{
    if (idx == m)
    {
        for (int i = 0; i < m - 1; i++)
        {
            cout << list[i] << " ";
        }
        cout << list[m - 1] << "\n";
        return;
    }

    for (int i = 0; i < n; i++)
    {
        if (!cache[i])
        {
            cache[i] = true;
            list[idx] = total[i];
            getP(n, m, idx + 1, total, cache, list);
            cache[i] = false;
        }
    }
}

int main()
{
    vector <int> total;
    vector <bool> cache;
    vector <int> list;
	int n, m;

    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        total.push_back(i + 1);
        cache.push_back(false);
    }

    for (int i = 0; i < m; i++)
    {
        list.push_back(0);
    }

    getP(n, m, 0, total, cache, list);

    return 0;
}
