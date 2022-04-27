#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() {
    int n, c = 0;
    double x, y, function, area;
    scanf("%d", &n);
    srand(n);
    for (int i = 0; i < n; i++) {
          x = (double)rand() / RAND_MAX;
          y = (double)rand() / RAND_MAX;
          function = pow(x, 2);

          if (y <= function){
              c++;
          }
    }
    area = (double)c / n;
    printf("Area ~= %f\n", area);
    return 0;
}
