#include <iostream>
#include <cmath>



int main() {
    int list_k, n4;
    std::cin >> list_k >> n4;
    long long m = 998244353;

    int count[1 << list_k] = { 0 };

    for (int y = 0; y <= n4; ++y) {
        count[y % (1 << list_k)] = (count[y % (1 << list_k)] + std::llround(std::pow(n4, y))) % m;
    }

    long long answer[1 << list_k];
    for (int i = 0; i < (1 << list_k); ++i) {
        answer[i] = count[i] % m;
    }

    for (int i = 0; i < (1 << list_k); ++i) {
        std::cout << answer[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
