nmrs = [1,2,3,4,5,6,7,8,9,10]

def variable(nmrs):
 
 suma_impares =0
 for numero in nmrs:
    if numero % 2 != 0:
        suma_impares += numero
    

 return suma_impares

result = variable(nmrs)
 
print("Suma de valores impares en el rango 1 a 10: ", result)