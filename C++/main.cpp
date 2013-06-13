// Programiffication

// Includes
#include <iostream> 
#include <string>

using namespace std;

// Constants

// Variables
int varA = 5;
int varB = 4;
string myString = "This is a string";

// PrintNum function
int multNum(int num1, int num2) {
	int number = num1 * num2;
	cout << number << "\n";
	return 0;
}

// Main function
int main() {
	cout << "Hello, World!\n";
	multNum(varA, varB);
	cout << myString << "\n";
	return 0;
}


