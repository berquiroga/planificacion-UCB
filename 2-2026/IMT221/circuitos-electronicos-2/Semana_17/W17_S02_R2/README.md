# IMT-221 · W17-S02 — Recuperatorio 2 EC2 · Versión R2 (CircuiTikZ)

**Curso:** IMT-221 Circuitos Electrónicos II · UCB Sede Tarija  
**Fecha prevista:** miércoles 25 de noviembre de 2026  
**Fuentes:** `content-package(1).md` (Versión R2) y plantillas W17-S01 (`w17_s01_examen_EC2_A.tex`, `w17_s01_examen_EC2_B.tex`, `w17_s01_examen_EC2_formulario.tex`, `w17_s01_examen_EC2_solucionario.tex`).

## Estructura de artefactos

```text
W17_S02_R2/
├── student/
│   └── w17_s02_recuperatorio_EC2_R2_estudiantes.tex   # Cuadernillo estudiantil R2 con circuitikz/tikz/tcolorbox (sin clave)
├── instructor/
│   ├── w17_s02_recuperatorio_EC2_R2_solucionario.tex  # Solucionario y rúbrica R2 (CONFIDENCIAL DOCENTE)
│   ├── w17_s02_blueprint_equivalencia_A_R2.md         # Blueprint de equivalencia A → R2
│   └── w17_s02_instrucciones_aplicacion_R2.md         # Checklist de aplicación y acta de incidencias
├── MATRIZ_COBERTURA.md                                # Auditoría obligatoria de cobertura
└── README.md                                          # Este archivo
```

## Compilación y dependencias

Los archivos `.tex` reproducen el preámbulo exacto de W17-S01 (`tgpagella`, `tgcursor`, `babel[spanish, es-noshorthands]`, `tikz`, `circuitikz[american]`, `tcolorbox[most]`, `booktabs`, `tabularx`, `fancyhdr`, `lastpage`). Compilar con dos pasadas de `pdflatex` en Overleaf o TeX Live completo:

```bash
pdflatex -interaction=nonstopmode w17_s02_recuperatorio_EC2_R2_estudiantes.tex
pdflatex -interaction=nonstopmode w17_s02_recuperatorio_EC2_R2_estudiantes.tex
```

> **Limitación del entorno local:** `circuitikz`, `tikz`, `tcolorbox`, `lastpage` y `babel-spanish` no están preinstalados en el entorno local de compilación, por lo que esta versión `circuitikz` no fue compilada localmente a PDF; se verificó automáticamente el balanceo de llaves/entornos y la ausencia de filtraciones de clave.

## Puntos pendientes de confirmación antes de imprimir

1. Confirmar que el examen A realmente aplicado correspondió a `w17_s01_examen_EC2_A.tex` (`25/25/25/25`, `90 minutos`, `Calculadora: Válida`) y no a la Versión B (`30/30/30/10`, `105 minutos`).
2. Reutilizar sin cambios `formulario_EC2_IMT221.pdf` (`w17_s01_examen_EC2_formulario.tex`).
3. El puntaje de 100 es interno del instrumento; la ponderación global de EC2 corresponde a la decisión docente.
