#include <iostream>
#include <iomanip>
#include <cmath>
#define maxDeltaCircumference 0.9999999999999
using namespace std;

double functionForDifferentiation(double variableX)
{

    return pow(variableX, 3) + sin(variableX) - 12 * variableX - 1; //for example
}

int main()
{
    double variableX;
    double variableDeltaCircumference;
    double variableForDerivativeLeftMethod;
    double variableForDerivativeRightMethod;
    double variableForDerivativeCentralMethod;
    double variableForSecondOrderDerivative;

    unsigned variableForMethodSelection;


    cout << "Input value of variableX:" << endl;
    cin >> variableX;
    cout << "Input value of delta circumference:" << endl;
    cin >> variableDeltaCircumference;

    if(variableDeltaCircumference > maxDeltaCircumference)
    {
        cout << "Value of delta circumference must be negative than 0.999, restart program" << endl;
        return 0;
    }
    else
    {
        cout << "Choose method:\n "
                "1.Left\n"
                "2.Right\n"
                "3.Central\n"
                "4.Second order derivative\n"
                "5.All of the methods for first order derivative" << endl;
        cin >> variableForMethodSelection;

        switch (variableForMethodSelection)
        {
            case 1:
            {
                variableForDerivativeLeftMethod = (functionForDifferentiation(variableX) - functionForDifferentiation(variableX - variableDeltaCircumference)) / variableDeltaCircumference;
                cout << "Derivative by left method = " << variableForDerivativeLeftMethod << endl;
                break;

            }
            case 2:
            {
                variableForDerivativeRightMethod = (functionForDifferentiation(variableX + variableDeltaCircumference) - functionForDifferentiation(variableX)) / variableDeltaCircumference;
                cout << "Derivative by right method = " << variableForDerivativeRightMethod << endl;
                break;
            }
            case 3:
            {
                variableForDerivativeCentralMethod = (functionForDifferentiation(variableX + variableDeltaCircumference) - functionForDifferentiation(variableX - variableDeltaCircumference)) / (2 * variableDeltaCircumference);
                cout << "Derivative by central method = " << variableForDerivativeCentralMethod << endl;
                break;
            }
            case 4:
            {
                variableForSecondOrderDerivative = (functionForDifferentiation(variableX + variableDeltaCircumference) - 2 * functionForDifferentiation(variableX) + functionForDifferentiation(variableX - variableDeltaCircumference)) / (variableX * variableDeltaCircumference);
                cout << "Second order derivative = " << variableForSecondOrderDerivative << endl;
                break;
            }
            case 5:
            {
                variableForDerivativeLeftMethod = (functionForDifferentiation(variableX) - functionForDifferentiation(variableX - variableDeltaCircumference)) / variableDeltaCircumference;

                variableForDerivativeRightMethod = (functionForDifferentiation(variableX + variableDeltaCircumference) - functionForDifferentiation(variableX)) / variableDeltaCircumference;

                variableForDerivativeCentralMethod = (functionForDifferentiation(variableX + variableDeltaCircumference) - functionForDifferentiation(variableX - variableDeltaCircumference)) / (2 * variableDeltaCircumference);

                cout << setw(15) << "Left Method" << setw(15) << "Right Method" << setw(15) << "Central Method" << endl;

                cout << setw(15) << variableForDerivativeLeftMethod << setw(15) << variableForDerivativeRightMethod << setw(15) << variableForDerivativeCentralMethod;
            }

        }
    }

    

    return 0;
}

