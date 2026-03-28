import tkinter as tk
from tkinter import ttk

# Define the main application UI class
class ApplicationUI:
    # Initialize the class with the root window
    def __init__(self, root):
        # Set the root window reference
        self.root = root
        # Set the window title
        self.root.title("Application")
        # Set the window geometry (size)
        self.root.geometry("500x400")
        
        # Create the header label with title text
        header = ttk.Label(root, text="HELP HUB", font=("Times New Roman", 20, "bold"))
        # Pack the header with vertical padding
        header.pack(pady=20)
        
        # Create a frame for the county input section
        input_frame = ttk.Frame(root)
        # Pack the input frame with padding and fill horizontally
        input_frame.pack(pady=10, padx=20, fill="x")
        
        # Create and pack the label for county input
        ttk.Label(input_frame, text="County:").pack(side="left", padx=5)
        # Create the entry widget for county input
        self.name_entry = ttk.Entry(input_frame, width=30)
        # Pack the entry widget
        self.name_entry.pack(side="left", padx=5)

        # Create another frame for the salary range input section
        input_frame = ttk.Frame(root)
        # Pack the input frame with padding and fill horizontally
        input_frame.pack(pady=10, padx=20, fill="x")
        
        # Create and pack the label for salary range input
        ttk.Label(input_frame, text="Salary Range:").pack(side="left", padx=5)
        # Define the list of salary ranges for the dropdown
        salary_ranges = [
            "Under $25,000",
            "$25,000 - $49,999",
            "$50,000 - $74,999",
            "$75,000 - $99,999",
            "$100,000 and above"
        ]
        # Create the combobox widget for salary range selection
        self.salary_combo = ttk.Combobox(input_frame, values=salary_ranges, state="readonly", width=27)
        # Pack the combobox widget
        self.salary_combo.pack(side="left", padx=5)
        
        # Create a frame for the buttons
        button_frame = ttk.Frame(root)
        # Pack the button frame with vertical padding
        button_frame.pack(pady=20)
        
        # Create and pack the search button
        ttk.Button(button_frame, text="Search",
                  command=self.on_submit).pack(side="left", padx=5)
        # Create and pack the clear button
        ttk.Button(button_frame, text="Clear", 
                  command=self.on_clear).pack(side="left", padx=5)
        
        # Create checklist section
        checklist_frame = ttk.Frame(root)
        # Pack the checklist frame with padding and fill horizontally
        checklist_frame.pack(pady=20, padx=20, fill="x")
        
        # Header for checklist
        ttk.Label(checklist_frame, text="Resources Needed", font=("Times New Roman", 16, "bold")).pack(pady=10)
        
        # Create checkbutton variables and widgets
        self.check_vars = []
        options = ["Housing", "Employment", "Health", "Food"]
        for option in options:
            var = tk.BooleanVar()
            self.check_vars.append(var)
            ttk.Checkbutton(checklist_frame, text=option, variable=var).pack(anchor="w", padx=20)
    
    # Define the method to handle submit button click
    def on_submit(self):
        # Get the text from the county entry
        name = self.name_entry.get()
        # Get the selected value from the salary combobox
        salary = self.salary_combo.get()
    
    # Define the method to handle clear button click
    def on_clear(self):
        # Clear the county entry field
        self.name_entry.delete(0, "end")
        # Clear the salary combobox selection
        self.salary_combo.set('')
        # Reset all checklist options
        for var in self.check_vars:
            var.set(False)

# Check if this script is being run as the main module
if __name__ == "__main__":
    # Create the main Tkinter root window
    root = tk.Tk()
    # Instantiate the ApplicationUI class with the root window
    app = ApplicationUI(root)
    # Start the Tkinter main event loop
    root.mainloop()