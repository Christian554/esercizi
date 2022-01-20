import math_oper

p = input("Inserisci il primo numero e premi INVIO: ")
k = input("Inserisci il secondo numero e premi INVIO: ")

if p < k:
    
    print("NON è possibile prendere più oggetti di quanti ce ne siano.")
else:
    print( "Il numero di combinazioni di " + p + " oggetti presi a " + k + " a " +k+" è:")
    print(math_oper.combination(int(p),int(k)))
