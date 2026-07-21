#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include <cstdlib>
#include <ctime>
using namespace std;

vector<int> generate_random_array(int n){
	vector<int> arr(n);
	for (int i = 0; i < n; i++){
		arr[i] = rand() % 1000;
	}
	return arr;
}

void selection_sort(vector<int>& arr){
	int n = arr.size();
	for (int i = 0; i < n - 1; i++){
		int min_idx = i;
		for (int j = i + 1; j < n; j++){
			if (arr[j] < arr[min_idx]){
				min_idx = j;
			}
		}
		swap(arr[i], arr[min_idx]);
	}
}

int main(){

	srand(time(0));

	vector<int> sizes = {100, 1000, 5000, 10000};
	ofstream outfile("lab1/outputs/selectionsort_times.csv");
	outfile << "n,time_ms\n";

	for (int n : sizes){
		vector<int> arr = generate_random_array(n);

		auto start = chrono::high_resolution_clock::now();
		selection_sort(arr);
		auto end = chrono::high_resolution_clock::now();

		double ms = chrono::duration<double, milli>(end - start).count();
		cout << "n=" << n << "  time=" << ms << "ms" << endl;
		outfile << n << "," << ms << "\n";
	}

	outfile.close();
	return 0;
}
