import tkinter as tk
from tkinter import Label, ttk, messagebox
import main as cipherLib
from tkinter import filedialog as fd
import webbrowser as web


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.version = "v1.0"
        self.window_title = "Szyfrowanie - ISTU"
        self.title(self.window_title + " " + self.version)
        self.resizable(width=False, height=False)
        self.menu = tk.Menu(self, tearoff=0)

        # Tworzenie menu
        filemenu = tk.Menu(self.menu, tearoff=0)
        filemenu.add_command(label="Wczytaj z pliku", command=self.importFromFile)
        filemenu.add_command(label="Zapisz do pliku", command=self.exportToFile)
        self.menu.add_cascade(label="Plik", menu=filemenu)

        aboutmenu = tk.Menu(self.menu, tearoff=0)
        aboutmenu.add_command(label="Instrukcja", command=self.openInstructions)
        aboutmenu.add_command(label="O programie", command=self.showAbout)
        self.menu.add_cascade(label="Pomoc", menu=aboutmenu)

        self.config(menu=self.menu)

        # Ramki na elementy
        self.inputFrame = tk.Frame(self)
        self.inputFrame.grid(row=0, column=0, padx=7, pady=7)
        tk.Label(self.inputFrame, text="Wejście", font="Helvetica 11 bold").pack(
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

        tk.Label(self.inputFrame, text="Wynik", font="Helvetica 11 bold").pack(
            padx=3, pady=3, anchor="nw"
        )

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

    def openURL(self, url):
        web.open_new(url)

    def showAbout(self):
        text = """Aplikacja służy do szyfrowania i odszyfrowywania wiadomości korzystając z szyfru ogrodzeniowego lub szyfru transpozycji kolumnowej.\nAby dowiedzieć się jak korzystać z aplikacji naciśnij 'Instrukcja' w menu 'Pomoc'."""
        window = tk.Toplevel(self)
        # window.geometry("300x250")
        window.resizable(width=False, height=False)
        window.title("O programie")
        tk.Label(window, text=self.window_title, font="Helvetica 11 bold").pack(
            padx=6, pady=(3, 10), anchor="center"
        )
        tk.Message(window, text=text, aspect=300).pack(padx=4, pady=(0, 6), fill=tk.X)
        tk.Label(
            window,
            text="Autorzy: Paweł Szczepka, Tomasz Tendera",
            font="Helvetica 10 italic",
        ).pack(padx=3, pady=(3, 6), anchor=tk.CENTER)
        link = tk.Label(
            window, text="Github", font="Helvetica 10 italic", fg="blue", cursor="hand2"
        )
        link.pack(padx=3, pady=3, anchor=tk.CENTER)
        link.bind(
            "<Button-1>",
            lambda x: self.openURL("https://github.com/graniasty-dot/Szyfrowanko"),
        )
        tk.Button(window, text="Ok", width=20, command=window.destroy).pack(
            padx=3, pady=5
        )

    def openInstructions(self):
        answer = web.open(".\\instructions.html")
        if answer != True:
            print("Cannot open instructions")

    def delPlaceholder(self, event):
        message = event.widget.get(1.0, tk.END)
        if message == "Tekst podstawowy\n" or message == "Tekst zaszyfrowany\n":
            event.widget.delete(1.0, tk.END)

    def importFromFile(self):
        file = fd.askopenfilenames(
            title="Wczytaj plik", filetypes=[("Text file", ".txt")]
        )[0]
        if file != None:
            print(file)
            try:
                with open(file, "r") as f:
                    self.firstInput.delete(1.0, tk.END)
                    self.firstInput.insert(tk.END, f.read())
            except Exception as e:
                messagebox.showerror(title="Nie można odczytać pliku", message=e)
                print(e)

    def exportToFile(self):
        file = fd.asksaveasfilename(
            title="Zapisz jako", filetypes=[("Text file", ".txt")]
        )
        if file != None:
            print(file)
            try:
                with open(file + ".txt", "w") as f:
                    output = self.secondInput.get(1.0, tk.END)
                    f.write(output)
            except Exception as e:
                messagebox.showerror(title="Nie można zapisać pliku", message=e)
                print(e)

    def buttonClicked(self):
        # TODO: Sprawdzanie poprawnosci wprowadzania danych, konwersja na wielkie/male litery
        chosenCipher = self.cipherChoose.get()
        password = self.passphrase.get()
        operation = self.chosenOperation.get()
        message = self.firstInput.get(1.0, tk.END)
        message = self.stripWhitespace(message)
        if len(password) < 1:
            messagebox.showwarning("Error", "Nie podano klucza/hasła!")
            print("Bad password")
            return
        if len(message) < 1:
            messagebox.showwarning("Error", "Nie wprowadzono wiadomości!")
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

    def stripWhitespace(self, string):
        return "".join(string.split())


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
