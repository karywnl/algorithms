#include <iostream>
using namespace std;

void selection_sort(int arr[], int n){

	for (int i=0; i<n-1; i++){
		int min_idx = i;

		for (int j=i+1; j<n; j++){
			if (arr[j] < arr[min_idx]){
				min_idx = j;
			}
		}
		swap(arr[i], arr[min_idx]);
	}
}

void print_arr(int arr[], int n){
	for (int i=0; i<n; i++){
		cout << arr[i] << " ";
	}
	cout << endl;
}

int main(){

	int arr[] = {64, 25, 12, 22, 11};
	int n = sizeof(arr)/sizeof(arr[0]);

	selection_sort(arr, n);
	print_arr(arr, n);

	return 0;
}
