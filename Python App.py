import tkinter as tk
from tkinter import ttk

class ApplicationUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Application")
        self.root.geometry("500x400")
        
        # Title 
        header = ttk.Label(root, text="HELP HUB", 
                          font=("Times New Roman", 20, "bold"))
        header.pack(pady=20)
        
        # Input
        input_frame = ttk.Frame(root)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        ttk.Label(input_frame, text="County:").pack(side="left", padx=5)
        self.name_entry = ttk.Entry(input_frame, width=30)
        self.name_entry.pack(side="left", padx=5)
        
        # Button frame
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Submit", 
                  command=self.on_submit).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Clear", 
                  command=self.on_clear).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Exit", 
                  command=root.quit).pack(side="left", padx=5)
        
        # Output area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack(pady=10, padx=20, fill="both", expand=True)
    
    def on_submit(self):
        name = self.name_entry.get()
        self.output_text.insert("end", f"Hello, {name}!\n")
    
    def on_clear(self):
        self.output_text.delete("1.0", "end")

if __name__ == "__main__":
    root = tk.Tk()
    app = ApplicationUI(root)
    root.mainloop()