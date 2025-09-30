import tkinter as tk
import time
import threading

# Ajout d'une structure global pour stocker l'expression
expression = ""
typing_in_progress = False

def get_expression():
    global expression
    return expression

def calculate():
    global expression
    if expression:
        eval_expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(eval_expression)
        expression = str(result)
        if len(expression) > 10:
            expression = expression[:10]
            expression += "..."
        # print(f"Result: {expression}")
        # reset = True


def typing_effect(message):
    global expression, typing_in_progress
    typing_in_progress = True
    original_expression = expression
    
    for i, char in enumerate(message):
        if not typing_in_progress:
            expression = original_expression
            break
        expression = original_expression + message[:i+1]
        time.sleep(0.15)

    if typing_in_progress:
        time.sleep(1) 
        expression = ""
    
    typing_in_progress = False

def append_to_expression(value):
    global expression, typing_in_progress
    
    if typing_in_progress:
        typing_in_progress = False
        time.sleep(0.1) 
    
    if value == 'C':
        expression = ""
    elif value == '❤':
        expression = ""
        thread = threading.Thread(target=typing_effect, args=("❤ I love you ❤",))
        thread.daemon = True
        thread.start()
        expression = ""
    elif value == '★':
        expression = ""
        thread = threading.Thread(target=typing_effect, args=("★ You shine ★",))
        thread.daemon = True
        thread.start()
        expression = ""
    elif value == '❀':
        expression = ""
        thread = threading.Thread(target=typing_effect, args=("❀ My flower ❀",))
        thread.daemon = True
        thread.start()
        expression = ""
    if value not in ['❤', '★', '❀', 'C']:
        expression += str(value)    