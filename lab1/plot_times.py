# /// script
# dependencies = ["matplotlib"]
# ///
import csv
import matplotlib.pyplot as plt


def read_csv(path):
    ns = []
    times = []
    with open(path) as f:
        for row in csv.DictReader(f):
            ns.append(int(row["n"]))
            times.append(float(row["time_ms"]))
    return ns, times


insertion_n, insertion_ms = read_csv("outputs/insertionsort_times.csv")
selection_n, selection_ms = read_csv("outputs/selectionsort_times.csv")
search_n, search_ms = read_csv("outputs/binarysearch_times.csv")

# Plot 1: insertion sort vs selection sort
plt.figure()
plt.plot(insertion_n, insertion_ms, marker="o", label="Insertion sort")
plt.plot(selection_n, selection_ms, marker="o", label="Selection sort")
plt.xlabel("n (array size)")
plt.ylabel("time (ms)")
plt.title("Insertion vs Selection sort")
plt.legend()
plt.savefig("outputs/sort_times_plot.png")

# Plot 2: binary search
plt.figure()
plt.plot(search_n, search_ms, marker="o", color="green", label="Binary search")
plt.xscale("log")
plt.xlabel("n (array size, log scale)")
plt.ylabel("time (ms)")
plt.title("Binary search")
plt.legend()
plt.savefig("outputs/search_times_plot.png")

print("Saved outputs/sort_times_plot.png and outputs/search_times_plot.png")
