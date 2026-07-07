import pandas as pd
import matplotlib.pyplot as plt

# ==========================================================
# SIMULADOR DE ANÁLISIS DE RIESGOS
# TFG - Clínica SaludNova
# ==========================================================

print("\n==============================================")
print("   SIMULADOR DE ANÁLISIS DE RIESGOS")
print("         Clínica SaludNova")
print("==============================================\n")

# ----------------------------------------------------------
# Cargar datos
# ----------------------------------------------------------

df = pd.read_csv("riesgos.csv", sep=";")

# ----------------------------------------------------------
# Cálculo de riesgos
# ----------------------------------------------------------

df["Riesgo_Inherente"] = (
    df["Probabilidad_Inicial"] *
    df["Impacto_Inicial"]
)

df["Riesgo_Residual"] = (
    df["Probabilidad_Residual"] *
    df["Impacto_Residual"]
)

# ----------------------------------------------------------
# Reducción obtenida
# ----------------------------------------------------------

df["Reduccion"] = (
    df["Riesgo_Inherente"] -
    df["Riesgo_Residual"]
)

df["Reduccion_%"] = (
    df["Reduccion"] /
    df["Riesgo_Inherente"] * 100
).round(2)

# ----------------------------------------------------------
# Clasificación automática
# ----------------------------------------------------------

def clasificar(valor):

    if valor >= 20:
        return "Crítico"

    elif valor >= 15:
        return "Alto"

    elif valor >= 8:
        return "Medio"

    else:
        return "Bajo"

df["Nivel_Inherente"] = df["Riesgo_Inherente"].apply(clasificar)
df["Nivel_Residual"] = df["Riesgo_Residual"].apply(clasificar)

# ----------------------------------------------------------
# Mostrar resultados
# ----------------------------------------------------------

print("============== MATRIZ DE RIESGOS ==============\n")

print(df[[
    "ID",
    "Riesgo",
    "Riesgo_Inherente",
    "Nivel_Inherente",
    "Riesgo_Residual",
    "Nivel_Residual",
    "Reduccion_%"
]])

# ----------------------------------------------------------
# Estadísticas
# ----------------------------------------------------------

print("\n==============================================")
print("RESUMEN DEL ANÁLISIS")
print("==============================================")

print(f"Total de riesgos analizados: {len(df)}")

print(
    f"Riesgo medio inicial: "
    f"{df['Riesgo_Inherente'].mean():.2f}"
)

print(
    f"Riesgo medio residual: "
    f"{df['Riesgo_Residual'].mean():.2f}"
)

print(
    f"Reducción media: "
    f"{df['Reduccion_%'].mean():.2f}%"
)

print(
    f"Mayor riesgo detectado: "
    f"{df['Riesgo_Inherente'].max()}"
)

print(
    f"Menor riesgo residual: "
    f"{df['Riesgo_Residual'].min()}"
)

# ----------------------------------------------------------
# Riesgos críticos
# ----------------------------------------------------------

criticos = len(df[df["Nivel_Inherente"] == "Crítico"])
altos = len(df[df["Nivel_Inherente"] == "Alto"])
medios = len(df[df["Nivel_Inherente"] == "Medio"])
bajos = len(df[df["Nivel_Inherente"] == "Bajo"])

print("\nDistribución de riesgos:")

print(f"Críticos : {criticos}")
print(f"Altos    : {altos}")
print(f"Medios   : {medios}")
print(f"Bajos    : {bajos}")

# ----------------------------------------------------------
# Guardar resultados
# ----------------------------------------------------------

df.to_csv(
    "riesgos_resultado.csv",
    sep=";",
    index=False
)

print("\nArchivo riesgos_resultado.csv generado correctamente.")
# ==========================================================
# GRÁFICO 1 - COMPARACIÓN DE RIESGO
# ==========================================================

plt.figure(figsize=(11,6))

x = range(len(df))

plt.bar(
    [i-0.2 for i in x],
    df["Riesgo_Inherente"],
    width=0.4,
    label="Riesgo inherente"
)

plt.bar(
    [i+0.2 for i in x],
    df["Riesgo_Residual"],
    width=0.4,
    label="Riesgo residual"
)

plt.xticks(x, df["ID"])

plt.xlabel("Riesgos")

