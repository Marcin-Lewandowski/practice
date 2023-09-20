import tkinter as tk
import numpy as np

# Funkcja sprawdzająca odpowiedź użytkownika
def sprawdz_odpowiedz():
    odpowiedz = pole_odpowiedzi.get()
    
    try:
        odpowiedz = int(odpowiedz)
        if odpowiedz == 2 + 2:
            wynik.config(text="Brawo! Odpowiedź jest poprawna.", fg="green")
        else:
            wynik.config(text="Błąd. Odpowiedź jest niepoprawna.", fg="red")
    except ValueError:
        wynik.config(text="Błąd. Podaj liczbę całkowitą jako odpowiedź.", fg="red")

# Tworzenie głównego okna
root = tk.Tk()
root.title("Quiz Matematyczny")

# Ustawienie rozmiaru głównego okna na 400x400 pikseli
root.geometry("400x400")

# Tworzenie etykiety z pytaniem
etykieta_pytanie = tk.Label(root, text="Ile jest 2 plus 2?")
etykieta_pytanie.pack()

# Tworzenie pola do wprowadzenia odpowiedzi
pole_odpowiedzi = tk.Entry(root)
pole_odpowiedzi.pack()

# Tworzenie przycisku do sprawdzania odpowiedzi
przycisk_sprawdz = tk.Button(root, text="Sprawdź", command=sprawdz_odpowiedz)
przycisk_sprawdz.pack()

# Tworzenie etykiety wyniku
wynik = tk.Label(root, text="", fg="black")
wynik.pack()

# Uruchamianie głównej pętli programu
root.mainloop()