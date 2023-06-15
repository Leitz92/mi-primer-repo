# librería locate de py. solicitará de pesetas a euros y de euros a pesetas conversor. 
# que quieres utilizar de pesetas a euros y de euros a pesetas. a nivel de euro tiene que tener formato euro.
# tiene que tener un menú de selección
import locale

# Establecemos la configuración regional de ESPAÑA!
locale.setlocale(locale.LC_ALL, "es_ES.utf8")

# Función que convierte pesetas a euros
def pesetas_euros(pesetas):
    return round(pesetas/166.386,2)

# Función que convierte euros a pesetas
def euros_pesetas(euros):
    return round(euros*166.386,2)

# Función que muestra menú
def mostrar_menu():
    print('---- Menú de conversión ----')
    print('[1] - Convertir Pesetas a Euros\n[2] - Convertir Euros a Pesetas\n[3] - Salir')

# Programa principal
def run():
    while True:
        mostrar_menu()
        opcion = int(input('👉 '))

        if opcion == 1:
            pesetas_str = input('Dime las pesetas: ')
            pesetas = locale.atof(pesetas_str)
            euros = pesetas_euros(pesetas)
            print(f'{locale.currency(pesetas, grouping=True).replace("€", "pts")} son {locale.currency(euros, grouping=True)}')
        elif opcion == 2:
            euros_str = input('Dime los euros: ')
            euros = locale.atof(euros_str)
            pesetas = euros_pesetas(euros)
            print(f'{locale.currency(euros, grouping=True)} son {locale.currency(pesetas, grouping=True).replace("€", "pts")}')
        elif opcion == 3:
            print('FINALIZANDO PROGRAMA!')
            break
        else:
            print('Error: No introduciste una opción correcta.')


if __name__ == '__main__':
    run()


