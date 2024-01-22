#include <iostream>
#include <unordered_set>

using namespace std;

bool isHappy(int n) {
    unordered_set<int> seen;
    while (n != 1 && seen.find(n) == seen.end()) {
        seen.insert(n);
        int next_n = 0;
        while (n > 0) {
            int digit = n % 10;
            next_n += digit * digit;
            n /= 10;
        }
        n = next_n;
    }
    return n == 1;
}

int countHappyNumbers(int a, int b) {
    int count = 0;
    for (int n = a; n <= b; n++) {
        if (isHappy(n)) {
            count++;
        }
    }
    return count;
}

int main() {
    int a, b;
    cin >> a >> b;
    cout << countHappyNumbers(a, b) << endl;
    return 0;
}
