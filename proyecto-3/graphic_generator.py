import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("ventas.xlsx")

# Gráfico de ventas por producto
df.groupby("Producto")["Total"].sum().plot(kind="bar", figsize=(10,5), color="skyblue")
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas en $")
plt.xticks(rotation=45)
plt.savefig("ventas_reporte.png")
plt.show()
