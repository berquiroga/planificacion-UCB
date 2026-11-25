# Blueprint de Equivalencia A → R2 — IMT-221 · W17-S02 · Recuperatorio 2 EC2

**Audiencia:** Exclusivo docente (no público antes de aplicar R2)  
**Fecha prevista:** miércoles 25 de noviembre de 2026  
**Cotejo realizado contra:** `w17_s01_examen_EC2_A.tex` (25/25/25/25 = 100 pts, 90 min, `Calculadora: Válida`) y `w17_s01_examen_EC2_B.tex` (30/30/30/10 = 100 pts, 105 min).

## Cambio de estructura sin aumentar nivel

| Competencia (25 pts) | Examen A (`w17_s01_examen_EC2_A.tex`) | Recuperatorio R2 (`w17_s02_recuperatorio_EC2_R2_estudiantes.tex`) | Por qué no es repetición |
|---|---|---|---|
| **Op-amp real** | No inversor ($A_{CL}=11$); ganancia, BW, SR, excursión, pico SR máx. | **Inversor** ($A_v=-4$, $\mathrm{NG}=5$); evaluar **dos frecuencias** ($10$ y $40\,\mathrm{kHz}$) y recomendar límite $f_{\max,\mathrm{SR}}$ | Cambia topología y tarea central de diagnóstico |
| **In-Amp / CMRR** | Ganancias $A_d, A_{cm}$ dadas; calcular salida y CMRR | Ensayos D y C dados; **inferir** $A_d, A_{cm}$, CMRR y predecir tercera condición | Invierte dirección del problema |
| **Rectificación** | Calcular picos para dos amplitudes y llenar tabla de estados | **Identificar circuitos** desde 6 muestras; calcular $E_{\mathrm{MAE}}$ discreto; analizar anomalía en muestra 2 | Exige interpretación de evidencia y métrica |
| **Filtro 2.º orden (Lab 6)** | Coeficientes de $H(s)$ y evaluación directa en $H(j\omega_0)$ | $H(s)$ **factorizada**, lectura de tabla de magnitudes y refutación de dos afirmaciones técnicas (I y II) | Auditoría crítica sin repetir cálculo idéntico |

## Control de equivalencia real (A vs. B)

- `w17_s01_examen_EC2_A.tex` confirma el reparto **25/25/25/25 (100 pts)** con `Duración: 90 minutos` y `Calculadora: Válida`.
- Si la versión efectivamente impresa en W17-S01 fue la **Versión B** (`30/30/30/10` con P4-B introductoria y `105 minutos`), R2 (`25/25/25/25`) no es automáticamente equivalente y el docente debe decidir el ajuste antes de imprimir.
- Se reutiliza literalmente `w17_s01_examen_EC2_formulario.tex` / `formulario_EC2_IMT221.pdf` sin modificaciones.
