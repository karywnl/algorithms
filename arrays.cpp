#include <iostream>
using namespace std;

int main(){
    int arr[6] = {12, 4, 7, 9, 2, 15};
    int sum = 0;
    for (int i=0; i<6; i++){
        cout << arr[i] << endl;
        sum += arr[i];
    }
    cout << sum << endl;
    return 0;
}