# ==============================================================================
# SCRIPT DE PLANTILLA: ANÁLISIS DE RECTAS DE CARGA DC Y PUNTO Q
# Asignatura: Circuitos Electrónicos III
# Universidad Católica Boliviana (UCB) - Sede Tarija
# ==============================================================================
#
# Propósito:
#   Este script permite simular de forma interactiva y graficar la recta de
#   carga DC de un transistor BJT tipo NPN de silicio. Ilustra de manera
#   clara los conceptos de:
#     1. TRASLACIÓN: Al cambiar el voltaje de la fuente Vcc (pendientes paralelas).
#     2. ROTACIÓN: Al cambiar la resistencia de colector Rc (cambio de pendiente).
#
# Instrucciones para los estudiantes:
#   1. Copia este script en un archivo de Python (.py) o en una celda de su 
#      Jupyter Notebook (.ipynb).
#   2. Si utiliza Jupyter, comente la línea "matplotlib.use('Agg')" para ver 
#      el gráfico interactivo en pantalla.
#   3. Ajuste los parámetros de diseño (R_c, V_cc, R_b, beta) para validar
#      sus propios cálculos analíticos antes de entrar al laboratorio.
# ==============================================================================

import numpy as np
import matplotlib
# Descomentar la siguiente línea si se ejecuta como script sin entorno gráfico (headless):
# matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns

# 1. ESTILO DE GRAFICACIÓN PROFESIONAL
sns.set_theme(style="whitegrid", context="talk", palette="colorblind")

# 2. PARÁMETROS NOMINALES DEL TRANSISTOR BJT (Silicio estándar)
beta = 100         # Ganancia de corriente nominal en región activa
V_be = 0.7         # Voltaje de encendido base-emisor (V)
R_b = 470e3        # Resistencia de base (Ohms) - Fijada en 470 kΩ

def calcular_punto_q(V_cc, R_c):
    """
    Calcula el punto de operación Q (Ic, Vce) y verifica la región de operación.
    """
    # Corriente de base (fijada por la malla de entrada)
    I_b = (V_cc - V_be) / R_b
    
    # Suposición inicial: Región Activa
    I_c_activa = beta * I_b
    V_ce_activa = V_cc - I_c_activa * R_c
    
    # Límite físico de saturación
    V_ce_sat = 0.2
    I_c_sat = (V_cc - V_ce_sat) / R_c
    
    if V_ce_activa < V_ce_sat:
        # Si el cálculo arroja un voltaje por debajo de sat, el BJT se ha saturado
        return I_b, I_c_sat, V_ce_sat, "Saturación"
    else:
        # De lo contrario, la hipótesis activa es correcta
        return I_b, I_c_activa, V_ce_activa, "Activa"

# 3. CONFIGURACIÓN DE LOS TRES ESCENARIOS CLAVE DE CLASE
# Estructura: (Voltaje_Fuente_Vcc, Resistencia_Colector_Rc, Etiqueta_Gráfico)
escenarios = [
    (10, 2000, "Original: $V_{CC}=10V$, $R_C=2k\\Omega$"),
    (15, 2000, "Traslación: $V_{CC}=15V$, $R_C=2k\\Omega$ (Paralela)"),
    (10, 1000, "Rotación: $V_{CC}=10V$, $R_C=1k\\Omega$ (Inclinada)")
]

# Inicializar figura de matplotlib
fig, ax = plt.subplots(figsize=(11, 7.5))

# 4. BUCLE DE GRAFICACIÓN PARA CADA ESCENARIO
for V_cc, R_c, label in escenarios:
    
    # A. Extremos de la recta de carga para trazado
    # Extremo 1: Corte (Ic = 0) -> Vce = Vcc
    # Extremo 2: Saturación Ideal (Vce = 0) -> Ic = Vcc / Rc
    v_ce_ejes = np.array([0, V_cc])
    i_c_ejes = (V_cc - v_ce_ejes) / R_c * 1000  # Convertir Ic a miliamperios (mA)
    
    # Trazar la recta de carga correspondiente
    linea, = ax.plot(v_ce_ejes, i_c_ejes, label=label, linewidth=3)
    
    # B. Cálculo exacto del Punto Q para este escenario
    ib, ic, vce, region = calcular_punto_q(V_cc, R_c)
    ic_mA = ic * 1000
    ib_uA = ib * 1e6
    
    # Graficar el Punto Q físico sobre la recta
    ax.plot(vce, ic_mA, 'o', color=linea.get_color(), markersize=11, 
            markeredgecolor='black', markeredgewidth=1.5, zorder=5)
    
    # C. Anotación descriptiva de texto con llamada (Callout)
    ax.annotate(
        f"Q: ({vce:.2f} V, {ic_mA:.2f} mA)\n$I_B$: {ib_uA:.1f} $\\mu$A\nRegión: {region}",
        xy=(vce, ic_mA),
        xytext=(vce + 0.4, ic_mA + 0.35),
        fontsize=10,
        fontweight='bold',
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=linea.get_color(), lw=1.5, alpha=0.9),
        arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=0.1", color=linea.get_color(), lw=1.5),
        zorder=6
    )

# 5. EMBELLECIMIENTO Y LÍMITES DEL GRÁFICO
ax.set_title("Comportamiento del Punto Q: Traslación ($V_{CC}$) vs Rotación ($R_C$)", 
             fontsize=15, fontweight='bold', pad=20)
ax.set_xlabel("Voltaje Colector-Emisor $V_{CE}$ (V)", fontsize=13, labelpad=10)
ax.set_ylabel("Corriente de Colector $I_C$ (mA)", fontsize=13, labelpad=10)
ax.set_xlim(0, 16)
ax.set_ylim(0, 11)

# Resaltar en color rojo la Zona de Saturación física (Vce < 0.2V)
ax.axvspan(0, 0.2, color='red', alpha=0.08, label="Límite de Saturación ($V_{CE} < 0.2$ V)")

# Ajustes de grilla y leyendas
ax.legend(loc="upper right", frameon=True, facecolor="white", edgecolor="none", shadow=True)
sns.despine()
plt.tight_layout()

# Guardar imagen resultante automáticamente
plt.savefig("comparativa_rectas_carga_estudiantes.png", dpi=150, bbox_inches='tight')
print("\n>>> ¡Gráfico 'comparativa_rectas_carga_estudiantes.png' guardado exitosamente!")
print(">>> Copie y ejecute este archivo para que sus estudiantes experimenten en clase.\n")
plt.close()
