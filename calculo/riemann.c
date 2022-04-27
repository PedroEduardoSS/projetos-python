#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int n;

    scanf("%d", &n);

    double x = 0, y, soma = 0;
    double  lr = (double)1 / n, ar;
    
    //somas de Riemann
    for (int i = 0; i < n; i++) {
        y = (double)pow(x, 2);
        ar = lr * y;
        soma += ar;
        x += lr;
    }
    
    printf("Area ~= %.3lf\n", soma);
    return 0;
}
