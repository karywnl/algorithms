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

void insertion_sort(vector<int>& arr){
	int n = arr.size();
	for (int i = 1; i < n; i++){
		int key = arr[i];
		int j = i - 1;
		while (j >= 0 && arr[j] > key){
			arr[j+1] = arr[j];
			j = j - 1;
		}
		arr[j+1] = key;
	}
}

int main(){

	srand(time(0));

	vector<int> sizes = {100, 1000, 5000, 10000};
	ofstream outfile("lab1/outputs/insertionsort_times.csv");
	outfile << "n,time_ms\n";

	for (int n : sizes){
		vector<int> arr = generate_random_array(n);

		auto start = chrono::high_resolution_clock::now();
		insertion_sort(arr);
		auto end = chrono::high_resolution_clock::now();

		double ms = chrono::duration<double, milli>(end - start).count();
		cout << "n=" << n << "  time=" << ms << "ms" << endl;
		outfile << n << "," << ms << "\n";
	}

	outfile.close();
	return 0;
}
