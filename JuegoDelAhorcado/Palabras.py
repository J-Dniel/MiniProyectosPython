#palabra que se agregaran por defecto
palabras = ['aire', 'ojos', 'piel', 'anteojos', 'joven', 'viejo', 'alto', 'bajo', 'pequeño', 'gordo', 'delgado', 'bella', 'azul', 'verde', 'negro', 'sombrero', 'guantes']

# Verificar Existencia de un archivo
def chequearExistencia(filepath):
    try:
        with open(filepath,'r') as f:
            return True
    except FileNotFoundError as e:
        return False
    except IOError as e:
        return False

def guardarPalabras(palabras):

    # Creacion de un archivo binario para almacenar las palabras
    with open('palabras.txt','a+') as f:

        for p in palabras:
            f.write(p.upper() + ",")

        f.close()


def LeerArchivo():

    # lectura de un archivo y almacena la palabras en una lista
    with open('palabras.txt','r+') as f:

        l = str(f.readline()).split(sep=',')

        f.close()
    return l
