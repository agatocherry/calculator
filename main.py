import tkinter as tk
import calculate as calc
import display as disp

# TODO: Ajouter la possibilité de taper au clavier !
# TODO: Ajouter une typo pixelisée

# Window setup
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

# Background color
root.configure(bg="#E2B8AD")

root.text = tk.StringVar()
root.text.set("Calculator")

# Create display with decorative frame
label = disp.create_display_with_frame(root, root.text)
# Initialize display for updates
disp.init_display(root, root.text)
disp.update_display()

# Button number here
button_frame = tk.Frame(root, bg="#E2B8AD")
button_frame.pack(pady=5)
buttons = [
    '❤', '★', '❀', '+',
    '7', '8', '9', '-',
    '4', '5', '6', '×',
    '1', '2', '3', '÷',
    '.', '0', 'C', '='
]
for button in buttons:
    btn = tk.Button(button_frame, text=button, font=("Arial", 18), width=3, height=2)
    btn.grid(row=buttons.index(button)//4, column=buttons.index(button)%4, padx=5, pady=5)
    btn.configure(bg="#6D322A", fg="white", borderwidth=0, activebackground="#C38D9E", activeforeground="white")
    if button == '=':
        btn.config(command=lambda b=button: calc.calculate())
    else:
        btn.config(command=lambda b=button: calc.append_to_expression(b))

# Start the GUI event loop
root.mainloop()