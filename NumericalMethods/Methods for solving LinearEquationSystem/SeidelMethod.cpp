#include <iostream>

#define constForSize 2 //for example

using namespace std;

int main()
{
    double arrayListForMatrix[constForSize][constForSize];
    double arrayListForVectorFreeCoefficients[constForSize];
    double arrayListForInitialValues[constForSize];
    double arrayListForVariables[constForSize];

    unsigned int variableForResultIteration = 0;


    for (unsigned variableForIterationI = 0; variableForIterationI < constForSize; variableForIterationI++)
    {
        for (unsigned variableForIterationJ = 0; variableForIterationJ < constForSize; variableForIterationJ++)
        {
            cout << "Input elements to matrix:[" << variableForIterationI << "][" << variableForIterationJ << "]:";

            cin >> arrayListForMatrix[variableForIterationI][variableForIterationJ];
        }
    }

    cout << endl;

    for (unsigned variableForIterationI = 0; variableForIterationI < constForSize; variableForIterationI++)
    {
        unsigned variableForIterationJ = 0;

        cout << "Input elements to vector free vector of coefficients:[" << variableForIterationI << "][" << variableForIterationJ << "]:";

        cin >> arrayListForVectorFreeCoefficients[variableForIterationI];
    }

    cout << endl;

    for (unsigned variableForIterationI = 0; variableForIterationI < constForSize; variableForIterationI++)
    {
        cout << "Input values x that were obtained from another method, If you do not have - Input: 0 to all of the x values: [" << variableForIterationI<<"]:";
        cin >> arrayListForInitialValues[variableForIterationI];
    }

    cout << endl;

    cout << "Input number of iterations:";
    cin >> variableForResultIteration;

    cout << endl;

    while (variableForResultIteration > 0)
    {
        for (unsigned variableForIterationI = 0; variableForIterationI < constForSize; variableForIterationI++)
        {
            arrayListForVariables[variableForIterationI] = (arrayListForVectorFreeCoefficients[variableForIterationI] / arrayListForMatrix[variableForIterationI][variableForIterationI]);

            for (unsigned variableForIterationJ = 0; variableForIterationJ < constForSize; variableForIterationJ++)
            {
                if (variableForIterationJ == variableForIterationI) continue;

                arrayListForVariables[variableForIterationI] = arrayListForVariables[variableForIterationI] -

                        ((arrayListForMatrix[variableForIterationI][variableForIterationJ] / arrayListForMatrix[variableForIterationI][variableForIterationI]) * arrayListForInitialValues[variableForIterationJ]);

                arrayListForInitialValues[variableForIterationI] = arrayListForVariables[variableForIterationI];
            }

            cout << "x" << variableForIterationI + 1 << " = " << arrayListForVariables[variableForIterationI] << endl;
        }

        cout << endl;

        variableForResultIteration--;
    }
    return 0;
}