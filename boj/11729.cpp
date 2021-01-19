/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   11729.cpp                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: hyukim <hyukim@student.42seoul.kr>         +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/01/19 23:51:02 by hyukim            #+#    #+#             */
/*   Updated: 2021/01/19 23:51:06 by hyukim           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <iostream>
#include <math.h>

using namespace std;

void	hanoi(int n, int from, int to, int tmp)
{
	if (n >= 2)
		hanoi(n - 1, from, tmp, to);
	cout << from << " " << to << "\n";
	if (n >= 2)
		hanoi(n - 1, tmp, to, from);
}

int		main(void)
{
	int		n;
	int		x;

	cin >> n;
	x = pow(2, n) - 1;
	cout << x << "\n";
	hanoi(n, 1, 3, 2);
	return (0);
}
