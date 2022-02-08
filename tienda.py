from datetime import datetime


class transaccion:

    VENTA = 1
    ABASTESIMIENTO = 2
    def __init__(self, tipo: int,cantidad: int):
        self._tipo: int = tipo
        self._cantidad: int = cantidad
        self._fecha = datetime.now() 
    
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, valor):
        if valor == 1 or valor == 2:
           self._tipo = valor 


class Libro:
    def __init__(self,isbn,titulo,precio_compra,precio_venta,cantidad_actual) -> None:
        pass
        self.isbn = isbn
        self.titulo = titulo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad_actual = cantidad_actual
        self.transacciones = list()

class Tienda:
  def __init__(self) -> None:
    self.dinero_en_caja = 1000000
    self.catalogo = dict()


if __name__ == "__main__":
    trans_1 = transaccion(transaccion.VENTA, 5)
    trans_2 = transaccion(transaccion.ABASTESIMIENTO,10)

    print(f"Tipo t1: {trans_1.cantidad}")
    print(f"Tipo t2: {trans_2.cantidad}")

    trans_1.cantidad = 20 
    print(f"Tipo t1: {trans_1.cantidad}")
    print(f"Tipo t2: {trans_2.cantidad}")

        
