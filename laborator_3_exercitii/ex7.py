lista_preturi = [17, 13, 10, 9, 2, 4, None, 8, None]
def fun(variable):
    if variable != None:
        return True
    else:
        return False
    
        
def reduction(variable):
    return variable - (10/100 * variable)

    
filtered = filter(fun, lista_preturi)
lista_redusa = map(reduction, filtered)
print(list(lista_redusa))