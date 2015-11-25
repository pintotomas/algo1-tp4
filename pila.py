class PilaVaciaError(Exception):
    pass
class Pila(object):
    """....."""
    def __init__(self):
        self.elementos = []

    def apilar(self,dato):
        self.elementos.append(dato)

    def desapilar(self):
       try:    
           quitar_dato = self.elementos.pop()
           return quitar_dato
       except IndexError:
           raise PilaVaciaError("La pila esta vacia")

    def ver_tope(self):
        try:
            return self.elementos[-1]
        except IndexError:
            raise PilaVaciaError()
    def esta_vacia(self):
        return len(self.elementos) == 0
