class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        
def insertar(raiz,nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None:
                raiz.derecha=nodo
            else:
                insertar(raiz.derecha,nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda =nodo
            else:
                insertar(raiz.izquierda,nodo)
                
def inorden(raiz):
    if raiz is not None:
        inorden(raiz.izquierda)
        print(raiz.dato)
        inorden(raiz.derecha)

def preorden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

raiz = Nodo(10)
insertar(raiz,Nodo(15))
insertar(raiz,Nodo(8))
insertar(raiz,Nodo(17))
insertar(raiz,Nodo(23))
insertar(raiz,Nodo(5))
insertar(raiz,Nodo(1))

inorden(raiz)
print()

preorden(raiz)
print()