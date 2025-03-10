import pandas as pd

# Datos de prueba
data = {
    "Fecha": ["2024-03-01", "2024-03-02", "2024-03-03"],
    "Producto": ["Laptop", "Mouse", "Teclado"],
    "Cantidad": [3, 10, 5],
    "Precio": [800, 25, 50]
}

df = pd.DataFrame(data)

df["Total"] = df["Cantidad"] * df["Precio"]

df.to_excel("ventas.xlsx", index=False)

print("Archivo ventas.xlsx creado exitosamente.")
