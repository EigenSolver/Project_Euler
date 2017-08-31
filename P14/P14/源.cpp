#include<iostream>
#include<algorithm>

using namespace std;

long long next(long long n) 
{
	if (n % 2 == 0)
		return n / 2;
	else
		return 3 * n + 1;
}

long collatz_len(long n)
{
	if (n == 1)
		return 0;
	return 1 + collatz_len(next(n));
}

int main()
{
	cout << collatz_len(27) << endl;
	system("pause");
	return 0;
}

int main()
{
	int start = 0;//113382;
	int max_length = 1;
	int result;
	int cache[10000];
	cache[0] = 0;
	cache[1] = 0;

	for (int i = 1; i < 10000; i++) 
	{
		start += 1;
		long long temp = start;
		int count = 1;

		if (start % 10000 == 0)
		{
			cout << start << "  is finished!" << endl;
		}

		while (temp != 1)
		{
			temp = next(temp);
			if (temp <= 0)
			{
				cout << "Error" << endl;
				system("pause");
				return 1;
			}
			if (temp < start && temp < 10000) 
			{
				count += cache[temp];
				break;
			}
			count += 1;
		}

		if (start < 10000)
		{
			cache[start] = count;
		}

		if (count>max_length)
		{
			max_length = count;
			result = start;
		}
	}
	cout << result << " " << max_length << endl;
	system("pause");
	return 0;
}