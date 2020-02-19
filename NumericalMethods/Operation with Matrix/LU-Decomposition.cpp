#include <iostream>
#include <iomanip>

#define matrixInputOutputSize 2 //for example

using namespace std;



void LU_DecompositionProcedure(double arrayListForEnterMatrix[matrixInputOutputSize][matrixInputOutputSize],

        double firstHandMatrixL[matrixInputOutputSize][matrixInputOutputSize], double secondHandMatrixU[matrixInputOutputSize][matrixInputOutputSize])
{


    for(unsigned variableForIterationI = 0; variableForIterationI < matrixInputOutputSize; variableForIterationI++)
    {
        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixInputOutputSize; variableForIterationJ++)
        {
            if (variableForIterationJ < variableForIterationI)
            {
                firstHandMatrixL[variableForIterationJ][variableForIterationI] = 0;
            }

            else
                {
                    firstHandMatrixL[variableForIterationJ][variableForIterationI] = arrayListForEnterMatrix[variableForIterationJ][variableForIterationI];

                for(unsigned variableForIterationK = 0; variableForIterationK < variableForIterationI; variableForIterationK++)
                {
                    firstHandMatrixL[variableForIterationJ][variableForIterationI] = firstHandMatrixL[variableForIterationJ][variableForIterationI] -

                            firstHandMatrixL[variableForIterationJ][variableForIterationK] * secondHandMatrixU[variableForIterationK][variableForIterationI];
                }
            }
        }

        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixInputOutputSize; variableForIterationJ++)
        {
            if (variableForIterationJ < variableForIterationI)
            {
                secondHandMatrixU[variableForIterationI][variableForIterationJ] = 0;
            }
            else if (variableForIterationJ == variableForIterationI)
            {
                secondHandMatrixU[variableForIterationI][variableForIterationJ] = 1;
            }

            else
                {

                secondHandMatrixU[variableForIterationI][variableForIterationJ] = arrayListForEnterMatrix[variableForIterationI][variableForIterationJ] / firstHandMatrixL[variableForIterationI][variableForIterationI];

                for(unsigned variableForIterationK = 0; variableForIterationK < variableForIterationI; variableForIterationK++)
                {
                    secondHandMatrixU[variableForIterationI][variableForIterationJ] = secondHandMatrixU[variableForIterationI][variableForIterationJ]

                            - ((firstHandMatrixL[variableForIterationI][variableForIterationK] * secondHandMatrixU[variableForIterationK][variableForIterationJ]) / firstHandMatrixL[variableForIterationI][variableForIterationI]);
                }
            }
        }
    }
}

int main()
{
    double arrayListForEnterMatrix[matrixInputOutputSize][matrixInputOutputSize];

    double firstHandMatrixL[matrixInputOutputSize][matrixInputOutputSize];

    double secondHandMatrixU[matrixInputOutputSize][matrixInputOutputSize];


    for(unsigned variableForIterationI = 0; variableForIterationI < matrixInputOutputSize; variableForIterationI++)
    {
        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixInputOutputSize; variableForIterationJ++)
        {
           cerr << "Input element to matrix:[" << variableForIterationI << "][" << variableForIterationJ << "] :";

            cin >> arrayListForEnterMatrix[variableForIterationI][variableForIterationJ];
        }
    }

    cout << endl;

    cout << "Input Matrix:" << endl;

    cout << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixInputOutputSize; variableForIterationI++)
    {
        for (unsigned variableForIterationJ = 0; variableForIterationJ < matrixInputOutputSize; variableForIterationJ++)
        {
            cout << setw(5) << arrayListForEnterMatrix[variableForIterationI][variableForIterationJ] << setw(5);
        }
        cout << endl;
    }

    LU_DecompositionProcedure(arrayListForEnterMatrix, firstHandMatrixL, secondHandMatrixU);

    cout << endl;

    cout << "First Hand Matrix (L Decomposition) equals:" << endl;

    cout << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixInputOutputSize; variableForIterationI++)
    {
        for(unsigned variableForIterationJ = 0; variableForIterationJ < matrixInputOutputSize; variableForIterationJ++)
        {
            cout << setw(5) << firstHandMatrixL[variableForIterationI][variableForIterationJ] << setw(5);
        }
        cout << endl;
    }

    cout << endl;

    cout << "Second Hand Matrix (U Decomposition) equals:" << endl;

    cout << endl;

    for(unsigned variableForIterationI = 0; variableForIterationI < matrixInputOutputSize; variableForIterationI++)
    {
        for (unsigned variableForIterationJ = 0; variableForIterationJ < matrixInputOutputSize; variableForIterationJ++)
        {
            cout << setw(5) << secondHandMatrixU[variableForIterationI][variableForIterationJ] << setw(5);
        }
        cout << endl;
    }

    return 0;
}
