import pandas as pd

# Cargar datos de ventas
df = pd.read_excel("ventas.xlsx")

# Calcular métricas
df["Total"] = df["Cantidad"] * df["Precio"]
ventas_totales = df["Total"].sum()
producto_mas_vendido = df.groupby("Producto")["Cantidad"].sum().idxmax()
promedio_ventas = df["Total"].mean()

# Guardar reporte
reporte = f"""
Reporte de Ventas 
--------------------------------
Ventas Totales: ${ventas_totales:,.2f}
Producto Más Vendido: {producto_mas_vendido}
Promedio de Ventas: ${promedio_ventas:,.2f}
"""
with open("reporte.txt", "w", encoding= "utf-8") as file:
    file.write(reporte)

print(reporte)
print("Reporte guardado en reporte.txt")
