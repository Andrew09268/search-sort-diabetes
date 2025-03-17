# Search & Sort Algorithm Implementation (Diabetes Dataset)

## Description
This project demonstrates the implementation of various search and sorting algorithms on a diabetes dataset. It allows users to search for specific values within selected columns using linear or binary search and sort data using different sorting algorithms such as Bubble Sort, Selection Sort, Insertion Sort, and Quick Sort.

## Installation
Ensure you have Python installed on your system. Then, install the required dependencies using:
```sh
pip install pandas
```

## Usage
1. Place the `diabetes.csv` file in the same directory as the script.
2. Run the script using:
```sh
python script.py
```
3. Follow the on-screen prompts to:
   - Choose a column to search.
   - Enter a value to search for.
   - Select a search algorithm (Linear Search or Binary Search).
   - Choose a column to sort.
   - Select a sorting algorithm.
4. The sorted data is saved as `sorted-diabetes.csv`.

## Sample Output
```
Choose a column to search (Glucose, Age, BMI, etc.): Glucose
Enter a value to search for: 120

Choose search method:
1. Linear Search
2. Binary Search
Enter choice: 2
Sorting "Glucose" column before Binary Search...
Binary Search: Found at row index 15
Time taken: 0.00321s

Choose a column to sort (Glucose, Age, BMI, etc.): Age

Choose sorting algorithm:
1. Bubble Sort
2. Selection Sort
3. Insertion Sort
4. Quick Sort
Enter choice: 4
Sorting by "Age" using chosen method...
Sorting completed.
Sorted data saved as "sorted-diabetes.csv".
Time taken: 0.00567s
```

## License
This project is for educational purposes.

