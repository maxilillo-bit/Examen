productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False]
}

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3]
}
def buscar_codigo(codigo):
    codigo = codigo.upper()
    for c in productos:
        if c.upper() == codigo:
            return c
    return None

def unidades_categoria(categoria):
    total = 0
    categoria = categoria.lower()

    for codigo, datos in productos.items():
        if datos[1].lower() == categoria:
            total += stock[codigo][1]

    print("El total de unidades disponibles es:", total)

def busqueda_precio(p_min, p_max):
    lista = []

    for codigo, datos in stock.items():
        precio = datos[0]
        unidades = datos[1]

        if p_min <= precio <= p_max and unidades > 0:
            nombre = productos[codigo][0]
            lista.append(nombre + "--" + codigo)

    lista.sort()

    if len(lista) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        print("Los productos encontrados son:", lista)

def actualizar_precio(codigo, nuevo_precio):
    cod = buscar_codigo(codigo)

    if cod is None:
        return False

    stock[cod][0] = nuevo_precio
    return True

def agregar_producto(codigo, nombre, categoria, marca, peso,
                     importado, cachorro, precio, unidades):

    if buscar_codigo(codigo) is not None:
        return False

    productos[codigo] = [nombre, categoria, marca,
                         peso, importado, cachorro]

    stock[codigo] = [precio, unidades]

    return True

def eliminar_producto(codigo):
    cod = buscar_codigo(codigo)

    if cod is None:
        return False

    del productos[cod]
    del stock[cod]

    return True
def validar_codigo(codigo):
    return codigo.strip() != ""

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_categoria(categoria):
    return categoria.strip() != ""

def validar_marca(marca):
    return marca.strip() != ""

def validar_peso(peso):
    return peso > 0

def validar_importado(valor):
    return valor.lower() in ["s", "n"]

def validar_cachorro(valor):
    return valor.lower() in ["s", "n"]

def validar_precio(precio):
    return precio > 0

def validar_unidades(unidades):
    return unidades >= 0

while True:

    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")

    opcion = input("Ingrese opción: ")

    if opcion == "1":
        categoria = input("Ingrese categoria a consultar: ")
        unidades_categoria(categoria)

    elif opcion == "2":

        while True:
            try:
                minimo = int(input("Ingrese precio minimo: "))
                maximo = int(input("Ingrese precio maximo: "))
                break
            except:
                print("Debe ingresar valores enteros")

        busqueda_precio(minimo, maximo)

    elif opcion == "3":

        while True:

            codigo = input("Ingrese codigo del producto: ")

            while True:
                try:
                    precio = int(input("Ingrese nuevo precio: "))
                    if precio > 0:
                        break
                    else:
                        print("El precio debe ser mayor que cero")
                except:
                    print("Debe ingresar un numero entero")

            if actualizar_precio(codigo, precio):
                print("Precio actualizado")
            else:
                print("El codigo no existe")

            seguir = input("Desea actualizar otro precio (s/n)?: ").lower()

            if seguir == "n":
                break

    elif opcion == "4":

        codigo = input("Ingrese codigo del producto: ")

        if not validar_codigo(codigo):
            print("Codigo invalido")
            continue

        nombre = input("Ingrese nombre: ")

        if not validar_nombre(nombre):
            print("Nombre invalido")
            continue

        categoria = input("Ingrese categoria: ")

        if not validar_categoria(categoria):
            print("Categoria invalida")
            continue

        marca = input("Ingrese marca: ")

        if not validar_marca(marca):
            print("Marca invalida")
            continue

        try:
            peso = float(input("Ingrese peso (kg): "))
        except:
            print("Peso invalido")
            continue

        if not validar_peso(peso):
            print("Peso invalido")
            continue

        importado = input("¿Es importado? (s/n): ")

        if not validar_importado(importado):
            print("Valor invalido")
            continue

        cachorro = input("¿Es para cachorro? (s/n): ")

        if not validar_cachorro(cachorro):
            print("Valor invalido")
            continue

        try:
            precio = int(input("Ingrese precio: "))
        except:
            print("Precio invalido")
            continue

        if not validar_precio(precio):
            print("Precio invalido")
            continue

        try:
            unidades = int(input("Ingrese unidades: "))
        except:
            print("Unidades invalidas")
            continue

        if not validar_unidades(unidades):
            print("Unidades invalidas")
            continue

        if agregar_producto(
                codigo.upper(),
                nombre,
                categoria,
                marca,
                peso,
                importado.lower() == "s",
                cachorro.lower() == "s",
                precio,
                unidades):

            print("Producto agregado")
        else:
            print("El codigo ya existe")

    elif opcion == "5":

        codigo = input("Ingrese codigo del producto: ")

        if eliminar_producto(codigo):
            print("Producto eliminado")
        else:
            print("El codigo no existe")

    elif opcion == "6":
        print("Programa finalizado")
        break

    else:
        print("Debe seleccionar una opcion válida")