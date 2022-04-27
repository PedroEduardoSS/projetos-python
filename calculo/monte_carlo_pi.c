#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    int n, c = 0;
    double x, y, m, pi;

    scanf("%d", &n);

    srand(n);
    for (int i = 0; i < n; i++) {
          x = (double)rand() / RAND_MAX;
          y = (double)rand() / RAND_MAX;
          m = pow((x - 0.50), 2) + pow((y - 0.50), 2);
          if (m <= 0.25){
              c++;
          }

    }

    pi = 4 * (double)c / n;
    printf("pi ~= %lf\n",pi);
    return 0;
}
