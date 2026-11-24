# IMT-342 — Hito 3 Integrado (ECI-3/4): Colección de Artefactos LaTeX

**Asignatura:** IMT-342 — Robótica (Universidad Católica Boliviana "San Pablo" — Sede Tarija)  
**Entrega y defensa:** martes 24 de noviembre de 2026  
**Fuentes autoritativas:**
- `formato-minimo-informe-hito3-IMT342.md`
- `instrumento-unificado-evaluacion-hito3-IMT342.md`
- Convenciones visuales heredadas de: `criterios_unificados_validacion_hito3.tex`, `matriz_aceptacion_hito3.tex` y `anexo_campana_piloto_tolerancias_hito3.tex`.

---

## Estructura de la colección

```text
IMT342_Hito3/
├── student/
│   ├── imt342_hito3_plantilla_informe.tex          # Plantilla editable de informe técnico (cuerpo 3–5 págs. + anexos)
│   ├── imt342_hito3_plantilla_informe.pdf          # PDF compilado de referencia
│   ├── imt342_hito3_guia_defensa_estudiante.tex    # Guía imprimible de 1 página para preparación de defensa
│   └── imt342_hito3_guia_defensa_estudiante.pdf    # PDF compilado de referencia
├── instructor/
│   ├── imt342_hito3_instrumento_evaluacion_docente.tex  # Instrumento unificado de evaluación, rúbrica y acta
│   └── imt342_hito3_instrumento_evaluacion_docente.pdf  # PDF compilado de referencia
├── MATRIZ_COBERTURA.md                             # Auditoría obligatoria de cobertura de contenido
└── README.md                                       # Este archivo
```

---

## Decisiones de arquitectura y fidelidad visual

1. **Separación de audiencias y notas del renderer:**
   - La plantilla de informe (`imt342_hito3_plantilla_informe.tex`) está lista para que cada grupo complete los campos `[ ]` y compile su entrega en PDF sin arrastrar texto de preparación para la defensa ni las *Indicaciones para LaTeX Architect*.
   - La guía estudiantil de preparación para la defensa y el alcance del formato se entregaron como documento separado de 1 página (`imt342_hito3_guia_defensa_estudiante.tex`).
   - El instrumento docente (`imt342_hito3_instrumento_evaluacion_docente.tex`) es un formulario operativo imprimible con espacios de escritura, matriz Gate 0–4, rúbrica 100 pts (A–E), banco de preguntas, acta consolidada, registro de incidencias/bloqueos, checklist rápido y cautelas.
2. **Convenciones visuales preservadas:**
   - Tipografía institucional: `tgpagella` + `tgcursor` + `microtype` (UTF-8, T1).
   - Paleta oficial IMT-342: `ucbblue` (`RGB(0, 51, 102)`), `offcolor`, `readcolor`, `acccolor`, `movcolor`.
   - Encabezados y pies `fancyhdr` consistentes con los documentos previos del Hito 3.
3. **Portabilidad y compilación sin dependencias faltantes:**
   - Los archivos `.tex` son 100 % autocontenidos y compilan con `pdflatex` (o `lualatex`) estándar sin requerir `tcolorbox`, `tikz`, `enumitem` ni `babel-spanish` (`spanish.ldf`), utilizando cajas vectoriales nativas (`\ucbbox`), etiquetas en español explícitas y un diagrama esquemático nativo (`picture`) editable.

### Compilación

```bash
pdflatex -interaction=nonstopmode imt342_hito3_plantilla_informe.tex
pdflatex -interaction=nonstopmode imt342_hito3_plantilla_informe.tex
```

Repetir el mismo comando de dos pasadas para `imt342_hito3_guia_defensa_estudiante.tex` e `imt342_hito3_instrumento_evaluacion_docente.tex`.

---

## Detalles de implementación no resueltos y limitaciones de fuente (pendientes de confirmación docente)

Los siguientes elementos se preservaron explícitamente como **pendientes** o **propuestas operativas** sin inventar valores ni asumir aprobación formal:

1. **Aprobación formal de la rúbrica (`20/25/25/20/10`):** pendiente confirmar si fue aprobada y comunicada oficialmente al curso antes de puntuar.
2. **Desglose operativo del dominio E (`4 + 6` puntos):** 4 puntos grupales de documentación + 6 puntos de defensa individual siguen en estado de propuesta pendiente de confirmación.
3. **Umbrales y tolerancias numéricas (FK, IK, Jacobiano, singularidades, LSPB, tracking):** sujetos a campaña piloto y aprobación docente formal; no se incluyeron ni inventaron tolerancias del fabricante ABB.
4. **Regla uniforme ante bloqueos externos (`BA`) en el subcriterio de movimiento físico (4 pts en dominio C):** pendiente definición docente común para los grupos afectados por falta de autorización, licencia o acceso al hardware.
5. **Autorización de laboratorio (`GO/NO-GO`):** ninguno de los documentos generados concede permiso de operación física del ABB IRB120 / IRC5.
6. **Duración de defensa y ponderación distinta:** no se fijó duración ni nueva escala; prevalece la convocatoria y rúbrica aprobadas por el docente.
