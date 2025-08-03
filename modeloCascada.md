# Resumen de Dificultades - Metodología en Cascada

## Dificultades Identificadas

### 1. **Coordinación entre Backend y Frontend**
- **Problema**: Asegurar que las funciones del backend devuelvan datos en el formato esperado por el frontend
- **Solución**: Definir interfaces claras y documentar el formato de datos esperado

### 2. **Manejo de Errores**
- **Problema**: Los errores del backend deben ser manejados apropiadamente en el frontend
- **Solución**: Implementar validaciones y mensajes de error informativos

### 3. **Dependencias entre Módulos**
- **Problema**: El frontend depende completamente del backend, lo que puede causar problemas si el backend no está listo
- **Solución**: Crear interfaces mock o trabajar en paralelo con especificaciones claras

### 4. **Formato de Presentación**
- **Problema**: Asegurar que los datos se presenten de manera consistente y legible
- **Solución**: Usar librerías como `tabulate` para formateo estándar

### 5. **Integración de Componentes**
- **Problema**: Unir el trabajo de diferentes desarrolladores de manera coherente
- **Solución**: Crear un archivo principal (`app.py`) que integre todos los componentes
