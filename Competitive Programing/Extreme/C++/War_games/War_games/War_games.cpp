#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int card_values[14] = { 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 };


string champion(vector<int>& man1, vector<int>& man2) {
    int current_index = 0;

    while (!man1.empty() && !man2.empty()) {

        int player1_card = man1[current_index];
        int player2_card = man2[current_index];

        if (player1_card < player2_card) {
           
            man2.push_back(player1_card);
            man2.push_back(player2_card);
            man1.erase(man1.begin() + current_index);
            man2.erase(man2.begin() + current_index);

        }
        else if (player1_card > player2_card) {
            
            man1.push_back(player2_card);
            man1.push_back(player1_card);
            man2.erase(man2.begin() + current_index);
            man1.erase(man1.begin() + current_index);

        }
        else if (player1_card == player2_card) {
           
            man1.push_back(player1_card);
            man2.push_back(player2_card);
            man1.erase(man1.begin() + current_index);
            man2.erase(man2.begin() + current_index);

        }
    }

    if (man1.empty()) {
        return "player 2";

    }
    else if (man2.empty()) {
      
        return "player 1";

    }
    else {
       
        return "draw";

    }
}

int main() {
    int n;
    cin >> n;

 
    for (int i = 0; i < n; i++) {

        vector<int> man1, man2;

        
        for (int j = 0; j < 52; j++) {
            int card;
            cin >> card;
            man1.push_back(card_values[card - 1]);
        }

        for (int j = 0; j < 52; j++) {
            int card;
            cin >> card;
            man2.push_back(card_values[card - 1]);
        }

        string champion1 = champion(man1, man2);

      
        cout << champion1 << endl;

    }

    return 0;
}