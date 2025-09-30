import tkinter as tk
import calculate as calc
import display as disp

# TODO: Réduire espace entre l'écran et les boutons

# Window setup
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.focus_set()  # Permet de capturer les événements clavier

# Background color
root.configure(bg="#E2B8AD")

root.text = tk.StringVar()
root.text.set("Calculator")

# Utiliser une icône PNG (plus fiable que .ico)
icon = tk.PhotoImage(file="./assets/calc.png")
root.iconphoto(False, icon)

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
    btn = tk.Button(button_frame, text=button, font=("Pixelify Sans", 18), width=3, height=2)
    btn.grid(row=buttons.index(button)//4, column=buttons.index(button)%4, padx=5, pady=5)
    btn.configure(bg="#6D322A", fg="white", borderwidth=0, activebackground="#C38D9E", activeforeground="white")
    if button == '=':
        btn.config(command=lambda b=button: calc.calculate())
    else:
        btn.config(command=lambda b=button: calc.append_to_expression(b))

# Fonction pour gérer les événements clavier
def on_key_press(event):
    key = event.char
    
    # Mapping des touches du clavier vers les symboles de la calculatrice
    key_mapping = {
        '0': '0', '1': '1', '2': '2', '3': '3', '4': '4',
        '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
        '+': '+', '-': '-', '*': '×', 'x': '×', 'X': '×',
        '/': '÷', '.': '.', ',': '.',
        'c': 'C', 'C': 'C',
        '\r': '=',  # Touche Entrée
        '\x08': 'C',  # Touche Backspace (efface tout)
    }
    
    # Touches spéciales (avec event.keysym)
    if event.keysym == 'Return':
        calc.calculate()
        return
    elif event.keysym == 'BackSpace':
        calc.append_to_expression('C')
        return
    elif event.keysym == 'Escape':
        calc.append_to_expression('C')
        return
    
    # Traitement des touches normales
    if key in key_mapping:
        mapped_key = key_mapping[key]
        if mapped_key == '=':
            calc.calculate()
        else:
            calc.append_to_expression(mapped_key)

# Lier les événements clavier à la fenêtre
root.bind('<KeyPress>', on_key_press)

# Start the GUI event loop
root.mainloop()