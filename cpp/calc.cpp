#include <iostream>
#include "mpreal.h"

using namespace mpfr;

mpfr::mpreal fact(int n) {
	return (n == 0 || n == 1) ? 1 : fact(n - 1) * n;
}

mpfr::mpreal calcit(int maxiter) {

	mpfr::mpreal s = mpfr::mpreal(0);

	for (int n = 0; n < maxiter; ++n) {
		s += mpfr::pow(-1, n) * fact(6 * n) * (13591409 + n * mpfr::mpreal(545140134)) /
             mpfr::pow(fact(n), 3) / fact(3 * n) /
             mpfr::pow(100100025 * 8 * mpfr::mpreal(327843840), n);
	}

	return 53360 * mpfr::pow(640320, mpfr::mpreal("0.5")) / s; 

}

int main(int argc, char *argv[]) {

	const int prec = 7;

	mpfr::mpreal::set_default_prec(50 * 50 * prec);
	std::cout.precision(50 * 75 * prec);

	std::cout << calcit(50 * prec) << std::endl << mpfr::mpreal::get_default_prec();

    return 0;
}
