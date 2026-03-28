import tkinter as tk
from tkinter import ttk
import csv
import os
import tkinter.messagebox as messagebox

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
        
        # Load the dataset
        self.load_data()
        
        # Define keywords for resource matching
        self.resource_keywords = {
            "Housing": ["housing", "shelter", "residential"],
            "Employment": ["employment", "vocational", "rehabilitation"],
            "Health": ["health", "medical", "care", "hospital", "physician", "dentist", "nursing"],
            "Food": ["food", "nutrition", "relief", "emergency"]
        }
        header = ttk.Label(root, text="HELP HUB", font=("Times New Roman", 20, "bold"))
        # Pack the header with vertical padding
        header.pack(pady=20)
        
        # Add goal description
        description = ttk.Label(root, text="Helping low-income families locate essential resources", font=("Times New Roman", 11))
        # Pack the description with padding
        description.pack(pady=10)
        
        # Create a frame for the county input section
        input_frame = ttk.Frame(root)
        # Pack the input frame with padding and fill horizontally
        input_frame.pack(pady=10, padx=20, fill="x")
        
        # Create and pack the label for county input
        ttk.Label(input_frame, text="County:").pack(side="left", padx=5)
        # Create the combobox widget for county selection
        self.county_combo = ttk.Combobox(input_frame, values=self.counties, state="readonly", width=27)
        # Pack the combobox widget
        self.county_combo.pack(side="left", padx=5)

        
        # Create checklist section
        checklist_frame = ttk.Frame(root)
        # Pack the checklist frame with padding and fill horizontally
        checklist_frame.pack(pady=20, padx=20, fill="x")
        
        # Header for checklist
        ttk.Label(checklist_frame, text="Resources Needed", font=("Times New Roman", 16)).pack(pady=10)
        
        # Create checkbutton variables and widgets
        self.check_vars = []
        self.options = ["Housing", "Employment", "Health", "Food"]
        for option in self.options:
            var = tk.BooleanVar()
            self.check_vars.append(var)
            ttk.Checkbutton(checklist_frame, text=option, variable=var, command=self.update_buttons).pack(anchor="w", padx=20)

        # Create a frame for the buttons (initially hidden)
        self.button_frame = ttk.Frame(root)
        # Do not pack initially
        


        # Create and pack the search button
        ttk.Button(self.button_frame, text="Search",
                  command=self.on_submit).pack(side="left", padx=5)
        # Create and pack the clear button
        ttk.Button(self.button_frame, text="Clear", 
                  command=self.on_clear).pack(side="left", padx=5)
    
    # Define the method to load data from CSV
    def load_data(self):
        self.data = {}
        self.counties = []
        current_county = None
        try:
            # Get the directory of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            csv_path = os.path.join(script_dir, 'Book1.csv')
            with open(csv_path, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) >= 2:
                        label, count_str = row[0], row[1]
                        if 'County' in label and count_str.isdigit():
                            current_county = label
                            self.data[current_county] = []
                            self.counties.append(current_county)
                        elif current_county and count_str.isdigit():
                            self.data[current_county].append((label, int(count_str)))
        except FileNotFoundError:
            messagebox.showerror("Error", "Book1.csv not found.")
    
    # Define the method to handle submit button click
    def on_submit(self):
        # Get the selected county
        county = self.county_combo.get()
        # Get selected resources
        selected = [option for option, var in zip(self.options, self.check_vars) if var.get()]
        
        if not county:
            messagebox.showwarning("Input Error", "Please enter a county.")
            return
        
        if not selected:
            messagebox.showwarning("Input Error", "Please select at least one resource.")
            return
        
        if county not in self.data:
            messagebox.showerror("County Not Found", f"The county '{county}' is not in the database.")
            return
        
        # Find matching services
        results = []
        for service, count in self.data[county]:
            if any(any(kw in service.lower() for kw in self.resource_keywords[res]) for res in selected):
                results.append(f"{service}: {count}")
        
        if results:
            messagebox.showinfo("Matching Resources", "\n".join(results))
        else:
            messagebox.showinfo("No Matches", "No matching resources found for the selected options.")
    
    # Define the method to handle clear button click
    def on_clear(self):
        # Clear the county combobox selection
        self.county_combo.set('')
        # Reset all checklist options
        for var in self.check_vars:
            var.set(False)
        # Hide the buttons
        self.button_frame.pack_forget()
    
    # Define the method to update button visibility
    def update_buttons(self):
        # Show buttons if any checklist option is checked
        if any(var.get() for var in self.check_vars):
            self.button_frame.pack(pady=20)
        else:
            self.button_frame.pack_forget()

# Check if this script is being run as the main module
if __name__ == "__main__":
    # Create the main Tkinter root window
    root = tk.Tk()
    # Instantiate the ApplicationUI class with the root window
    app = ApplicationUI(root)
    # Start the Tkinter main event loop
    root.mainloop()