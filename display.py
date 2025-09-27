import tkinter as tk
import calculate as calc

# Store references to root and text variable
_root = None
_text_var = None
_label = None

def create_display_with_frame(root, text_var):
    """Create the display area with text label and decorative frame"""
    global _root, _text_var, _label
    _root = root
    _text_var = text_var
    
    # Display area container
    display_frame = tk.Frame(root, bg="#E2B8AD")
    display_frame.pack(pady=42)
    
    # Main text label with decorative background
    _label = tk.Label(display_frame, bg="#CFA195", fg="white", font=("Arial", 24), 
                     bd=5, padx=2, pady=10, width=15)
    _label.pack(pady=(0, 5))
    _label.config(textvariable=text_var)
    
    return _label

def init_display(root, text_var):
    global _root, _text_var
    _root = root
    _text_var = text_var

def update_display():
    if _root is None or _text_var is None:
        return
    
    if calc.get_expression() == "":
        _text_var.set("0")
    else:
        _text_var.set(calc.get_expression()) 
    _root.after(100, update_display)