---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #2b2b2b
color: #ffffff
---

# Guía Docente: Sesión 01
## Circuitos Electrónicos I (IMT-121)
**Fecha:** 3 de Agosto de 2026
**Duración:** 90 Minutos

---

## Bloque 1: Bienvenida y CDIO (00 - 15 min)
**Objetivo:** Establecer el tono de rigor y la metodología de la asignatura.
*   **Acción:** Dar la bienvenida oficial al Semestre II/2026. 
*   **Punto Clave:** Contrastar el aprendizaje pasivo vs. Ingeniería Basada en Evidencia.
*   **Concepto a introducir:** Mencionar brevemente los pilares de la Metodología MECA (Concebir, Diseñar, Implementar, Operar) enfocada en el diseño personalizado para la carrera.
*   *Nota mental:* Observar el lenguaje corporal. El objetivo es motivar, no intimidar con la carga de trabajo.

---

## Bloque 2: Proyecto Final Integrador (15 - 35 min)
**Objetivo:** Mostrar la meta final (Hardware Validado).
*   **Acción:** Proyectar el diagrama de bloques del PFI.
*   **Alineamiento Biomédica:** Enfatizar la supresión de ruido (50 Hz) y seguridad del paciente en adquisición EMG/ECG.
*   **Alineamiento Mecatrónica:** Enfatizar el acondicionamiento de galgas extensiométricas para lazos de control de fuerza.
*   *Pregunta detonante al grupo:* "¿De qué sirve un algoritmo de control perfecto si la señal analógica que recibe el ADC es puro ruido?"

---

## Bloque 3: El Puente Matricial (35 - 55 min)
**Objetivo:** Desmitificar el uso del Álgebra Lineal.
*   **Acción:** Explicar que Python y LTSpice harán el "trabajo sucio".
*   **Discurso:** "No necesitamos que sean teóricos puros del álgebra; necesitamos mecánicos matriciales operativos. Su trabajo es modelar la física."
*   **Punto Clave:** Mostrar la ecuación $\mathbf{A}\mathbf{x} = \mathbf{b}$. $\mathbf{A}$ es la topología (física), $\mathbf{x}$ son los voltajes/corrientes, $\mathbf{b}$ son las fuentes.

---

## Bloque 4: Ejercicio Diagnóstico (55 - 80 min)
**Objetivo:** Evaluación formativa silenciosa.
*   **Consigna:** Circuito de dos lazos. $V_s = 12\text{V}$, $R_1 = 100\Omega$, $R_2 = 220\Omega$, $R_3 = 330\Omega$.
*   **Solución Esperada:**
    1. LCK en el nodo: $\frac{V_1 - 12}{100} + \frac{V_1}{220} + \frac{V_1}{330} = 0$
    2. Reordenando: $V_1 \left( \frac{1}{100} + \frac{1}{220} + \frac{1}{330} \right) = \frac{12}{100}$
    3. Forma Matricial (Escalar): $V_1 \cdot (G_{11}) = I_{s1}$
*   **Cierre del ejercicio:** Mostrar cómo $\left( \frac{1}{100} + \frac{1}{220} + \frac{1}{330} \right)$ es simplemente la suma de las conductancias conectadas al nodo. ¡Es intuitivo!

---

## Bloque 5: Módulo Cero y Cierre (80 - 90 min)
**Objetivo:** Asignar trabajo asincrónico y herramientas.
*   **Acción:** Mostrar la plataforma de la universidad.
*   **Asignación:** Jupyter Notebook 1 y 2 (NumPy y Sistemas Lineales).
*   **Instalaciones:** Python 3.12 y LTSpice XVII.
*   **Lectura:** Alexander & Sadiku, Cap. 1 y 2.
*   **Despedida:** "Nos vemos el miércoles para llevar la teoría matricial a Python y LTSpice."