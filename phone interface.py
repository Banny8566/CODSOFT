import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Phone Calculator")
        self.root.geometry("400x600")
        self.current_input = ""
        
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Entry(self.root, font=('Arial', 24), borderwidth=2, relief='solid', justify='right')
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        for i, text in enumerate(button_texts):
            button = tk.Button(self.root, text=text, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            row = (i // 4) + 1
            col = i % 4
            button.grid(row=row, column=col, sticky="nsew")

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.current_input = ""
        elif char == '=':
            try:
                self.current_input = str(eval(self.current_input))
            except:
                self.current_input = "Error"
        else:
            self.current_input += char
        
        self.update_display()

    def update_display(self):
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
