class Producto:
    def __init__(self, nombre, precio_unitario, stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def reducir_stock(self, cantidad: int) -> bool:
        if self.stock >= cantidad:
            self.stock -= cantidad
            print(f'INFO: Stock de "{self.nombre}" actualizado. Nuevo stock: {self.stock}')
            return True
        else:
            print(f'ALERTA: No hay suficiente stock de "{self.nombre}".'
                  f'Requerido {cantidad}, disponible: {self.stock}')
            return False

    def __str__(self) -> str:
        return f"Producto: {self.nombre}, Precio: ${self.precio_unitario:.2f}, Stock: {self.stock} unidades"

class Pedido:
    id=1
    def __init__(self, pedidos: dict, descuento: float = 0.1):
        self.pedidos = pedidos
        self.id = Pedido.id
        Pedido.id+=1
        self.estado = 'Recibido'
        self.descuento = descuento
        self.costo_total = self.costo_total()

    def actualizar_estado(self, nuevo_estado: str):
        print(f'El estado del pedido #{self.id} ha cambiado de {self.estado} a {nuevo_estado}')
        self.estado = nuevo_estado

    def costo_total(self):
        subtotal = 0
        for producto, cantidad in self.pedidos.items():
            subtotal += producto.precio_unitario * cantidad
        total_con_desc = subtotal * (1-self.descuento)
        return total_con_desc

    def procesar_pedido(self) -> bool:
        # 1. Verificar stock disponible

        for producto, cantidad in self.pedidos.items():
            if producto.stock < cantidad:
                print(f'ERROR: No se puede procesar el pedido #{self.id}. Stock de {producto.nombre} insuficiente')
                self.actualizar_estado('Cancelado')
                return False
        # Si paso el primer paso, se procede a reducir el stock

        for producto, cantidad in self.pedidos.items():
            producto.reducir_stock(cantidad)
        self.actualizar_estado('En preparación')
        print(f'Pedido #{self.id} procesado exitosamente. Nuevo estado: {self.estado}')
        return True

    def __str__(self) -> str:
        lista_productos_str = "\n".join([f"  - {cantidad} x {producto.nombre} (${producto.precio_unitario:.2f} c/u)"
                                         for producto, cantidad in self.pedidos.items()])
        return (f'\n-- PEDIDO #{self.id} --\n'
                f'Estado: {self.estado}\n'
                f'Productos:\n{lista_productos_str}\n'
                f'Costo Total (con {self.descuento*100:.0f}% de descuento: ${self.costo_total:.2f})\n'
                f'--------------------')

if __name__ == "__main__":
    print("=============================================")
    print("  Bienvenido al sistema de 'Delicioso Sabor' ")
    print("=============================================\n")

    # 1. Creamos el inventario de productos del restaurante
    print("--- Creando Inventario Inicial ---")
    hamburguesa = Producto("Hamburguesa", 12000.00, 50)
    papas_fritas = Producto("Papas Fritas", 4000.00, 100)
    gaseosa = Producto("Gaseosa", 3800.00, 80)

    print(hamburguesa)
    print(papas_fritas)
    print(gaseosa)
    print("--------------------------------\n")

    # 2. Un cliente realiza un primer pedido
    print("--- Nuevo Pedido de Cliente 1 ---")
    orden_cliente_1 = {
        hamburguesa: 2,
        papas_fritas: 1,
        gaseosa: 2
    }
    pedido_1 = Pedido(orden_cliente_1)
    print(pedido_1) # Mostramos el pedido recién creado

    # 3. Procesamos el pedido (esto afectará al stock)
    pedido_1.procesar_pedido()

    # 4. Verificamos cómo quedó el stock después del primer pedido
    print("\n--- Inventario Actualizado ---")
    print(hamburguesa)
    print(papas_fritas)
    print(gaseosa)
    print("----------------------------\n")

    # 5. El pedido progresa en la cocina y se entrega
    print("--- Progreso del Pedido 1 ---")
    pedido_1.actualizar_estado("listo_para_entregar")
    pedido_1.actualizar_estado("entregado")
    print(pedido_1) # Mostramos el estado final del pedido
    print("---------------------------\n")

    # 6. Un segundo cliente realiza otro pedido para demostrar los IDs únicos
    print("--- Nuevo Pedido de Cliente 2 ---")
    orden_cliente_2 = {
        hamburguesa: 1,
        gaseosa: 1
    }
    pedido_2 = Pedido(orden_cliente_2)
    print(pedido_2)
    pedido_2.procesar_pedido()
    print("---------------------------\n")
