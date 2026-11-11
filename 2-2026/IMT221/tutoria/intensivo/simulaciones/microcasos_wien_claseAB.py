# simulaciones/microcasos_wien_claseAB.py
"""
IMT-221 — Laboratorio Intensivo Integrado (10-17 noviembre 2026)
Microcasos conceptuales en simulacion (CP3B y CP4B):
1. Oscilador de Puente de Wien con ganancia A >= 3 y saturacion suave para estabilizar amplitud.
2. Comparacion matematica idealizada de distorsion de cruce por cero: Clase B vs Clase AB.
ADVERTENCIA: Modelos matematicos ilustrativos; no sustituyen analisis SPICE de transistores.
"""

import numpy as np
import matplotlib.pyplot as plt

# --- MICROCASO 1: Dinamica de arranque y limitacion no lineal en oscilador de Wien ---
R = 10e3
C = 10e-9
w0 = 1.0 / (R * C)
f0 = w0 / (2.0 * np.pi)

# Ecuacion diferencial de 2do orden de la red de Wien con ganancia no lineal A(v_b)
# v_out = A0 * v_b / (1 + (v_b / Vsat)^2), con A0 = 3.15 (> 3 para garantizar arranque)
A0 = 3.15
Vsat = 1.5
t_wien = np.linspace(0, 12e-3, 6000)
dt = t_wien[1] - t_wien[0]

x1 = np.zeros_like(t_wien)  # v_b(t)
x2 = np.zeros_like(t_wien)  # dv_b/dt
v_out_wien = np.zeros_like(t_wien)
x1[0] = 0.01  # Perturbacion inicial pequena (10 mV)

for k in range(len(t_wien) - 1):
    vb = x1[k]
    dvb = x2[k]
    # Ganancia instantanea con compresion no lineal suave
    A_inst = A0 / (1.0 + (vb / Vsat) ** 2)
    v_out_wien[k] = A_inst * vb
    # Dinamica: (1/w0^2)*d2vb/dt2 + ((3 - A_inst)/w0)*dvb/dt + vb = 0
    ddvb = -w0 * (3.0 - A_inst) * dvb - (w0 ** 2) * vb
    x1[k + 1] = vb + dvb * dt
    x2[k + 1] = dvb + ddvb * dt

# --- MICROCASO 2: Distorsion de cruce por cero (Clase B vs Clase AB) ---
t_ab = np.linspace(0, 2e-3, 1000)
v_in = 2.0 * np.sin(2.0 * np.pi * 1000.0 * t_ab)
V_dead = 0.65  # Zona muerta ilustrativa (~V_BE sin polarizar en Clase B)
V_bias = 0.58  # Polarizacion previa en Clase AB que reduce la zona muerta

v_claseB = np.where(np.abs(v_in) > V_dead, v_in - np.sign(v_in) * V_dead, 0.0)
dead_AB = max(0.0, V_dead - V_bias)
v_claseAB = np.where(np.abs(v_in) > dead_AB, v_in - np.sign(v_in) * dead_AB, 0.0)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
ax1.plot(t_wien * 1e3, v_out_wien, 'b-', label=f'Salida v_out(t) con A0={A0} y limitacion suave')
ax1.set_title(f'Microcaso CP3B: Arranque y Estabilizacion Ilustrativa de Wien (f0 = {f0:.1f} Hz)')
ax1.set_xlabel('Tiempo [ms]')
ax1.set_ylabel('Tension [V]')
ax1.grid(True)
ax1.legend(loc='upper left', fontsize=8)

ax2.plot(t_ab * 1e3, v_in, 'k--', label='Entrada sinusoidal ideal')
ax2.plot(t_ab * 1e3, v_claseB, 'r-', label='Salida Clase B (con distorsion de cruce)')
ax2.plot(t_ab * 1e3, v_claseAB, 'g-', label='Salida Clase AB (polarizada)')
ax2.set_title('Microcaso CP4B: Comparacion Conceptual Clase B vs Clase AB [ILUSTRATIVO]')
ax2.set_xlabel('Tiempo [ms]')
ax2.set_ylabel('Tension [V]')
ax2.grid(True)
ax2.legend(loc='upper right', fontsize=8)

plt.tight_layout()
plt.savefig('microcasos_wien_claseAB.png', dpi=150)
plt.show()
