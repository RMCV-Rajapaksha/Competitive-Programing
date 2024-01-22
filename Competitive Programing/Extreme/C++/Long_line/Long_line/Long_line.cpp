#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<int> s(5);

    for (int i = 0; i < 5; i++) {
        cin >> s[i];
    }

    int num = s[0];
    int height = s[1];
    int aisec = s[2];
    int cest = s[3];
    int q12 = s[4];

    vector<int> data_var;
    data_var.push_back(height);

    for (int i = 1; i < num; i++) {
        int number1 = (aisec * data_var[i - 1] + cest);
        int number = number1 % q12;
        data_var.push_back(number);
    }

    int count_number = 0;

    for (int y = 1; y < num; y++) {
        int max_height = 0;
        for (int zz = y - 1; zz >= 0; zz--) {
            if (data_var[zz] > max_height) {
                max_height = data_var[zz];
                count_number++;
            }
        }
    }

    cout << count_number << endl;

    return 0;
}
