#include<iostream>

using namespace std;

struct node
{
	int data;
	node *right = NULL;
	node *left = NULL;
	node(int num)
	{
		data = num;
	}
};

int countNodes(node *root)
{
	if (root == NULL)
		return 0;
	else
	{
		int count = 1;
		count += countNodes(root->left);
		count += countNodes(root->right);
		return count;
	}
}

void preorderPrint(node *root)
{
	if (root!=NULL)
	{
		cout << root->data << ' ';
		preorderPrint(root->left);
		preorderPrint(root->right);
	}
}

void postorderPrint(node *root)
{
	if (root!=NULL)
	{
		postorderPrint(root->left);
		postorderPrint(root->right);
		cout << root->data << ' ';
	}
}

void inorderPrint(node *root)
{
	if (root!=NULL)
	{
		inorderPrint(root->left);
		cout << root->data << ' ';
		inorderPrint(root->right);
	}
}

bool treeContains(node *root, int item)
{
	if (root==NULL)
	{
		return false;
	}
	else if (item == root->data)
	{
		return true;
	}
	else if (item<root->data)
	{
		return treeContains(root->left, item);
	}
	else if (item>root->data)
	{
		return treeContains(root->right, item);
	}
}

void treeInsert(node *root, int item)
{
	if (root == NULL)
	{
		root = new node(item);
		return;
	}
	else if (item < root->data)
	{
		treeInsert(root->left, item);
	}
	else
		treeInsert(root->right, item);
}

void addRight(node *root, node *right)
{
	root->right = right;
}

void addLeft(node *root, node *left)
{
	root->left = left;
}

void addChildren(node *root, node *left, node *right)
{
	addLeft(root, left);
	addRight(root, right);
}

