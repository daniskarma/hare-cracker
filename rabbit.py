import pyzipper
import sys

def main():
    if len(sys.argv) != 2:
        print("Uso: python archivo.zip")
        return 1

    file = sys.argv[1]

    for i in range(1000):
        password = str(i).zfill(3)
        try:
            with pyzipper.AESZipFile(file,'r') as zf:
                zf.extractall(pwd=bytes(password, 'utf-8'))
                print(f"psw {password} - Contraseña correcta")
                return 0
        except Exception as e:
            print(e)
            print(f"psw {password} - Contraseña fallida")

main()