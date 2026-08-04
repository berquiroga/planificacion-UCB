# Proyecto Final Integrador (PFI): Robótica IMT-342
**Universidad Católica Boliviana "San Pablo" — Sede Tarija**
**Docente:** M.Sc. Ing. Bernardo Quiroga Turdera

## Celda de Manufactura Flexible Inteligente
Repositorio oficial con los lineamientos, plantillas y rúbricas para el diseño, simulación e implementación de una celda de clasificación y paletizado autónomo por visión artificial utilizando el **ABB IRB 120**.

### 📌 Sobre las Entregas y el Tracking Automatizado
El seguimiento de este proyecto está automatizado. Cada equipo deberá hacer un *Fork* de este repositorio. Las entregas de los 4 Hitos se evaluarán directamente desde sus repositorios. 
Nuestro sistema en la nube (Python + Streamlit) leerá automáticamente sus *commits* mediante GitHub Actions y actualizará sus horas de avance y calificaciones en la base de datos de Google Sheets de la cátedra.

### ⚙️ Reglas de Control de Versiones (Git)
Se exige el uso de **Conventional Commits**:
* `feat(vision): agrega calibracion SVD`
* `fix(kinematics): corrige divergencia en singularidad de Pieper`

**Ramas obligatorias:**
* `main`: Código estable probado en el robot real.
* `dev`: Rama de integración continua.
* `feature/*`: Ramas para el desarrollo de cada hito (ej. `feature/urdf-model`).

⚠️ *Los commits masivos (ej. "subiendo todo el hito 3") de un solo golpe serán penalizados y no contabilizarán horas en el sistema.*

### 📂 Contenido de este Repositorio
* `/01_Guia_Oficial`: Pliego de especificaciones técnicas (Reglas, KPIs y WBS).
* `/02_Rubricas_y_Evaluacion`: Criterios de aprobación (Pasaportes) y matriz de pruebas metrológicas.
* `/03_Plantillas_Entregables`: Esqueleto en LaTeX para el artículo final formato IEEE.