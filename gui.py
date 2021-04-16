import tkinter as tk
from tkinter import Label, ttk
import main


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.version = None
        self.title = None
        
        # Ramki na elementy
        self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(row=0, column=0, padx=7, pady=7)
        tk.Label(self.inputFrame, text="Wprowadzanie", font="Helvetica 11 bold").pack(padx=3, pady=3, anchor="nw")

        self.settingsFrame = tk.Frame(self)
        self.settingsFrame.grid(row=0, column=1, padx=7, pady=7)
        tk.Label(self.settingsFrame, text="Ustawienia", font="Helvetica 11 bold").pack(side=tk.TOP, padx=3, pady=3, anchor="nw")

        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=1, column=0, columnspan=2, padx=7, pady=7)

        # Ramka wprowadzania
        self.firstInput = tk.Text(self.inputFrame, width =50, height=10)
        self.firstInput.insert(tk.END, "Tekst podstawowy")
        self.firstInput.pack(padx=3, pady=3)
        self.secondInput = tk.Text(self.inputFrame, width=50, height=10)
        self.secondInput.insert(tk.END, "Tekst zaszyfrowany")
        self.secondInput.pack(padx=3, pady=3)
        
        # Ramka ustawien
        tk.Label(self.settingsFrame, text="Szyfr").pack(anchor="nw")
        self.ciphers = ["Ogrodzeniowy", "Transpozycja kolumnowa"]
        self.cipherChoose = ttk.Combobox(self.settingsFrame, values=self.ciphers, state="readonly", width=23)
        self.cipherChoose.current(0)
        self.cipherChoose.pack(padx=5, pady=5)
        tk.Label(self.settingsFrame, text="Operacja").pack(anchor="nw")
        self.chosenOperation = tk.IntVar()
        operation = ["Szyfrowanie", "Deszyfrowanie"]
        for val, x in enumerate(operation):
            tk.Radiobutton(self.settingsFrame, variable=self.chosenOperation, text=x, value=val).pack(padx=3, pady=3, anchor="w")
        #Pole na szyfr
        self.passphrase=tk.Text(self.settingsFrame,width=20,height=1)
        self.passphrase.insert(tk.END, "Hasło")
        self.passphrase.pack(padx=0, pady=0)
        #Ramka przycisku
        self.submitButton = tk.Button(self.buttonFrame, text="Szyfruj/Deszyfruj", font="Helvetica 12")
        self.submitButton.pack(padx=5, pady=5)


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()