---
marp: true
theme: default
class: 
  - lead
paginate: true
backgroundColor: #f8f9fa
---

# Circuitos Electrónicos II (IMT-221)
## Semestre II-2026 | UCB Sede Tarija
**Docente:** M.Sc. Ing. Bernardo Quiroga Turdera

---

# Bienvenidos al Taller de Ingeniería
Esta asignatura no es una lista de temas teóricos para memorizar. 
Es el espacio donde construirán un **sistema de control analógico de precisión**, real e inmune al ruido industrial.

**Nuestra Meta:** Transición del análisis pasivo al control dinámico activo[cite: 1].

---

# Metodología de Trabajo

- **Enfoque "Python-First":** Procesamiento de datos experimentales, gráficos de Bode y análisis estadísticos mediante `numpy`, `scipy` y `matplotlib`[cite: 1].
- **Modelo F.I.V.E. para Laboratorios:**
  1. **F**undamentación (Modelos matemáticos)
  2. **I**mplementación (Hardware)
  3. **V**alidación (Contraste teoría vs. práctica)
  4. **E**videncia (Reporte técnico profesional)

---

# Sistema de Evaluación (100%)

### Evaluación Continua (50%)
- **EC1 (Sem 1-4):** Análisis CA, Impedancias y Bode pasivo. (Incluye Hito 1 PFI).
- **EC2 (Sem 5-17):** Op-Amps reales, Filtros, PID y Potencia. (Incluye Hitos 2 y 3 PFI).
- *Recuperatorios en Semana 5 y 17 para nivelación teórica.*

### Evaluación Final Híbrida (50%)
- **Componente A (40%):** Prueba de estrés grupal en vivo al prototipo físico.
- **Componente B (60%):** Examen individual de rediseño analítico sobre el hardware.

---

# Evaluación Diagnóstica
### Tiempo: 30 minutos

- Objetivo: Medir competencias previas. No tiene ponderación sumativa, pero es un requisito **obligatorio**.
- Áreas a evaluar:
  - Álgebra de números complejos.
  - Leyes de Kirchhoff en CC.
  - Dinámica de capacitores.
  - Parámetros de señales.

*(Proceder a la entrega de las hojas de evaluación)*

---

# Tema 1.1: Análisis Dinámico de CA
## Definición Matemática de una Señal Senoidal

$$v(t) = V_m \cos(\omega t + \phi)$$

- $V_m$: Amplitud pico de la señal [V].
- $\omega = 2\pi f$: Frecuencia angular [rad/s].
- $f = 1/T$: Frecuencia cíclica [Hz] (50 Hz nominal en Bolivia).
- $\phi$: Ángulo de fase [rad] o [°].

---

# El Valor Eficaz (RMS)
**Discusión:** *¿Por qué el multímetro marca 220 V si la señal oscila entre positivo y negativo?*

El valor eficaz es el equivalente en CC que entrega la **misma potencia promedio** a una resistencia pura $R$.

$$P_{avg} = \frac{1}{T} \int_{0}^{T} \frac{V_m^2}{R} \cos^2(\omega t + \phi) dt = \frac{V_m^2}{2R} = \frac{V_{RMS}^2}{R}$$

$$\therefore V_{RMS} = \frac{V_m}{\sqrt{2}} \approx 0.7071 \cdot V_m$$

**Ejemplo en Tarija:** Para $V_{RMS} = 220\text{ V}$, el pico es $V_m \approx 311.12\text{ V}$.

---

# Introducción a la Transformación Fasorial
Para evitar resolver ecuaciones diferenciales en el dominio del tiempo, aplicamos la **Identidad de Euler**:

$$e^{\pm j\theta} = \cos(\theta) \pm j\sin(\theta)$$

El **Fasor** ($\hat{V}$) captura la amplitud y la fase:

$$\hat{V} = V_m e^{j\phi} = V_m \angle \phi$$
$$\hat{V}_{RMS} = \frac{V_m}{\sqrt{2}} \angle \phi$$

---

# Próximos Pasos (Laboratorio Miércoles)

**Obligatorio para la próxima sesión (09:00 - 10:45):**
1. **Software:** Instalar LTSpice y entorno Python (3.10+).
2. **Lectura:** Capítulo 9 de Hayt & Kemmerly[cite: 1].
3. **Actividad:** Iniciaremos la simulación e instrumentación del Puente de Wheatstone en CA para el sensor térmico.