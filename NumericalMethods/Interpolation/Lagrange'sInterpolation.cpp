#include <iostream>

using namespace std;


struct StructureOfDataSetOfPoints
{
    double pointX, pointY;
};

double functionForInterpolation(StructureOfDataSetOfPoints dataFrame[], int variableForYDescribedByX, int variableForQuantityOfPoints)
{
    double variableForResult = 0; 

    for (unsigned variableForIterationI = 0; variableForIterationI < variableForQuantityOfPoints; variableForIterationI++)
    {
        double variableForVectorOfPointsY = dataFrame[variableForIterationI].pointY;

        for (unsigned variableForIterationJ = 0; variableForIterationJ < variableForQuantityOfPoints; variableForIterationJ++)
        {
            if(variableForIterationJ != variableForIterationI)
            {
                variableForVectorOfPointsY = variableForVectorOfPointsY * (variableForYDescribedByX - dataFrame[variableForIterationJ].pointX) / double (dataFrame[variableForIterationI].pointX - dataFrame[variableForIterationJ].pointX);
            }
        }
        variableForResult += variableForVectorOfPointsY;
    }
    return variableForResult;
}

int main()
{

    StructureOfDataSetOfPoints dataFrame[] = {{13.1072, 13.1072}, {4.1472, 5.1472}, {0.8192, 2.8192}, {0.0512, 3.0512},                            ////FOR EXAMPLE!!!
                                                                                                                                                  ////FOR EXAMPLE!!!
                                              {0, 4}, {0.0512, 5.0512}, {0.8192, 6.8192}, {4.1472, 11.1472}, {13.1972, 21.1972}, {32, 41}};      ////FOR EXAMPLE!!!

    cout << "\nValue of Lagrange's Interpolation is: " << functionForInterpolation(dataFrame, 9, 4) << endl;

    return 0;
}
