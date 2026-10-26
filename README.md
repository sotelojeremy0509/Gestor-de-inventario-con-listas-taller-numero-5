# Gestor-de-inventario-con-listas-taller-numero-5
Programa de consola en Python para administrar el inventario de una tienda pequeña (nombres y cantidades de productos), hecho para practicar **listas, índices, ciclos, condicionales y funciones**.
 
**Autor:** Jeremy Antoine Sotelo Scarpeta
**Curso:** Lógica de Programación, Ingeniería de Software, Universidad de La Salle, primer semestre
 
## Funciones del menú
 
| Opción | Qué hace |
|--------|----------|
| 1 | Registrar un producto y su cantidad |
| 2 | Mostrar todos los productos con su cantidad |
| 3 | Buscar un producto por nombre |
| 4 | Modificar la cantidad de un producto |
| 5 | Eliminar un producto |
| 6 | Mostrar cuántos productos diferentes hay (y el total de unidades) |
| 7 | Mostrar el producto con mayor cantidad (maneja empates) |
| 8 | Salir |
 
Cualquier otra opción muestra el mensaje "Opción no válida".
 
## Cómo funcionan las listas paralelas
 
Se usan dos listas: `productos` y `cantidades`. El elemento del índice `i` de cada una describe el mismo producto:
 
```
indice      0         1         2
productos   Arroz     Leche     Panela
cantidades  10        25        7
```
 
Cada operación mantiene ambas listas sincronizadas: al registrar se hace `append` en las dos, al eliminar se hace `pop(i)` en las dos con el mismo índice, y al modificar solo se cambia `cantidades[i]`.
 
## Decisión sobre productos duplicados
 
No se permite registrar el mismo producto dos veces. La comparación ignora mayúsculas y espacios sobrantes (`Arroz` y ` arroz ` son el mismo). Así cada nombre tiene una única cantidad y buscar, modificar o eliminar nunca es ambiguo. Para cambiar la cantidad de uno existente se usa la opción 4.
 
## Casos límite manejados
 
- Inventario vacío (mostrar, resumen, mayor cantidad)
- Buscar, modificar o eliminar un producto que no existe
- Cantidades que no son números enteros no negativos (se vuelve a pedir)
- Nombre vacío
- Opción de menú inexistente
## Estructura
 
```
gestor-inventario-listas/
|-- main.py
|-- README.md
|-- evidencias/
```
 
