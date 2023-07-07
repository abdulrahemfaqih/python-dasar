

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.configure(bg='white')
window.geometry('300x200')

window.title(f'{"LOGIN"}') 

# Frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(
    padx = 10, pady = 10, fill = 'x', expand = True
    )

# komponen-komponen
'''label email'''
email_label = ttk.Label(input_frame, text='email')
email_label.pack(
    padx = 10, fill = 'x', expand = True
    )   

'''entry email ''' 
EMAIL = tk.StringVar()
email_entry = ttk.Entry(input_frame,textvariable = EMAIL)
email_entry.pack(
    padx = 10, fill = 'x', expand = True
    )   
    
'''label password'''
password_label = ttk.Label(input_frame, text='password')
password_label.pack(
    padx = 10, fill = 'x', expand = True
    )   

'''entry pasword'''
PASSWORD = tk.StringVar()
password_entry = ttk.Entry(input_frame,textvariable = PASSWORD)
password_entry.pack(
    padx = 10, fill = 'x', expand = True
    )   
'''tombol'''
def tombol_click():
    print(PASSWORD.get())


tombol_login = ttk.Button(input_frame, text='LOGIN', command = tombol_click)
tombol_login.pack(
    fill = 'x', expand = True, padx = 10, pady  = 10

)


window.mainloop() 