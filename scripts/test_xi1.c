#include <stdio.h>
#include <math.h>
int main() {
    double a = 1e-4;
    double loga = log(a);
    double activation = 0.5 * (1.0 + tanh(loga + 9.21034037198));
    printf("activation: %e\n", activation);
    return 0;
}
