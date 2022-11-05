#include<iostream>
using namespace std;
int NUMBER=3;

int get(int* tab,int val,int* coins){
	if (tab[val]!=INT_MAX)
		return tab[val];		
	int min=INT_MAX;
	for(int i=0;i<NUMBER;i++)
		if(val-coins[i]>=0){
			int nVal = get(tab,val-coins[i],coins);
			if (nVal<min)
				min=nVal;
		}
	tab[val]=min+1;
	return tab[val];
}

int dynamic(int amount,int* coins) {
	int* tab = new int[amount+1];
	tab[0]=0;
	for(int i=1;i<=amount;i++)
		tab[i]=INT_MAX;
	return get(tab,amount,coins);	
}

int greedy(int amount,int* coins) {
	int actual = amount;
	int numberC = 0;
	for(int i=NUMBER-1;i>=0;i--)
		if (actual-coins[i]>=0){
			numberC+=actual/coins[i];
			actual=actual%coins[i];
		}
	return numberC;
}


int main() {
	int amount;
	int coins[NUMBER]={1,2,5};
	cout<<"Give an amount: ";
	cin>>amount;
	cout<<"Dynamic: "<<dynamic(amount,coins)<<endl;
	cout<<"Greedy: "<<greedy(amount,coins)<<endl;
}
