# /// script
# dependencies = ["pandas", "matplotlib"]
# ///
import pandas as pd
import matplotlib.pyplot as plt

insertion_df = pd.read_csv("outputs/insertionsort_times.csv")
selection_df = pd.read_csv("outputs/selectionsort_times.csv")
search_df = pd.read_csv("outputs/binarysearch_times.csv")

# Plot 1: insertion sort vs selection sort
plt.figure()
insertion_df.plot(x="n", y="time_ms", marker="o", label="Insertion sort", ax=plt.gca())
selection_df.plot(x="n", y="time_ms", marker="o", label="Selection sort", ax=plt.gca())
plt.xlabel("n (array size)")
plt.ylabel("time (ms)")
plt.title("Insertion vs Selection sort")
plt.legend()
plt.savefig("outputs/sort_times_plot.png")

# Plot 2: binary search
plt.figure()
search_df.plot(x="n", y="time_ms", marker="o", color="green", label="Binary search", ax=plt.gca())
plt.xscale("log")
plt.xlabel("n (array size, log scale)")
plt.ylabel("time (ms)")
plt.title("Binary search")
plt.legend()
plt.savefig("outputs/search_times_plot.png")

print("Saved outputs/sort_times_plot.png and outputs/search_times_plot.png")
