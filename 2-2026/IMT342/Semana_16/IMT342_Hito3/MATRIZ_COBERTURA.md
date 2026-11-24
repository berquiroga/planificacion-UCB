# Matriz de Cobertura de Contenido — IMT-342 Hito 3 Integrado

Auditoría obligatoria comparando los paquetes fuente (`formato-minimo-informe-hito3-IMT342.md` e `instrumento-unificado-evaluacion-hito3-IMT342.md`) contra los artefactos LaTeX generados.

## 1. Cobertura de `formato-minimo-informe-hito3-IMT342.md`

| Contenido del paquete fuente | Artefacto destino | Ubicación (sección / elemento) | Estado |
|---|---|---|---|
| Metadatos de entrega (24/11/2026, PDF 3–5 págs., alcance, estado) | `student/imt342_hito3_plantilla_informe.tex` | Encabezado y caja *Condiciones de entrega y alcance* | Completo |
| Regla principal de evidencia (simulación $\neq$ IRC5 $\neq$ comando $\neq$ movimiento $\neq$ seguridad) | `student/imt342_hito3_plantilla_informe.tex` y `student/imt342_hito3_guia_defensa_estudiante.tex` | Caja *Regla principal de evidencia* | Completo |
| Portada (7 campos editables `[ ]`) | `student/imt342_hito3_plantilla_informe.tex` | Sección *Portada del Proyecto* (tabla) | Completo |
| Sec. 1: Objetivo técnico, resultado demostrado, tabla Gate 0–4 y nota sobre «Verificado» | `student/imt342_hito3_plantilla_informe.tex` | Sección 1 | Completo |
| Sec. 2: Diagrama esquemático (comando vs. estado; línea discontinua no probada) | `student/imt342_hito3_plantilla_informe.tex` | Sección 2, Figura 1 (`fig:arquitectura`) | Completo |
| Sec. 2: Tabla de manifiesto de comparabilidad (7 filas) y limitación de comparabilidad | `student/imt342_hito3_plantilla_informe.tex` | Sección 2 (tabla + campo editable) | Completo |
| Sec. 3.1: Lectura del IRC5 y comunicación ROS (4 campos) | `student/imt342_hito3_plantilla_informe.tex` | Subsección 3.1 | Completo |
| Sec. 3.2: Tabla de pruebas `FK-01`, `IK-01`, `J-01`, `S-01` | `student/imt342_hito3_plantilla_informe.tex` | Subsección 3.2 (tabla) | Completo |
| Sec. 3.2: Ecuaciones mínimas $e_p$ y $R_{\mathrm{err}}, e_R$ | `student/imt342_hito3_plantilla_informe.tex` | Subsección 3.2, Ecuaciones (1)–(2) | Completo |
| Sec. 3.2: Reglas sobre IK (ramas), Jacobiano (bloques/FD), singularidad y criterio de aceptación (sin inventar tolerancias ABB) | `student/imt342_hito3_plantilla_informe.tex` | Subsección 3.2 | Completo |
| Sec. 3.3: Tabla de niveles de evidencia de trayectoria/movimiento y nota de movimiento físico / `NO EJECUTADO` / `BLOQUEADO` | `student/imt342_hito3_plantilla_informe.tex` | Subsección 3.3 | Completo |
| Sec. 4: Análisis crítico y limitaciones (4 puntos numerados) | `student/imt342_hito3_plantilla_informe.tex` | Sección 4 | Completo |
| Sec. 5: Conclusiones y siguiente paso (3 ítems) | `student/imt342_hito3_plantilla_informe.tex` | Sección 5 | Completo |
| Anexos y evidencias (tabla E-01..E-03 y nota de confidencialidad de red/credenciales) | `student/imt342_hito3_plantilla_informe.tex` | Sección *Anexos y evidencias* (página separada) | Completo |
| Preparación para defensa — guía estudiantil (6 puntos + nota de sustento y alcance) | `student/imt342_hito3_guia_defensa_estudiante.tex` | Documento completo (1 página) | Completo |
| Fuente y alcance del formato | `student/imt342_hito3_guia_defensa_estudiante.tex` | Caja inferior *Fuente y alcance del formato* | Completo |
| Indicaciones para LaTeX Architect (separadas del contenido estudiantil) | `README.md` | Sección *Decisiones de arquitectura y fidelidad visual* | Completo |

## 2. Cobertura de `instrumento-unificado-evaluacion-hito3-IMT342.md`

| Contenido del paquete fuente | Artefacto destino | Ubicación (sección / elemento) | Estado |
|---|---|---|---|
| Encabezado, fecha (24/11/2026), estado de propuesta (20/25/25/20/10) y separación curricular (50 % EC vs. final) | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Encabezado y caja *Estado editorial* | Completo |
| Sec. 1: Ficha del grupo (11 campos) y Declaración de alcance al comenzar | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 1 | Completo |
| Sec. 2: Matriz de evidencia por Gate (0, 1, 2a–2e, 3a–3b, 4), estados V/P/F/NE/BA y claves de evidencia | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 2 | Completo |
| Sec. 3: Nota de uso de rúbrica y dominios A (20), B (25), C (25), D (20), E (10: 4+6) con notas de equidad y seguridad | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 3 (Subsecciones A–E) | Completo |
| Sec. 3: Guía de niveles (100 %, $\approx$75 %, $\approx$50 %, $\approx$25 %, 0 %) y distinción NE/BA | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 3 (*Guía de niveles*) | Completo |
| Sec. 4: Banco de preguntas de defensa individual (8 ejes) y tabla de registro por estudiante (4 filas imprimibles) | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 4 | Completo |
| Sec. 5: Acta consolidada (tablas grupal /94 e individual /100) y ecuaciones $N_{H3,i}$ y $EC$ | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 5, Ecuaciones (1)–(2) | Completo |
| Sec. 6: Registro de incidencias, bloqueos de ejecución física, estado de calificación, devolución y firma docente | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 6 | Completo |
| Sec. 7: Checklist rápido del docente para hoy (8 ítems con casillas) | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 7 | Completo |
| Sec. 8: Fuentes y cautelas de aplicación (4 fuentes + 4 puntos a confirmar por el docente) | `instructor/imt342_hito3_instrumento_evaluacion_docente.tex` | Sección 8 | Completo |
