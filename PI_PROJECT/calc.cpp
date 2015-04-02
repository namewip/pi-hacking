#include <iostream>
#include "mpreal.h"

using namespace mpfr;
using namespace std;

mpreal fact(int n) {
	return (n == 0 || n == 1) ? 1 : fact(n - 1) * n;
}

mpreal calcit(int maxiter) {

	mpreal s = mpreal(0);

	for (int n = 0; n < maxiter; ++n) {
		s = s + pow(-1, n) * fact(6 * n) * (13591409 + n * mpreal(545140134)) / pow(fact(n), 3) / fact(3 * n) / pow(100100025 * 8 * mpreal(327843840), n);
	}

	return 53360 * pow(640320, mpreal("0.5")) / s; 

}

int main(int argc, char *argv[]) {

	const int prec = 100;

	mpreal::set_default_prec(50 * 50 * prec);
	cout.precision(50 * 75 * prec);

	cout << calcit(50 * prec) << endl << mpreal::get_default_prec();

    return 0;
}
