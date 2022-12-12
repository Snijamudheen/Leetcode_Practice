/*A C++ program to calculate area of a circle, perimeter of a rectangle and the force between two bodies of masses M1 and M2. The program will run indefinitely until the user types in Q or q to terminate the program.*/

#include <iostream>
#include <cmath>
using namespace std;

//function prototypes
void Menu();
double AreaOfACircle(double);
int PerimeteofARetangle(int,int);
double Force(int,int,int);
double PresentValue(double &f);

//constants
#define PI 3.14
#define K 6.67 * pow(10,-8)

int main(){

    char choice;

    do{

        Menu();
        cin >> choice;

        // input and output commands for area of circle
        if(choice == 'A' || choice == 'a'){


            float R;
            float area;

            cout << "\n";
            cout << "You have entered " << choice << ". - Area of a circle will be calculated" << endl;
            cout << "Please Enter the Radius(R): ";
            cin >> R;

            area = AreaOfACircle(R);
            cout << "Area of a circle is: " << area << endl;
            cout << "\n\n";

        }

        //input and output commands for perimeter of a rectangle 
        else if(choice == 'P' || choice == 'p'){

            float L;
            float W;
            double perimeter;

            cout << "\n";
            cout << "You have entered " << choice << ". - Perimeter will be calculated." << endl;
            cout << "Please Enter Length (L) and Width (W): ";
            cin >> L >> W;

            perimeter = PerimeteofARetangle(L,W);
            cout << "Perimeter of a rectangle is: " << perimeter << endl;
            cout << "\n\n";
        }

        //input and output commands for force between the bodies
        else if(choice == 'F' || choice == 'f'){

            float M1;
            float M2;
            float d2;
            double F;
            double current;

            cout << "\n";
            cout << "You have entered " << choice << ". - The force between the bodies calculation." << endl;
            cout << "Please Enter M1 M2 d2: ";
            cin >> M1 >> M2 >> d2;

            F = Force(M1,M2,d2);
            cout << "Force is: " << F << endl;

            current = PresentValue(F);
            cout << "Current value of f is: " << current << endl;
            cout << "\n\n";
        }

        //Display message for terminating the program
        else if(choice == 'Q' || choice == 'q'){

            cout << "Program terminating....\n";
        }

        //input validation
        else{

            cout << "\n";
            cout << "Invalid character. Please enter your choice again." << endl;

            Menu();
            cin >> choice;
        }

    }while((choice != 'q') && (choice != 'Q'));

}

//function to display the menu to the user and ask input from user
void Menu(){

    cout << "Menu:\n"
         << "(A or a) - Area of a Circle\n"
         << "(P or p) - Perimeter of a rectangle\n"
         << "(F or f) - Newton's Law of Force\n"
         << "(Q or q) - to terminate the program enter q\n"
         << "Please enter your choice: " << endl;

}

//function to calculate the area of a circle
double AreaOfACircle(double rad){

    double area;

    area = PI * rad * rad;
    return area;

}

//function to calculate the perimeter of a rectangle
int PerimeteofARetangle(int len,int wid){

    double peri;

    peri = 2 * len + 2 * wid;
    return peri;

}

//function to calculate force between two bodies of masses M1 and M2 with a distance d^2 between them.
double Force(int mass1,int mass2,int dist){

    double F;

    F = ((K * mass1 * mass2) / (dist * dist));
    return F;

}

//function to display the present value of force using reference variable f
double PresentValue(double &f){

    return f;

}
