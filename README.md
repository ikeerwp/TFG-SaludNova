# Análisis y Gestión de Riesgos de Ciberseguridad en una Clínica Sanitaria mediante NIST SP 800-30

## Trabajo Fin de Grado

Este repositorio contiene el desarrollo completo del Trabajo Fin de Grado centrado en el análisis y gestión de riesgos de ciberseguridad aplicado a una organización sanitaria ficticia denominada **SaludNova**.

El proyecto combina una memoria académica desarrollada en LaTeX junto con una pequeña validación práctica mediante Python para demostrar la aplicación de la metodología seleccionada.

---

# Objetivos

Los objetivos principales del trabajo son:

- Analizar los activos críticos de una clínica sanitaria.
- Identificar amenazas y vulnerabilidades relevantes.
- Evaluar los riesgos mediante la metodología NIST SP 800-30.
- Diseñar un plan de tratamiento basado en controles de seguridad.
- Validar la metodología mediante una simulación desarrollada en Python.

---

# Tecnologías utilizadas

- LaTeX
- Python 3
- Pandas
- Matplotlib
- Excel (CSV)

---

# Estructura del proyecto

```
TFG/
│
├── riesgos.csv
├── riesgos_resultado.csv
├── simulador.py
├── barras.png
├── heatmap.png
├── reduccion.png
└── README.md
```

---

# Simulación desarrollada

La parte práctica implementa un pequeño simulador que:

- Lee los riesgos desde un archivo CSV.
- Calcula automáticamente el riesgo inherente.
- Calcula el riesgo residual tras aplicar controles.
- Obtiene el porcentaje de reducción conseguido.
- Genera estadísticas descriptivas.
- Produce automáticamente gráficos para la memoria:
  - Comparativa de riesgos inherentes y residuales.
  - Mapa de calor de riesgos.
  - Reducción porcentual del riesgo.

---

# Metodología

El análisis se basa principalmente en:

- NIST SP 800-30 Rev.1
- ISO/IEC 27001
- ISO/IEC 27002
- ISO/IEC 27005
- ISO 27799
- Reglamento General de Protección de Datos (RGPD)

---

# Autor

Iker Infantes
