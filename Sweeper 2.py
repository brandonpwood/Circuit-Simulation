import numpy as np
import csv
import sys

n = 4 # Number of data fields

# Find files
filenames = sys.argv
filenames = filenames[1:]
print(filenames)

# Data cleaning function
def sweep(file_name, n):
    # Open file
    with open(file_name + ".txt" , 'r') as f:
        data = f.read()
        # Separate into lines
        lines = data.split('\n')
    # Split into seperate data columns
    fields = []
    for line in lines:
        fields.append(line.split('	'))
    # Strip Unimportant values
    newData = []
    for field in fields:
        if len(field) == n:
            newData.append(field)
    titles = newData[0]
    newData = newData[1:]

    # Convert data to floats
    print("Data parsed, converting to floats.")
    x = np.array(newData)
    y = x.astype(np.float)
    print("Data converted, saving to .csv")
    # y2 = []
    # for i in y:
    #     y2.append(list(i))
    # y = y2

    # Save as .csv file
    with open(file_name + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(titles)
        for i in y:
            writer.writerow(i)
    print("Data conversion complete.")

# Clean data
for filename in filenames:
    sweep(filename, n)
