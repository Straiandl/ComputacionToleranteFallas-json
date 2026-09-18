# Práctica Integrada: Monitoreo de Errores y Restauración de Estado

##  Descripción General
Este proyecto implementa un patrón completo de **Resiliencia y Tolerancia a Fallas** en Python. Combina dos pilares fundamentales en el diseño de software confiable:

1. **Rastreo y Monitoreo de Errores en Tiempo Real (Sentry):** Captura las excepciones producidas por defectos (*Faults*) para notificarlas a los desarrolladores sin interrumpir la ejecución del sistema (*Evitando la Caída / Failure*).
2. **Punto de Control y Restauración de Estado (JSON Checkpointing):** Almacena de forma persistente el progreso de las transacciones para que, en caso de un reinicio o fallo del sistema, este pueda reanudarse exactamente desde el punto donde se quedó sin duplicar operaciones ni perder datos.

---

##  Objetivos
* Demostrar la mitigación de la cadena **Fault $\rightarrow$ Error $\rightarrow$ Failure**.
* Implementar mecanismos de persistencia liviana y segura mediante archivos **JSON** (evitando los riesgos de seguridad asociados a *pickle*).
* Asegurar la **idempotencia** en el procesamiento de transacciones (capacidad de reejecutar el script sin alterar el estado final).

---

##  Requisitos Previos

Para ejecutar la aplicación es necesario contar con Python 3.x y el SDK oficial de Sentry.

```bash
pip install sentry-sdk
```

*(Opcional): Si deseas ver el evento en tiempo real en la nube, configura una cuenta en [Sentry.io](https://sentry.io/) e ingresa tu DSN en la función `sentry_sdk.init()`.*

---

##  Evidencias de la Práctica (Capturas de Pantalla)

> **Nota para el alumno:** Sube tus capturas a una carpeta llamada `img/` dentro de tu repositorio y verifica que los nombres de los archivos coincidan.

### 1. Primera Ejecución y Detección de Falla

![Primera Ejecución](https://github.com/Straiandl/ComputacionToleranteFallas-json/blob/0192bd6a35ffd33b23b6eb3dfd72a55b1ce215d8/Cap1Json.png)

### 2. Estructura del Archivo de Estado (`estado_sistema.json`)

![Archivo JSON de Checkpoint](https://github.com/Straiandl/ComputacionToleranteFallas-json/blob/ce7b9f2715b2f480cb3f0048d0ab030f52ab0395/Cap2Json.png)

### 3. Segunda Ejecución (Reinicio y Restauración de Estado)

![Reejecución y Restauración](./img/captura_restauracion_estado.png)

### 4. Ejemplo del json generado
![Json creado]()

---

##  Cómo Ejecutar la Práctica

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta el script por primera vez:
   ```bash
   python main.py
   ```
3. Verifica la creación del archivo `estado_sistema.json`.
4. Vuelve a ejecutar el script para comprobar cómo se restaura el estado y se omiten las tareas previas:
   ```bash
   python main.py
   ```

---

##  Información del Estudiante

* **Alumno:** [De la Paz Mendoza Ian Alexandro]
* **Materia:** [Computacion tolerante a fallas]
* **Fecha:** 18 de Septiembre 2026
