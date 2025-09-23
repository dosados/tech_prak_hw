#include <iostream>
#include <string>
using namespace std;

string decrypt_caesar(int k, const string &text) {
    string result;
    for (char ch : text) {
        if (ch >= 'a' && ch <= 'z') {
            result += char((ch - 'a' - k + 26) % 26 + 'a');  
        } else if (ch >= 'A' && ch <= 'Z') {
            result += char((ch - 'A' - k + 26) % 26 + 'A'); 
        } else {
            result += ch;
        }
    }
    return result;
}

int main() {
    int k;
    string encrypted;

    cin >> k;
    cin.ignore();
    getline(cin, encrypted);

    cout << decrypt_caesar(k, encrypted) << endl;

    return 0;
}