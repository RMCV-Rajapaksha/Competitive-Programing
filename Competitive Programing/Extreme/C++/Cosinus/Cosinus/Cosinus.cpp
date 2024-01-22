#include<iostream>

using namespace std;

int main() {
    int t = 0;
    cin >> t;

    int* a = new int[4];
    int* bValues = new int[4];

    for (int i = 0; i < t; i++) {
        cin >> a[i];
    }

    for (int j = 0; j < t; j++) {
        int b = 0;
        int c = 1;

        while (c != 0) {
            b++;
            if ((a[j] * b) % 90 != 0) {
                c = a[j] * b % 90;
            }
            else {
                c = 0;
                break;
            }
        }
        bValues[j] = b;
        t--;
        j++;

    }

    for (int i = 0; i < t; i++) {
        cout << bValues[i] << " ";
    }
}