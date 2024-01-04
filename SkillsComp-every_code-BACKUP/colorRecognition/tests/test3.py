import tkinter as tk
from tkinter import filedialog
def save_file():
    # Prompt the user to enter a file name
    file_name = filedialog.asksaveasfilename(defaultextension=".txt")
    print(file_name)

    # Create a file path for the text file
    file_path = file_name

    # Open the file in write mode and write "hello world" to it
    with open(file_path, "w") as file:
        file.write("hello world")

root = tk.Tk()

# Create a button that calls the save_file function when clicked
button = tk.Button(root, text="Choose Directory", command=save_file)
button.pack()

# Run the tkinter app
root.mainloop()
