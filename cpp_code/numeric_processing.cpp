/*A C++ program that opens the file named 'Random' that contains random numbers, reads all the numbers from the file, and calculates the following:
The number of numbers in the file
The sum of all the numbers in the file (a running total)
The average of all the numbers in the file The program displays the number of numbers found in the file, the sum of the numbers, and the average of the numbers.*/

#include <iostream>
#include <fstream>
using namespace std;

int main ()
{
      int aNumber = 0;
      int numbers = 0;
      double sum = 0.0;
      double average = 0.0;
      
      ifstream randomFile;
      randomFile.open("Random.txt");
      
      if(randomFile.fail())
            cout << "failed to read file.";
      
      else
      {
            while (randomFile >> aNumber)
            {
              numbers++;
              sum += aNumber;
            }
            
            if (numbers > 0)
                  average = sum / numbers; 
            else
                  average = 0.0;
        
            cout << "Number of numbers: " << numbers << "\n";
            cout << "Sum of the numbers: " << sum << "\n";
            cout << "Average of the numbers: " << average;
      }
      
      randomFile.close();
      
      return 0;
}
