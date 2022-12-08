##Versión mejorada de rabbit.py
import pyzipper
import sys

def main():
    if len(sys.argv) != 3:
        print("Uso: python archivo.zip max_lenght")
        return 1

    file : str = sys.argv[1]

    max_length : int = sys.argv[2]

    for i in range(1, max_length + 1):
        #Establecer longitud en i
        #rellenar cada caracter con las opciones
        #con la contraseña finalizada, probar contraseña

        #password = str(i).zfill(3)



        try:
            with pyzipper.AESZipFile(file,'r') as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                print(f"psw {password} - Contraseña correcta")
                return 0
        except Exception as e:
            print(e)
            print(f"psw {password} - Contraseña fallida")

main()