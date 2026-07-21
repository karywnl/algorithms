#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <cstdlib>
#include <ctime>
using namespace std;

vector<int> generate_sorted_array(int n){
	vector<int> arr(n);
	for (int i = 0; i < n; i++){
		arr[i] = i;
	}
	return arr;
}

int binary_search(vector<int>& arr, int target){
	int low_idx = 0;
	int high_idx = arr.size() - 1;

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

	srand(time(0));

	vector<int> sizes = {1000, 10000, 100000, 1000000};
	ofstream outfile("lab1/outputs/binarysearch_times.csv");
	outfile << "n,time_ms\n";

	for (int n : sizes){
		vector<int> arr = generate_sorted_array(n);
		int target = arr[rand() % arr.size()];

		auto start = chrono::high_resolution_clock::now();
		int res = binary_search(arr, target);
		auto end = chrono::high_resolution_clock::now();

		bool found = (res != -1);
		double ms = chrono::duration<double, milli>(end - start).count();
		cout << "n=" << n << "  found=" << found << "  time=" << ms << "ms" << endl;
		outfile << n << "," << ms << "\n";
	}

	outfile.close();
	return 0;
}
