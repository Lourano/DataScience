#include<iostream>
#include <iomanip>
#define matrixSize 2 //for example
using namespace std;

int main()
{

    double ArrayForMatrix[matrixSize][matrixSize];

    double variableForDeterminantOfMatrix = 0;

    cout << "Enter elements of matrix row wise:" << endl;

    cout << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixSize; variableForIterationI++)
    {
        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixSize; variableForIterationJ++)
        {
            cout << "Input element to matrix:[" << variableForIterationI << "][" << variableForIterationJ << "] :";

            cin >> ArrayForMatrix[variableForIterationI][variableForIterationJ];
        }
    }

    cout << "Your Matrix:" << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixSize; variableForIterationI++)
    {
        cout << setw(5) << endl;

        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixSize; variableForIterationJ++)
        {
            cout << ArrayForMatrix[variableForIterationI][variableForIterationJ]  << "\t";
        }

    }

    cout << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixSize; variableForIterationI++)
    {
        variableForDeterminantOfMatrix = variableForDeterminantOfMatrix + (ArrayForMatrix[0][variableForIterationI] * (ArrayForMatrix[1][(variableForIterationI+1) % matrixSize] * ArrayForMatrix[2][(variableForIterationI + 2) % matrixSize]

                - ArrayForMatrix[1][(variableForIterationI + 2) % matrixSize] * ArrayForMatrix[2][(variableForIterationI + 1) % matrixSize]));
    }

    cout << "\nDeterminant: " << variableForDeterminantOfMatrix << endl;

    cout<<"\nInverse of matrix is:" << endl;

    cout << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixSize; variableForIterationI++)
    {
        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixSize; variableForIterationJ++)
        {
            cout << setw(15) << ((ArrayForMatrix[(variableForIterationJ+1) % matrixSize][(variableForIterationI+1) % matrixSize] * ArrayForMatrix[(variableForIterationJ + 2) % matrixSize][(variableForIterationI + 2) % matrixSize])

                     - (ArrayForMatrix[(variableForIterationJ + 1) % matrixSize][(variableForIterationI + 2) % matrixSize] * ArrayForMatrix[(variableForIterationJ + 2) % matrixSize][(variableForIterationI + 1) % matrixSize])) / variableForDeterminantOfMatrix << "\t";
        }

        cout << endl;
    }

    return 0;
}
