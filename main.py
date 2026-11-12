import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)

# Ejercicio 1
print("\n1. Gasto total por usuario:")

for usuario, compras in data.items():
    total = 0
    
    for compra in compras:
        total += compra["precio"]
        
    print(f"{usuario}: {total:.2f} €")
        
#Ejercicio 2

print("\n2. Cliente VIP (Mayor gasto):")   

mayor_gasto = 0
clinte_vip = ""  

for usuario, compras in data.items():
    total = 0
    
    for compra in compras:
        total += compra["precio"]
        
    if total > mayor_gasto:
        mayor_gasto = total
        cliente_vip = usuario
        
print(f"Cliente VIP: {cliente_vip}")
print(f"Gasto total: {mayor_gasto:.2f} €")
        

#Ejercicio 3

print("\n3. Cliente con más articulos:")

mayor_cantidad = 0
cliente_mas_articulos = ""

for usuario, compras in data.items():
    cantidad = len(compras)

    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        cliente_mas_articulos = usuario

print(f"Cliente: {cliente_mas_articulos}")
print(f"Cantidad de artículos: {mayor_cantidad}")


#Ejercicio 4

print("\n4. Producto más caro y más barato:")

producto_caro = None
producto_barato = None
usuario_caro = ""
usuario_barato = ""

for usuario, compras in data.items():
    for compra in compras:
        if producto_caro is None or compra["precio"] > producto_caro["precio"]:
            producto_caro = compra
            usuario_caro = usuario

        if producto_barato is None or compra["precio"] < producto_barato["precio"]:
            producto_barato = compra
            usuario_barato = usuario

print(f"Producto más caro: {producto_caro['producto']} - {producto_caro['precio']:.2f} € - Comprado por {usuario_caro}")
print(f"Producto más barato: {producto_barato['producto']} - {producto_barato['precio']:.2f} € - Comprado por {usuario_barato}")


#Ejercicio 5

print("\n5. Resumen por categorías:")

resumen_categorias = {}

for usuario, compras in data.items():
    for compra in compras:
        categoria = compra["categoria"]
        precio = compra["precio"]

        if categoria not in resumen_categorias:
            resumen_categorias[categoria] = 0

        resumen_categorias[categoria] += precio

for categoria, total in resumen_categorias.items():
    print(f"{categoria}: {total:.2f} €")
    

#Ejercicio 6

print("\n6. Productos con IVA:")

for usuario, compras in data.items():
    for compra in compras:
        compra["precioIVA"] = compra["precio"] * 1.21
        print(f"{compra['producto']}: {compra['precioIVA']:.2f} €")
        
        
#Ejercicio 7

import csv

print("\n7. Crear archivo contabilidad_a.csv:")

with open("contabilidad_a.csv", "w", newline="") as archivo:
    escritor = csv.writer(archivo)

    escritor.writerow(["producto", "precioIVA"])

    for usuario, compras in data.items():
        for compra in compras:
            escritor.writerow([compra["producto"], round(compra["precioIVA"], 2)])

print("Archivo contabilidad_a.csv creado correctamente.")

