import re

class Correo():
    def __init__(self, correo):
        self.correo = correo


    def validarCorreo(self):
        patron = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        correo = input("-> Ingrese su correo: ")
        if re.search(patron, correo):
            if self.correo == correo:
                print("-> Correo valido")
                print("-> Hola", correo)
            else:
                raise Exception("Correo inválido")
        else:
            print("Correo invalido")

correo = ["jacobo@gmail.com", "maria@gmail.com"]

for i in correo:
    try:
        Correo(i).validarCorreo()
    except Exception as e:
        print(e)