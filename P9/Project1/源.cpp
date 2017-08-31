
#include<iostream>
#include<cmath>
#include<algorithm>
#include<list>

using namespace std;

int main()
{
	int a = 1;
	for (int i = 1; i < 999; i++)
	{
		a += 1;
		int b = 1;
		for (int i = 1; i < 1000-a; i++)
		{
			b += 1;
			int c = 1000 - a - b;
			int numbers[3] = { a,b,c };
			sort(numbers, numbers + 3);
			if (pow(numbers[0], 2) + pow(numbers[1], 2) == pow(numbers[2], 2))
			{
				cout << a <<' '<< b <<' '<< c << endl;
			}
		}
	}
	cout << "Finished" << endl;
	system("pause");
	return 0;
}

