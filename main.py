import tkinter as tk

# Window setup
root = tk.Tk()
root.title("Code-o-dachi")
root.geometry("400x300")

label = tk.Label(root)
label.pack(pady=50)

# Background color
root.configure(bg="#F3CFC6")
label.configure(bg="#F3CFC6")

# Start the GUI event loop
root.mainloop()