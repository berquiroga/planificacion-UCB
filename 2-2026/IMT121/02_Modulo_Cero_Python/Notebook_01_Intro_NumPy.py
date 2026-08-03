# %% [markdown]
# # Módulo Cero: Nivelación en Python y Álgebra Lineal
# ## Circuitos Electrónicos I (IMT-121)
# 
# El objetivo de este notebook es familiarizarnos con `NumPy`, la librería estándar 
# de la industria para computación científica. En electrónica, no calculamos sistemas 
# complejos a mano; modelamos la física y dejamos que el procesador invierta las matrices.

# %%
import numpy as np

# %% [markdown]
# ### 1. Declaración de Matrices (Topología del Circuito)
# Una matriz de conductancia (Análisis Nodal) o de resistencia (Análisis de Mallas) 
# se declara en NumPy como un arreglo bidimensional (lista de listas).

# %%
# Ejemplo: Matriz de Resistencia R (3x3) de un circuito de tres lazos
R = np.array([
    [12.0, -4.0, -8.0],
    [-4.0, 10.0, -2.0],
    [-8.0, -2.0, 15.0]
])

print("Matriz de Resistencia [R]:\n", R)
print("\nDimensión de la matriz:", R.shape)

# %% [markdown]
# ### 2. Declaración de Vectores (Fuentes de Excitación)
# Las fuentes de voltaje independientes se agrupan en un vector columna.

# %%
# Vector de Voltaje V (3x1)
V = np.array([
    [10.0],
    [0.0],
    [-5.0]
])

print("Vector de Fuentes de Tensión [V]:\n", V)

# %% [markdown]
# ### 3. Resolución del Sistema: R * I = V
# Para encontrar las corrientes de malla (Vector I), necesitamos despejar I.
# Analíticamente: I = R^(-1) * V
# Computacionalmente: NUNCA invertimos la matriz directamente por costo computacional.
# Usamos algoritmos de resolución optimizados como `np.linalg.solve()`.

# %%
# Resolución del sistema lineal
try:
    I = np.linalg.solve(R, V)
    
    print("=== Corrientes de Malla Calculadas ===")
    print(f"I1 = {I[0][0]:.4f} A")
    print(f"I2 = {I[1][0]:.4f} A")
    print(f"I3 = {I[2][0]:.4f} A")

except np.linalg.LinAlgError:
    print("Error: La matriz es singular (Determinante = 0). Revise la topología del circuito.")

# %% [markdown]
# ### 4. Comprobación del Error (Ingeniería Basada en Evidencia)
# Un buen ingeniero siempre verifica sus resultados. Si multiplicamos R por I, 
# deberíamos obtener V nuevamente. Evaluemos el residuo numérico.

# %%
V_calculado = np.dot(R, I)
# Verificamos si V_calculado es computacionalmente igual a V
residuo = np.allclose(V_calculado, V)

print("¿La solución cumple la Ley de Kirchhoff de Voltajes para todas las mallas?:", residuo)