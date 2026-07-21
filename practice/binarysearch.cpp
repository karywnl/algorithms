#include <iostream>
using namespace std;

int binary_search(int arr[], int target, int n){

	int low_idx = 0;
	int high_idx = n - 1;

	while (low_idx <= high_idx){

		int mid_idx = low_idx + (high_idx - low_idx) / 2;

		if (arr[mid_idx] == target){
			return mid_idx;
		}

		else if (target < arr[mid_idx]){
			high_idx = mid_idx - 1;
		}

		else{
			low_idx = mid_idx + 1;
		}
		
	}

	return -1;
}


int main(){

	int arr[] = { 2, 3, 4, 10, 40 };
	int target = 10;

	int n =	sizeof(arr)/sizeof(arr[0]);

	int res = binary_search(arr, target, n);

	if (res != -1){
		cout << "Target found at " << res << endl;
	}

	else{
		cout << "Target not found" << endl;
	}
	
}