plt.ylabel("Nivel de riesgo")

plt.title("Comparación entre riesgo inherente y riesgo residual")

plt.grid(axis="y")

plt.legend()

plt.tight_layout()

plt.savefig("barras.png", dpi=300)

plt.close()

print("✓ Gráfico de barras generado.")

# ==========================================================
# MATRIZ DE RIESGOS (HEATMAP)
# ==========================================================

import numpy as np

plt.figure(figsize=(8,8))

# Fondo de colores de la matriz

matriz = np.array([
    [1,1,2,2,3],
    [1,2,2,3,3],
    [2,2,3,3,4],
    [2,3,3,4,4],
    [3,3,4,4,4]
])

plt.imshow(
    matriz,
    origin="lower",
    cmap="RdYlGn_r",
    extent=[0.5,5.5,0.5,5.5]
)

# Pequeños desplazamientos para evitar solapamientos

offset = {
    "R1":(-0.10,0.10),
    "R2":(0.10,-0.10),
    "R3":(0.10,0.10),
    "R4":(-0.10,-0.10),
    "R5":(0.10,0),
    "R6":(-0.10,0),
    "R7":(0,0.10),
    "R8":(0,-0.10),
    "R9":(0.10,0.10),
    "R10":(-0.10,0.10)
}

for _, fila in df.iterrows():

    dx, dy = offset.get(fila["ID"], (0,0))

    x = fila["Probabilidad_Inicial"] + dx
    y = fila["Impacto_Inicial"] + dy

    plt.scatter(
        x,
        y,
        s=fila["Riesgo_Inherente"]*25,
        color="black",
        edgecolors="white"
    )

    plt.text(
        x,
        y,
        fila["ID"],
        fontsize=8,
        color="white",
        ha="center",
        va="center",
        fontweight="bold"
    )

plt.title("Matriz de riesgos inherentes")

plt.xlabel("Probabilidad")

plt.ylabel("Impacto")

plt.xticks([1,2,3,4,5])
plt.yticks([1,2,3,4,5])

plt.grid(color="black", linewidth=1)

plt.tight_layout()

plt.savefig("heatmap.png", dpi=300)

plt.close()

print("✓ Matriz de riesgos generada.")

# ==========================================================
# GRÁFICO DE REDUCCIÓN PORCENTUAL
# ==========================================================

plt.figure(figsize=(11,6))

plt.bar(
    df["ID"],
    df["Reduccion_%"]
)

plt.xlabel("Riesgos")

plt.ylabel("Reducción (%)")

plt.title("Reducción porcentual obtenida tras aplicar los controles")

plt.ylim(0,100)

plt.grid(axis="y")

plt.tight_layout()

plt.savefig("reduccion.png", dpi=300)

plt.close()

print("✓ Gráfico de reducción generado.")

# ==========================================================
# TOP 3 RIESGOS MÁS IMPORTANTES
# ==========================================================

print("\n==============================================")
print("TOP 3 RIESGOS MÁS CRÍTICOS")
print("==============================================")

top = df.sort_values(
    by="Riesgo_Inherente",
    ascending=False
).head(3)

for _, fila in top.iterrows():

    print(
        f"{fila['ID']} | "
        f"{fila['Riesgo']} | "
        f"Inicial={fila['Riesgo_Inherente']} | "
        f"Residual={fila['Riesgo_Residual']} | "
        f"Reducción={fila['Reduccion_%']}%"
    )

# ==========================================================
# RESUMEN FINAL
# ==========================================================

riesgo_total_inicial = df["Riesgo_Inherente"].sum()

riesgo_total_residual = df["Riesgo_Residual"].sum()

reduccion_global = (
    (riesgo_total_inicial-riesgo_total_residual)
    /riesgo_total_inicial
)*100

print("\n==============================================")
print("RESULTADOS GLOBALES")
print("==============================================")

print(f"Riesgo total inicial: {riesgo_total_inicial}")

print(f"Riesgo total residual: {riesgo_total_residual}")

print(f"Reducción global: {reduccion_global:.2f}%")

print("\nSimulación completada correctamente.")

print("\nArchivos generados:")

print(" - riesgos_resultado.csv")

print(" - barras.png")

print(" - heatmap.png")

print(" - reduccion.png")