transacciones = [
    ("2024-01-10", "Ana", "deposito", 5000, "MXN"),
    ("2024-01-12", "Luis", "retiro", 1500, "MXN"),
    ("2024-01-15", "Ana", "retiro", 2000, "MXN"),
    ("2024-01-18", "Carlos", "deposito", 7000, "MXN")
]

balances = {}

for fecha, cliente, tipo, monto, moneda in transacciones:

    if cliente not in balances:
        balances[cliente] = 0

    if tipo == "deposito":
        balances[cliente] += monto
    elif tipo == "retiro":
        balances[cliente] -= monto

print("Balances finales por cliente:")
print(balances)

cliente_mayor = max(balances, key=lambda x: balances[x])

nombre, balance = cliente_mayor, balances[cliente_mayor]

print("\nCliente con mayor balance:")
print(nombre, "con", balance, "MXN")
