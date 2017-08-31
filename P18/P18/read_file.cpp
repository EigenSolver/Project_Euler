#include<iomanip>
#include<fstream>
#include<iostream>
#include"node.cpp"

using namespace std;

int *read_digits()
{
	int numbers[120];
	ifstream file("digit_tree.txt");
	if (file)
	{
		for (int i = 0; i < 120; i++)
		{
			file >> numbers[i];
			cout << numbers[i] << ' ';
		}
		cout << endl;
		system("pause");
		return numbers;
	}
}


void main()
{

}

