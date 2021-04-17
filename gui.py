import tkinter as tk
from tkinter import Label, ttk, messagebox
import main as cipherLib


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.version = None
        self.title = None

        # Ramki na elementy
        self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(row=0, column=0, padx=7, pady=7)
        tk.Label(self.inputFrame, text="Wprowadzanie", font="Helvetica 11 bold").pack(
            padx=3, pady=3, anchor="nw"
        )

        self.settingsFrame = tk.Frame(self)
        self.settingsFrame.grid(row=0, column=1, padx=7, pady=7)
        tk.Label(self.settingsFrame, text="Ustawienia", font="Helvetica 11 bold").pack(
            side=tk.TOP, padx=3, pady=3, anchor="nw"
        )

        self.buttonFrame = tk.Frame(self)
        self.buttonFrame.grid(row=1, column=0, columnspan=2, padx=7, pady=7)

        # Ramka wprowadzania
        self.firstInput = tk.Text(self.inputFrame, width=50, height=10)
        self.firstInput.insert(tk.END, "Tekst podstawowy")
        self.firstInput.pack(padx=3, pady=3)
        self.secondInput = tk.Text(self.inputFrame, width=50, height=10)
        self.secondInput.insert(tk.END, "Tekst zaszyfrowany")
        self.secondInput.pack(padx=3, pady=3)

        self.firstInput.bind("<FocusIn>", self.delPlaceholder)
        self.secondInput.bind("<FocusIn>", self.delPlaceholder)

        # Ramka ustawien
        tk.Label(self.settingsFrame, text="Szyfr").pack(anchor="nw")
        self.ciphers = ["Ogrodzeniowy", "Transpozycja kolumnowa"]
        self.cipherChoose = ttk.Combobox(
            self.settingsFrame, values=self.ciphers, state="readonly", width=23
        )
        self.cipherChoose.current(0)
        self.cipherChoose.pack(padx=5, pady=5)
        tk.Label(self.settingsFrame, text="Operacja").pack(anchor="nw")
        self.chosenOperation = tk.IntVar()
        operation = ["Szyfrowanie", "Deszyfrowanie"]
        for val, x in enumerate(operation):
            tk.Radiobutton(
                self.settingsFrame, variable=self.chosenOperation, text=x, value=val
            ).pack(padx=3, pady=3, anchor="w")
        # Pole na szyfr
        tk.Label(self.settingsFrame, text="Hasło / Klucz").pack(
            padx=3, pady=3, anchor="w"
        )
        self.key = tk.StringVar()
        self.passphrase = tk.Entry(self.settingsFrame, textvariable=self.key, width=20)
        self.passphrase.pack(padx=0, pady=0)
        # Ramka przycisku
        self.submitButton = tk.Button(
            self.buttonFrame,
            text="Szyfruj/Deszyfruj",
            font="Helvetica 12",
            command=self.buttonClicked,
        )
        self.submitButton.pack(padx=5, pady=5)

    def delPlaceholder(self, event):
        message = event.widget.get(1.0, tk.END)
        if message == "Tekst podstawowy\n" or message == "Tekst zaszyfrowany\n":
            event.widget.delete(1.0, tk.END)

    def buttonClicked(self):
        # TODO: Sprawdzanie poprawnosci wprowadzania danych, usuwanie znakow bialych, konwersja na wielkie/male litery
        chosenCipher = self.cipherChoose.get()
        password = self.passphrase.get()
        operation = self.chosenOperation.get()
        message = self.firstInput.get(1.0, tk.END)

        if len(password) < 1:
            messagebox.showwarning("Error", "Nie wprowadzono klucza/hasła")
            print("Bad password")
            return
        if len(message) <= 1:
            messagebox.showwarning("Error", "Nie wprowadzono wiadomości do szyfrowania")
            print("No message found!")
            return
        answer = None
        if chosenCipher == self.ciphers[0]:
            # Ogrodzeniowy
            password = int(password)
            if operation == 0:
                # Szyfrowanie
                answer = cipherLib.fenceCipher(message, password)
            else:
                # Deszyfrowanie
                answer = cipherLib.fenceDecipher(message, password)
        elif chosenCipher == self.ciphers[1]:
            # Transpozycyjny
            if operation == 0:
                # Szyfrowanie
                answer = cipherLib.columnTransCipher(message, password)
            else:
                # Deszyfrowanie
                answer = cipherLib.columnTransDecipher(message, password)
        else:
            print("Wrong cipher type")

        if answer != None:
            self.secondInput.delete(1.0, tk.END)
            self.secondInput.insert(tk.END, answer)


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
