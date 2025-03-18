import pandas as pd
import time

def load_data():
    return pd.read_csv('diabetes.csv')

def linear_search(data, column, value):
    values = data[column].values
    for index, val in enumerate(values):
        if val == value:
            return index
    return -1

def binary_search(data, column, value):
    values = data[column].values
    left, right = 0, len(values) - 1
    while left <= right:
        mid = (left + right) // 2
        if values[mid] == value:
            while mid > 0 and values[mid - 1] == value:
                mid -= 1
            return mid
        elif values[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def bubble_sort(data, column):
    sorted_data = data.copy()
    values = sorted_data[column].values
    n = len(values)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True
        if not swapped:
            break
    sorted_data[column] = values
    return sorted_data

def selection_sort(data, column):
    sorted_data = data.copy()
    values = sorted_data[column].values
    n = len(values)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if values[j] < values[min_idx]:
                min_idx = j
        values[i], values[min_idx] = values[min_idx], values[i]
    sorted_data[column] = values
    return sorted_data

def insertion_sort(data, column):
    sorted_data = data.copy()
    values = sorted_data[column].values
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and values[j] > key:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = key
    sorted_data[column] = values
    return sorted_data

def quick_sort(data, column):
    if len(data) <= 1:
        return data
    pivot = data[column].iloc[len(data) // 2]
    left = data[data[column] < pivot]
    middle = data[data[column] == pivot]
    right = data[data[column] > pivot]
    return pd.concat([quick_sort(left, column), middle, quick_sort(right, column)])

def get_valid_column(data, user_input):
    user_input = user_input.strip().lower()
    column_mapping = {col.lower(): col for col in data.columns}
    return column_mapping.get(user_input, None)

def main():
    data = load_data()

    column = get_valid_column(data, input("Choose a column to search (Glucose, Age, BMI, etc.): "))
    if column is None:
        print("Invalid column name. Please check spelling and capitalization.")
        return

    value = float(input("Enter a value to search for: "))

    print("\nChoose search method:\n1. Linear Search\n2. Binary Search")
    search_choice = int(input("Enter choice: "))

    start_time = time.time()
    if search_choice == 2:
        print(f"Sorting \"{column}\" column before Binary Search...")
        data = quick_sort(data, column)

    index = linear_search(data, column, value) if search_choice == 1 else binary_search(data, column, value)
    end_time = time.time()

    if index != -1:
        print(f"Found at row index {index}")
    else:
        print("Value not found.")
    print(f"Time taken: {end_time - start_time:.5f}s\n")

    column = get_valid_column(data, input("Choose a column to sort (Glucose, Age, BMI, etc.): "))
    if column is None:
        print("Invalid column name. Please check spelling and capitalization.")
        return

    print("\nChoose sorting algorithm:\n1. Bubble Sort\n2. Selection Sort\n3. Insertion Sort\n4. Quick Sort")
    sort_choice = int(input("Enter choice: "))

    start_time = time.time()
    sorting_algorithms = {1: bubble_sort, 2: selection_sort, 3: insertion_sort, 4: quick_sort}
    sorted_data = sorting_algorithms[sort_choice](data, column)
    sorted_data.to_csv("sorted-diabetes.csv", index=False)
    end_time = time.time()

    print(f"Sorting by \"{column}\" using chosen method...")
    print("Sorting completed.")
    print("Sorted data saved as \"sorted-diabetes.csv\".")
    print(f"Time taken: {end_time - start_time:.5f}s")

if __name__ == "__main__":
    main()
