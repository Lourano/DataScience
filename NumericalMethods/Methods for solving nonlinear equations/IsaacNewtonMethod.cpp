#include <iostream>
#include <cmath>
#define constForAccuracy 0.00001
#define constForMinAccuracy -10E10
using namespace std;

double functionForGivenFunction(double variableX)
{
    double variableForGivenFunction;

    variableForGivenFunction = pow(variableX, 3) + sin(variableX) - 12 * variableX + 1; //for example

    return variableForGivenFunction;

}
double givenFunctionFirstOrderDerivative(double variableX)
{
    double variableForFunctionFirstOrderDerivative;

    variableForFunctionFirstOrderDerivative = 3 * pow(variableX, 2) + cos(variableX) - 12; //for example

    return variableForFunctionFirstOrderDerivative;
}

double givenFunctionSecondOrderDerivative(double variableX)
{
    double variableForFunctionSecondOrderDerivative;

    variableForFunctionSecondOrderDerivative = 6 * variableX - sin(variableX); //for example
    return variableForFunctionSecondOrderDerivative;
}

int main()
{
    double variableForLimitA;
    double variableForLimitB;
    double variableX;
    int variableForNumberOfIterations;

    cout << "Input LimitA" << endl;
    cin >> variableForLimitA;
    cout << "Input LimitB" << endl;
    cin >> variableForLimitB;


    if(functionForGivenFunction(variableForLimitA) * givenFunctionSecondOrderDerivative(variableForLimitA) > 0)
    {
        cout << "The condition is satisfied on the basis of variables that are specified by the user;\n x = LimitA = " << variableForLimitA << endl;

        variableX = variableForLimitA;
    }
    else
    {
        if(functionForGivenFunction(variableForLimitB) * givenFunctionSecondOrderDerivative(variableForLimitB) > 0)
        {
            cout << "The condition is satisfied on the basis of variables that are specified by the user; x = LimitB = " << variableForLimitB << endl;
        }
        else
        {
            cout << "The condition is not met for convergence, you must change the input data or use another method" << endl;

            variableX = constForMinAccuracy;
        }
    }

    if(variableX > constForMinAccuracy)
    {
        variableForNumberOfIterations = 0;

        while(true)
        {
            variableX = variableX - functionForGivenFunction(variableX) / givenFunctionFirstOrderDerivative(variableX);

            variableForNumberOfIterations +=  1;

            if(fabs(functionForGivenFunction(variableX)) < constForAccuracy )
            {
                break;
            }
        }

        cout << "Root value = " << variableX << endl;
        cout << "Number of iterations = " << variableForNumberOfIterations << endl;
    }



}
