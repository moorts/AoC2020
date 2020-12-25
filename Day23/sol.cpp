#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> data = {4, 6, 7, 5, 2, 8, 1, 9, 3};
    long long unsigned int size = pow(10, 6);
    cout << "hello, world" << endl;
    vector<int> cups(size+1);
    for(int i = 0; i < data.size(); i++) {
        cups[data[i]] = data[(i+1) % data.size()];
    }
    cups[3] = 10;
    //cups[3] = 4;
    for(int i = 10; i < size; i++) {
        cups[i] = i+1;
    }
    cups[size] = 4;
    cout << cups[1000000] << endl;
    // Step
    int current = data[0];
    for(int i = 0; i < pow(10, 7); i++) {
        int next = cups[current];
        cups[current] = cups[cups[cups[next]]];
        set<int> pvals = {next, cups[next], cups[cups[next]], current};
        int dest = current > 1 ? current - 1 : size;
        while(pvals.find(dest) != pvals.end()) {
            dest = dest > 1 ? dest - 1 : size;
        }
        //cout << dest << endl;
        current = cups[current];
        // Inserting at dest
        int temp = cups[dest];
        //cout << temp << endl;
        cups[dest] = next;
        cups[cups[cups[next]]] = temp;
    }
    cout << cups[cups[1]] << endl;
    long long product = (long long) (cups[1]) * (long long) (cups[cups[1]]);
    cout << product << endl;
    return 0;
}
