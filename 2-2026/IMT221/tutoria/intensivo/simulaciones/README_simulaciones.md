# Guía de Archivos de Simulación (`simulaciones/`)

1. **`condicionador_ideal_dc.cir`**: Netlist SPICE con amplificador controlado ideal (`EAMP`) para verificar la ganancia $A_v = 1 + R_f/R_g = 3$. No posee rieles de alimentación ni modela saturación o Slew Rate.
2. **`filtro_sk_ideal_ac.cir`**: Netlist SPICE del filtro Sallen-Key de 2.º orden ($R_1=R_2=16\,\text{k}\Omega, C_1=C_2=100\,\text{nF}, R_g=10\,\text{k}\Omega, R_f=5.9\,\text{k}\Omega$). Graficar siempre `V(out)/V(in)`.
3. **`filtro_sk_ideal_trans.cir`**: Simulación transitoria del mismo filtro Sallen-Key excitado por la suma de una señal útil de $10\,\text{Hz}$ y una perturbación de $1000\,\text{Hz}$.
4. **`wien_red_ac.cir`**: Barrido AC de la red pasiva puente de Wien ($R=10\,\text{k}\Omega, C=10\,\text{nF}$) para verificar frecuencia de fase cero y atenuación $|\beta(j\omega_0)| = 1/3$.
5. **`planta_control_comparacion.py`**: Script en Python (`numpy`, `scipy`, `matplotlib`) que compara lazo cerrado P, PI y PID filtrado sobre la planta ilustrativa $G_p(s) = 2/(20s+1)$, incluyendo el efecto no lineal de saturación del actuador.
6. **`microcasos_wien_claseAB.py`**: Script en Python que ilustra numéricamente la necesidad de no linealidad para estabilizar la amplitud del oscilador de Wien y el efecto de la zona muerta en etapas Clase B frente a Clase AB.
