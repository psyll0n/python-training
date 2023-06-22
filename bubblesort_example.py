#!/usr/bin/env python3
# bubblesort_example.py - Demonstrates the bubble sort algorithm.


# Bubble Sort algorithm
def bubbleSort(dataset):
    # TODO: Start with the array length and decrement each time.
    for i in range(len(dataset) - 1, 0, -1):
        for j in range(i):
            if dataset[j] > dataset[j + 1]:
                temp = dataset[j]
                dataset[j] = dataset[j + 1]
                dataset[j + 1] = temp
        print("Current state: ", dataset)


def main():
    list1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(list1)
    print("Result: ", list1)


if __name__ == "__main__":
    main()
