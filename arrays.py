# Obejrzec odcinek o tablicach i zrobić przykład dodawania odejmowania i mnożenia tablic

list = [102, 6.6, '77', '564', 75, '3.92', 'E', 2.77, 7.66, 'C', '408', 605, '690', 'Z', '134', 'S', 'K', 148, '68', '654', 'U', '537', 0.64, 905, 5.75, 302, '7.57', '834', '0.64', '29', '709', '8.28', 'Y', 640, 'U', '0.92', 4.63, '259', '245', '5.1', 'Z', 'D', '5.58', 1.26, 6.95, '2.87', '9.25', 'F', 273, '852'] 

counter = 0

for item in list:
    counter += 1
    if isinstance(item, int):
        print("To jest liczba całkowita: ", item)
    elif isinstance(item, str):
        print("To jest string: ", item)
    elif isinstance(item, float):
        print("To jest liczba zmiennoprzecinkowa: ", item)
     

print("Lista zawiera: ",  len(list), " elementów")

print("Licznik wszystkich elementów listy: ", counter)