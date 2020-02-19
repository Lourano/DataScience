#include <iostream>
#include <cmath>
#define accuracyValue 0.0001
using namespace std;

double functionForGivenFunction(double variableX)
{
    double variableForFunction;

    variableForFunction = pow(variableX, 3) + sin(variableX) - 12 * variableX + 1; //for example


    return variableForFunction;
}

int main()
{
    double variableForLimitA;
    double variableForLimitB;
    double variableX;
    int variableForNumberOfIterations;

    cout << "Input limitA:" << endl;
    cin >> variableForLimitA;
    cout << "Input limitB:" << endl;
    cin >> variableForLimitB;


    cout << "LimitA = " << variableForLimitA << endl;
    cout << "LimitB = " << variableForLimitB << endl;
    cout << "Accuracy value = " << accuracyValue << endl;

    if(functionForGivenFunction(variableForLimitA) * functionForGivenFunction(variableForLimitB) < 0)
    {
        cout << "The condition is satisfied on the basis of variables that are specified by the user" << endl;

        variableForNumberOfIterations = 0;

        while(true)
        {
            variableX = (variableForLimitA + variableForLimitB) / 2.0;

            variableForNumberOfIterations += 1;

            if(fabs(functionForGivenFunction(variableX)) < accuracyValue)
            {
                break;
            }

            if(functionForGivenFunction(variableForLimitA) * functionForGivenFunction(variableX) < 0 )
            {
                variableForLimitA = variableForLimitA;
                variableForLimitB = variableX;
            }
            else
            {
                variableForLimitA = variableX;
                variableForLimitB = variableForLimitB;
            }
        }

        cout << "Root value = " << variableX << endl;
        cout << "Number of iterations = " << variableForNumberOfIterations << endl;

    }
    else
    {
        cout << "The condition is not met for convergence,\n "
                "you must change the input data or use another method" << endl;
        return 0;
    }
    return 0;
}
