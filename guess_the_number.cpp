/*This C++ game tests a player's ability to guess a random number between 1 and 100 with the fewest number of attempts. The computer tells the player whether he entered the guess too high, too low, or right each time he does. The game ends when the player guesses the number.*/

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() 
{
	int num, guess, attempts = 0;
	srand(time(0));
	num = 1 + (rand() % 100);
	
	cout << "THE GUESSING GAME" << endl;
	cout << "My number is between 1 and 100" << endl;

	do
	{
		cin >> guess;
 		tries++;

		if (num < guess)
			cout << "The number you entered is more than the given range." << endl;
		else if (num > guess)
			cout << "The number you entered is less than the given range." << endl;
		else
		  	cout << "Congratulation! You have guessed the correct number. You guessed it in " << tries << "." << endl;

	} while (guess =! num );
}
