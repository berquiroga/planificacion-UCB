# simulaciones/planta_control_comparacion.py
"""
IMT-221 — Laboratorio Intensivo Integrado (10-17 noviembre 2026)
Comparacion de lazo cerrado P vs PI vs PID filtrado sobre modelo de planta ILUSTRATIVO:
    Gp(s) = 2 / (20s + 1)
ADVERTENCIA DE TRAZABILIDAD:
Este script evalua un modelo matematico SINTETICO / ILUSTRATIVO.
No constituye identificacion experimental de una planta termica real.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# 1. Definicion del modelo de planta ilustrativo: Gp(s) = 2 / (20s + 1)
Kp_plant = 2.0
tau_plant = 20.0

# Vector de tiempo para simulacion (0 a 60 segundos)
t = np.linspace(0, 60, 1200)
dt = t[1] - t[0]

# 2. Funciones de transferencia lineales en lazo cerrado T(s) = L(s) / (1 + L(s))
# Caso P: Kc = 1.0 -> L(s) = 2 / (20s + 1) -> T_P(s) = 2 / (20s + 3)
sys_P = signal.TransferFunction([2.0], [20.0, 3.0])

# Caso PI nominal: Kc = 1.0, Ki = 0.05 -> C(s) = (20s + 1)/(20s) -> T_PI(s) = 1 / (10s + 1)
sys_PI = signal.TransferFunction([1.0], [10.0, 1.0])

# Caso PID con derivada filtrada: C(s) = Kc + Ki/s + Kd*s/(Tf*s + 1)
# Parametros declarados para comparacion: Kc = 1.8, Ki = 0.09, Kd = 2.0, Tf = 0.5 s
Kc_pid, Ki_pid, Kd_pid, Tf_pid = 1.8, 0.09, 2.0, 0.5
num_C = [Kc_pid * Tf_pid + Kd_pid, Kc_pid + Ki_pid * Tf_pid, Ki_pid]
den_C = [Tf_pid, 1.0, 0.0]
num_L = np.polymul(num_C, [Kp_plant])
den_L = np.polymul(den_C, [tau_plant, 1.0])
sys_PID = signal.TransferFunction(num_L, np.polyadd(den_L, num_L))

_, y_P = signal.step(sys_P, T=t)
_, y_PI = signal.step(sys_PI, T=t)
_, y_PID = signal.step(sys_PID, T=t)

# 3. Simulacion numerica por Euler del controlador PI CON saturacion de actuador (no lineal)
u_max = 0.8  # Limite ilustrativo de actuacion para demostrar efecto de saturacion/windup
y_sat = np.zeros_like(t)
u_sat = np.zeros_like(t)
u_lin = np.zeros_like(t)
y_lin = np.zeros_like(t)

integ_sat = 0.0
integ_lin = 0.0
Kc_pi, Ki_pi = 1.0, 0.05

for k in range(1, len(t)):
    # Lazo PI lineal sin saturacion
    e_lin = 1.0 - y_lin[k - 1]
    integ_lin += e_lin * dt
    u_lin[k] = Kc_pi * e_lin + Ki_pi * integ_lin
    dy_lin = (-y_lin[k - 1] + Kp_plant * u_lin[k]) / tau_plant
    y_lin[k] = y_lin[k - 1] + dy_lin * dt

    # Lazo PI con saturacion de mando en [0, u_max]
    e_sat = 1.0 - y_sat[k - 1]
    integ_sat += e_sat * dt
    u_cmd = Kc_pi * e_sat + Ki_pi * integ_sat
    u_sat[k] = np.clip(u_cmd, 0.0, u_max)
    dy_sat = (-y_sat[k - 1] + Kp_plant * u_sat[k]) / tau_plant
    y_sat[k] = y_sat[k - 1] + dy_sat * dt

print("=== RESUMEN DE METRICAS (MODELO SINTETICO ILUSTRATIVO) ===")
print(f"Control P   -> Valor final: {y_P[-1]:.4f}, Error est.: {1.0 - y_P[-1]:.4f}")
print(f"Control PI  -> Valor final: {y_PI[-1]:.4f}, Error est.: {1.0 - y_PI[-1]:.4f}")
print(f"Control PID -> Valor final: {y_PID[-1]:.4f}, Maximo: {np.max(y_PID):.4f}")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
ax1.plot(t, np.ones_like(t), 'k--', label='Referencia r(t) = 1')
ax1.plot(t, y_P, 'r-', label='Control P (Kc=1) [SIMULADO IDEAL]')
ax1.plot(t, y_PI, 'b-', label='Control PI lineal (Kc=1, Ki=0.05) [SIMULADO IDEAL]')
ax1.plot(t, y_PID, 'g-.', label='Control PID filtrado [SIMULADO IDEAL]')
ax1.plot(t, y_sat, 'm:', linewidth=2, label=f'PI con saturacion u <= {u_max} [SIMULADO]')
ax1.set_ylabel('Salida normalizada y(t)')
ax1.set_title('Comparacion P / PI / PID sobre Planta Ilustrativa Gp(s) = 2/(20s+1)')
ax1.grid(True)
ax1.legend(loc='lower right', fontsize=8)

ax2.plot(t, u_lin, 'b-', label='Accion u(t) PI lineal')
ax2.plot(t, u_sat, 'm--', label=f'Accion u(t) PI saturada (u_max={u_max})')
ax2.set_xlabel('Tiempo [s]')
ax2.set_ylabel('Accion de mando u(t)')
ax2.grid(True)
ax2.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.savefig('comparacion_control_ilustrativo.png', dpi=150)
plt.show()
