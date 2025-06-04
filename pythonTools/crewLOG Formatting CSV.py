##Prompts user for file to be formatted. It will then convert the phone numbers to the right format and add quotes around all of the data. It will then prompt for where to save the new file.
##Currently only for use on Silvertip
##CSV

import csv
from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pandas as pd

# Hide the main Tkinter window
Tk().withdraw()

# Prompt user to select a file to open
print("Please select the file to open.")
input_file_path = askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])

if input_file_path:
    # Load data from the selected file
    data = pd.read_csv(input_file_path)

    # Apply transformation to the last column
    # Format phone numbers in the last column as +1 (XXX) XXX-XXXX
    last_column = data.columns[-1]
    data[last_column] = data[last_column].apply(lambda x: f"+1 ({str(x)[1:4]}) {str(x)[4:7]}-{str(x)[7:]}" if pd.notnull(x) and len(str(x)) == 11 and str(x).isdigit() else x)

    # Prompt user to select a file to save the modified data
    print("Please select the file to save the modified data.")
    quoted_file_path = asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])

    if quoted_file_path:
        # Save the data to the selected file with all fields quoted
        data.to_csv(quoted_file_path, index=False, quoting=csv.QUOTE_ALL)
        print(f"Data saved to: {quoted_file_path}")
    else:
        print("No file selected for saving.")
else:
    print("No file selected for opening.")