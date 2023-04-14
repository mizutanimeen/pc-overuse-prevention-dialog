import tkinter as tk
from tkinter import * 

class CustomDialog(tk.Toplevel):
    input_text = "close"
    
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.withdraw()
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.title("Custom Dialog")
        self.resizable(False, False)
        self.attributes('-toolwindow', True)
        self.attributes('-topmost', True)
        self.bind("<Escape>", lambda e: self.on_close())
        self.bind("<FocusIn>", lambda e: self.grab_set())
        self.bind("<FocusOut>", lambda e: self.grab_release())
        self.bind("<Map>", self.disable_minimize_button)
        self.bind("<Unmap>", self.enable_minimize_button)

        self.overrideredirect(True)
        frame = tk.Frame(self)
        self.label = tk.Label(frame, text="↓input↓\n{}".format(self.input_text))
        self.label.pack(pady=10)
        self.button = tk.Button(frame, text="Button", command=self.on_close)
        self.button.pack(pady=10)
        self.entry = tk.Entry(frame, width=30)
        self.entry.pack(pady=10)
        self.entry.focus_set()
        frame.pack(expand=True)
        frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.update_idletasks()

        sizex = 1000
        sizey = 500
        x = (1920 - sizex) // 2 
        y = (1080 - sizey) // 2 
        self.geometry("{}x{}+{}+{}".format(sizex,sizey,x, y))

        self.deiconify()

    def disable_minimize_button(self, event):
        self.attributes("-toolwindow", True)

    def enable_minimize_button(self, event):
        self.attributes("-toolwindow", False)

    def on_close(self, event=None):
        if self.entry.get() == self.input_text:
            self.destroy()


root = tk.Tk()
root.withdraw()

dialog = CustomDialog(root)
dialog.wait_window()

root.destroy()
