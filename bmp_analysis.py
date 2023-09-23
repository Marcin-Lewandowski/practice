from PIL import Image
import numpy as np

# Wczytaj plik BMP
img = Image.open("C://kodilla/practice/test1.bmp")

# Pobierz wymiary obrazu
szerokosc, wysokosc = img.size

licznik_komorek_brzegowych = 0
licznik_komorek_oceanu = 0
licznik_komorek_ladu = 0
licznik_komorek_ropy = 0

# Tworzenie pustej macierzy 2x4 z samymi zerami
# macierz = np.zeros((wysokość, szeokość))
# macierz = np.zeros((wysokosc, szerokosc))
macierz = np.full((wysokosc, szerokosc), 'AAAA')

# Iteruj przez każdy piksel i pobierz jego kolor w formacie RGB
for x in range(szerokosc):
    for y in range(wysokosc):
        pixel_color = img.getpixel((x, y))
        if pixel_color == (0,0,255):
            licznik_komorek_oceanu += 1
            macierz[y, x] = "O"
            #print("To jest ocean ", licznik)
        if pixel_color == (0,255,0):
            licznik_komorek_ladu += 1
            macierz[y, x] = "L"
            #print("To jest ląd ", licznik)
        elif pixel_color == (250,200,50):
            licznik_komorek_brzegowych += 1
            macierz[y, x] = "B"
            #print("To jest brzeg ", licznik)
        elif pixel_color == (0,0,0):
            licznik_komorek_ropy += 1
            macierz[y, x] = "Ropa"
        #print(f"Piksel ({x}, {y}): RGB = {pixel_color}")

# Zamknij plik BMP
img.close()
print()
print("Liczba komórek oceanu: ", licznik_komorek_oceanu)
print()
print("Liczba komórek lądu: ", licznik_komorek_ladu)
print()
print("Liczba komórek brzegowych: ", licznik_komorek_brzegowych)
print()
print("Liczba komórek ropy: ", licznik_komorek_ropy)



# Wyświetlenie pustej macierzy
print(macierz)
print("Szerokość: ", szerokosc)
print("Wysokość: ", wysokosc)
print("Img size: ", img.size)