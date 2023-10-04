#hugo said taviras parra


#utilice el def que es el metodo para crear una funcion para poder aislar los datos y calculos que se deben hacer en el programa en este calos los utilice 
#para definir cual seria el calulo del indice de masa corporal IMC asi como tambien reducir las lineas de los casos if y else

def nivelIMC(IMC):
    if IMC < 18.9:
        return "UN PESO BAJO"
    elif 18.9 <= IMC <= 24.99:
        return "UN PESO NORMAL"
    elif 25 <= IMC <= 29.99:
        return"SOBREPESO"
    elif 30 <= IMC <= 34.99:
        return"OBESIDA LEVE"
    elif 35 <= IMC <= 39.99:
        return"OBESIDAD MEDIA"
    elif IMC >= 40:
        return"OBESIDAD MORBIDA"
    #elif sirve en este caso para evitar el uso de else y crear un ciclo if-else por cada caso posible del programa simplemente se coloca una condicion 
    # especfica por cada caso si la conndicion de alguno se cumple los demas se omiten agilizando y reduciendo el codigo base del programa

def calculoIMC(p,a):
    return p /(a*a)

print('============================================================================================================================================')
print('ESTE PROYECTO TE DEJARA CALCULAR TU INDICE DE MASA CORPORAL(IMC) Y SABER SI TIENES UN PESO A DECUADO EN BASE A TU ALTURA Y PESO')
print('============================================================================================================================================')

nombre= str(input('Cual es tu nombre? '))
print('============================================================================================================================================')
print('HOLA', nombre )
print('============================================================================================================================================')
peso= float(input('Ingresa tu peso en (KG): '))
print('============================================================================================================================================')
altura= float(input('Ingresa tu altura en (M): '))
print('============================================================================================================================================')
print('Su nivel IMC indica que usted tiene:', nivelIMC(calculoIMC(peso,altura)) )
#en el ultimo mensaje impreso a la pantalla se manda el mensaje final con la condicion especifica la cual incluye la otra condicion especifica dentro de la 
#misma linea es decir se manda el mensaje de pantalla seguido de la fncion nivelIMC la cual contiene las repuestas a cada posible calculo del IMC   
#dentro de esta funcion se incluye la funcion caluloIMC la cual incluye la formula para calcular el IMC dentro de la cual especifico que los valores de p,a seran 
#sustituidos por los valores peso y altura en ese orden esto deja que podamos imprimir y especificar la repuesat adecuada para cada posible caso en una sola linea





    