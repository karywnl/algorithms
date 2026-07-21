#include <iostream>
#include <vector>
using namespace std;

int main(){
    vector<int> nums = {12, 4, 7, 9, 2};
    nums.push_back(20);

    for (int i=0; i<nums.size(); i++){
        cout << nums[i] << " ";
    }
    cout << endl;
    cout << "size: " << nums.size() << endl;

    return 0;
}
