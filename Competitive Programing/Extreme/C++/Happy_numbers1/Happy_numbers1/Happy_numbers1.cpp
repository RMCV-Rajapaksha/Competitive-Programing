#include <iostream>
#include <vector>

using namespace std;

int h_number(int num) {
    int sum_digit = 0;
    while (num > 0) {
        int di = num % 10;
        sum_digit = (di * di) + sum_digit;
        num /= 10;
    }
    return sum_digit;
}

int final(int x) {
    while (x != 1 && x != 89) {
        x = h_number(x);
    }
    return (x == 1) ? 1 : 0;
}

int main() {
    int num_a, num_b;
    int s;
    cin >> num_a;
    cin >> num_b;

    s = num_b + 1 - num_a;
    vector<int> index(s);

    for (int p = 0; p< s; p++) {
        index[p] = num_a + p;
    }

    int step = 0;
    for (int q = 0; q < s; q++) {
        if (final(index[q]) == 1) {
            step++;
        }
    }
    cout << step << endl;
    return 0;
}