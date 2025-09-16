# ⚙️ Automatización de Transformación de Datos para Plantilla de Reporte

Este proyecto consiste en una **automatización de procesos de datos** que toma como entrada una base de clientes (`BASE_Lima_reporte_sbp_prueba.csv`) y genera una **plantilla estandarizada** con las columnas necesarias, reordenadas y renombradas según los requerimientos del negocio.

---

## 📂 Archivos

- **Entrada**  
  - `BASE_Lima_reporte_sbp_prueba.csv` → Contiene la base original de clientes con múltiples variables.  

- **Salida esperada**  
  - `Plantilla_Final.xlsx` (o `.csv`) → Archivo generado con las columnas seleccionadas, reordenadas y con los nombres correctos para su integración en procesos posteriores.

---

## 🛠️ Proceso de Transformación

La automatización realiza los siguientes pasos:

1. **Carga de la base original**  
   Lectura del archivo fuente en formato CSV.

2. **Selección de columnas requeridas**  
   Se identifican las columnas necesarias de la base de datos y se descartan las que no son relevantes para el reporte.

3. **Renombrado de columnas**  
   Las columnas son renombradas de acuerdo con la **plantilla de negocio**.

   Ejemplo de mapeo (fragmento):

   | Columna Origen                   | Columna Plantilla                         |
   |----------------------------------|-------------------------------------------|
   | `RUC_Validata`                   | `RUC`                                     |
   | `Razon Social_Validata`          | `RAZON SOCIAL`                            |
   | `Nombre_Completo`                | `TIPO CLIENTE`                            |
   | `Fecha Nacimiento`               | `NUMERO DOCUMENTO`                        |
   | `Nombre_Completo`                | `PRIMER NOMBRE` / `SEGUNDO NOMBRE` (parseado) |
   | `Lineas TC Utilizadas`           | `TOTAL LINEAS TC` (o según plantilla)     |
   | `Numero1`                        | `CELULAR1`                                |
   | `Numero2`                        | `CELULAR2`                                |
   | `Numero3`                        | `CELULAR3`                                |
   | `SBP_PRESTAMO`                   | `RCC SALDO LD`                            |
   | `COLOR_DXP_Filtro_A_top`         | `COLOR`                                   |
   | `Edad`                           | `EDAD`                                    |

   > 📌 El mapeo completo de columnas debe colocarse en un archivo adicional dentro del repositorio (`mapeo_columnas.md`) para referencia y mantenimiento.

4. **Reordenamiento de columnas**  
   Las columnas se ordenan según el formato requerido en la **plantilla final**.

5. **Validaciones y limpieza**  
   - Validación de formatos de teléfono, RUC y documento.  
   - Manejo de nulos y valores por defecto.  
   - Normalización de strings (trim, upper/lower, eliminación de caracteres especiales si aplica).

6. **Generación del archivo de salida**  
   Se exporta el archivo transformado (`Plantilla_Final.xlsx` o `.csv`) listo para ser usado en reportes o procesos posteriores.

---

## ✅ Beneficios

La automatización entrega beneficios operativos, de calidad de datos y de negocio. A continuación se detallan con su impacto y cómo medirlos:

### Beneficios operativos
- **Ahorro de tiempo**: reduce el tiempo manual de preparación de plantillas (horas/hombre por tarea).  
- **Escalabilidad**: procesa grandes volúmenes de datos sin intervención manual.  

### Beneficios de calidad de datos
- **Menos errores humanos**: elimina errores por copy-paste y renombrados manuales.  
- **Estándares consistentes**: nombres y formatos homogéneos que facilitan integraciones posteriores.  

### Beneficios de negocio
- **Mayor velocidad para toma de decisiones**: los reportes se generan más rápido, reduciendo el *time-to-insight*.  
- **Mejor trazabilidad y auditoría**: logs y versiones permiten seguir cambios y reproducir resultados.  

### Beneficios de cumplimiento y riesgo
- **Validaciones automáticas** (RUC, formatos, flags) ayudan a cumplir reglas internas y regulaciones.  
- **Reducción de reprocesos**: menos filtraciones de datos incorrectos en procesos críticos (por ejemplo, scoring u ofertas).  

### Beneficios técnicos y económicos
- **Reutilización**: el script puede integrarse en pipelines o programarse como job (cron / Airflow).  
- **Menor costo operativo**: menos horas hombre significa ahorro en costos laborales por tarea repetitiva.

---

## 📊 Cómo medir los beneficios

| Métrica                          | Antes (baseline) | Después (objetivo) | Periodicidad |
|----------------------------------|------------------|--------------------|--------------|
| Horas hombre por proceso         | (ej. 4 h)        | (ej. 0.5 h)        | por ejecución|
| % registros con errores          | (ej. 6%)         | (ej. 0.5%)         | mensual      |
| Archivos procesados/hora         | (ej. 1)          | (ej. 10)           | diario       |
| Tiempo hasta entrega del reporte | (ej. 24 h)       | (ej. 2 h)          | por ciclo    |

> Ajusta los valores base (baseline) con tus mediciones reales y define objetivos alcanzables.

---

## 🚀 Ejecución

### Requisitos previos
- Python 3.9 o superior  
- Librerías necesarias:
  ```bash
  pip install pandas openpyxl

