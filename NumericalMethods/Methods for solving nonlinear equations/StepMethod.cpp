#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;


double functionForGivenFunction(double variableX)
{
    double variableForFunction;

    variableForFunction =  pow(variableX, 3) + sin(variableX) - 12 * variableX + 1; //for example


    return variableForFunction;
}

int main()
{
    double variableForLimitA;
    double variableForLimitB;
    double variableForNumberOfIterations;
    double variableForStep;
    double variableX;
    unsigned int variableForRootOfEquation = 0;

    cout << "Input LimitA: " << endl;
    cin >> variableForLimitA;
    cout << "Input LimitB: " << endl;
    cin >> variableForLimitB;
    cout << "Input number of iterations: " << endl;
    cin >> variableForNumberOfIterations;

    variableForStep = (variableForLimitB - variableForLimitA) / variableForNumberOfIterations;

    cout << endl;


    cout << "LimitA =  " << variableForLimitA << endl;
    cout << "LimitB =  " << variableForLimitB << endl;
    cout << "Number of iterations = " << variableForNumberOfIterations << endl;
    cout << "Step  = " << variableForStep << endl;

    cout << endl;


    cout << setw(15) << "x" << setw(15) << "f(x)" << endl;

    for(variableX = variableForLimitA; variableX <= variableForLimitB; variableX += variableForStep)
    {
        cout << setw(15) << variableX << setw(15) << functionForGivenFunction(variableX);

        if(variableX < variableForLimitB && functionForGivenFunction(variableX) * functionForGivenFunction(variableX + variableForStep) < 0)
        {
            cout << " --> Isolation gap [" << variableX  << ";" << variableX + variableForStep << "]" << endl;
            variableForRootOfEquation += 1;
        }
        else
        {
            cout << endl;
        }
    }

    cout << endl;
    cout << "Number of roots = " << variableForRootOfEquation << endl;

    return 0;
}
