/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hyukim <hyukim@student.42seoul.kr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/01/19 23:35:59 by hyukim            #+#    #+#             */
/*   Updated: 2021/01/19 23:39:29 by hyukim           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <math.h>
#include <vector>
#include <stack>
#include <queue>

using namespace std;

static void	dfs(int g[][1001], int from, int n)
{
	stack<int>	stack;
	bool		visited[n + 1];
	int			tmp;

	for (int i = 0; i < n + 1; i++)
		visited[i] = 0;
	stack.push(from);
	while (!stack.empty())
	{
		tmp = stack.top();
		stack.pop();
		if (visited[tmp] == false)
		{
			visited[tmp] = true;
			cout << tmp << " ";
		}
		for (int i = n; i > 0; i--)
		{
			if (g[tmp][i] == 1 && visited[i] == false)
				stack.push(i);
		}
	}
	cout << "\n";
}

static void	bfs(int g[][1001], int from, int n)
{
	queue<int>	queue;
	bool		visited[n + 1];
	int			tmp;

	for (int i = 0; i < n + 1; i++)
		visited[i] = 0;
	queue.push(from);
	while (!queue.empty())
	{
		tmp = queue.front();
		queue.pop();
		if (visited[tmp] == false)
		{
			visited[tmp] = true;
			cout << tmp << " ";
		}
		for (int i = 1; i <= n; i++)
		{
			if (g[tmp][i] == 1 && visited[i] == false)
				queue.push(i);
		}
	}
	cout << "\n";
}

int			main(void)
{
	int		n;	// 정점
	int		m;	// 간선
	int		v;	// 시작
	int		tmp[2];
	int		g[1001][1001] = { 0 };

	cin >> n >> m >> v;
	for (int i = 0; i < m; i++)
	{
		cin >> tmp[0] >> tmp[1];
		g[tmp[0]][tmp[1]] = 1;
		g[tmp[1]][tmp[0]] = 1;
	}
	dfs(g, v, n);
	bfs(g, v, n);
	return (0);
}
