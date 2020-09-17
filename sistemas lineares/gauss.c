#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void solveGauss(int n, double A[n][n], double b[n], double X[n]) {
    int i, j, k, l, m, oi=1;
    //ETAPA DE ESCALONAMENTO
    for (k = 0; k < n - 1; k++) {

            //realiza o escalonamento
            for (m = k + 1; m < n; m++) {
                
                double F = -A[m][k] / A[k][k];
                A[m][k] = 0; //evita uma iteraÃ§Ã£o
                b[m] = b[m] + F * b[k];
                printf("    Interação %d - Razão de %f\n",oi,F);
                oi++;
                for (l = k + 1; l < n; l++) {
                    A[m][l] = A[m][l] + F * A[k][l];
                   // printf("    Interação - Somando Elemento %f com %f * %f\n",A[m][l], F,A[k][l]);
                }
                
                for(int u=0; u<3; u++){
                    printf("    ");
                    for(int y = 0; y<3; y++){
                        printf("%f ",A[u][y]);
                        
                    }
                    if (u == m)
                        printf("Linha %d = Linha %d + (%f * Linha %d)", m+1, m+1, F, k+1);
                    printf("\n");
                }
                printf("\n");
            }
        
    }
    //ETAPA DE RESOLUÃ‡ÃƒO DO SISTEMA
    printf ("   Resolução do X\n");
    for (i = n - 1; i >= 0; i--) {
        X[i] = b[i];
        for (j = i + 1; j < n; j++) {
            X[i] = X[i] - X[j] * A[i][j];
           
        }
        printf("        X[%d] = X[%d] / A[%d][%d]\n",i+1,i+1,i+1,i+1);
        X[i] = X[i] / A[i][i];
        printf("        X[%d] = %f\n", i+1, X[i]);
        printf("\n");
    }
    
}
//CÃ³digo de testes
int main(){
    int n = 3;
    double A[3][3] = {{4,1,1},
                    {2,5,2},
                    {1,2,4}};
                    
    double b[3] = {6, 3, 11}; 
    double x[3];
    solveGauss(n, A, b, x);
    
    printf("Solução: x1 = %f, x2 = %f, x3 = %f\n\n\n", x[0], x[1], x[2]);

    double B[3][3] = {{3,2,1},
                    {2,7,2},
                    {1,3,5}};
    double c[3] = {2, -3, 3};

    solveGauss(n, B, c, x);
    
    printf("Solução: x1 = %f, x2 = %f, x3 = %f\n\n\n", x[0], x[1], x[2]);

    double C[3][3] = {{1,1,-3},
                    {0,-2,1},
                    {-4,1,-1}};
                    
    double d[3] = {5, -3,-2}; 
        
    solveGauss(n, C, d, x);

    printf("Solução: x1 = %f, x2 = %f, x3 = %f\n\n\n", x[0], x[1], x[2]);


    double D[3][3] = {{3,1,1},
                    {1,-4,2},
                    {1,-3,5}};      
    double e[3] = {1, 3,-1}; 
    
    solveGauss(n, D, e, x);
    printf("Solução: x1 = %f, x2 = %f, x3 = %f\n\n\n", x[0], x[1], x[2]);
    
    
    
    return 0;
}
