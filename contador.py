import re


def contador_palabras(entrada):

    contador_palabras = []

    # Convierto a una lista y defino un separador con Expresion Regular
    frase = re.split(r'[- , ; ! _ % # ! ¡ " "]', entrada)

    print(frase)

    nueva_lista = []


    # Limpiar la cadena de caracteres que se pueden filtrar
    for letra in frase:
        palabra = ''

        for j in letra:
            # Defino un caracter de codigo ASCII que puede tener en cuenta
            if((ord(j) >= 65 and ord(j) <= 90) or (ord(j) >= 97 and ord(j) <= 122) or (ord(j) >= 160 and ord(j) <= 165)):
                palabra += j
            else:
                continue
        
        nueva_lista.append(palabra)
            

    for palabra in nueva_lista:
        bandera = False
        
        for j in palabra:
            
            # Defino un caracter de codigo ASCII que puede tener en cuenta
            if((ord(j) >= 65 and ord(j) <= 90) or (ord(j) >= 97 and ord(j) <= 122) or (ord(j) >= 160 and ord(j) <= 165)):
                bandera = True
            else:
                bandera = False
                
        # Para guardar las palabras
        if (bandera == True):
            contador_palabras.append(palabra)
    
    print(65 * '=')
    print(f'¡Muy bien, tu me has mostrado tu pensamiento en {len(contador_palabras)} palabras!')
    print(65 * '=')
    
    return len(contador_palabras)

