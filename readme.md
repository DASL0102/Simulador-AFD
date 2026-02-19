# Simulador de AFD en Python

Este proyecto permite definir y probar un **Autómata Finito Determinista (AFD)** usando un archivo JSON, sin necesidad de modificar el código fuente cada vez que se quiera crear un nuevo autómata.

---

# Requisitos

- Python 3.8 o superior
- No se requieren librerías externas (usa solo `json`)

Verifica tu versión:

```bash
python --version
```

---

# Estructura del Proyecto

```
proyecto/
│
├── afd.py
├── automata.json
└── README.md
```

---

# ▶Cómo ejecutar el programa

Desde la carpeta del proyecto:

```bash
python3 simulador.py
```

El programa cargará automáticamente el archivo:

```
automata.json
```

Y ejecutará todas las cadenas de prueba definidas en él.

---

# Cómo crear el archivo JSON

El archivo debe llamarse:

```
automata.json
```

Debe tener la siguiente estructura:

```json
{
  "estados": ["q0", "q1", "q2"],
  "alfabeto": ["0", "1"],
  "estado_inicial": "q0",
  "estados_finales": ["q2"],
  "transiciones": [
    ["q0", "0", "q1"],
    ["q0", "1", "q0"],
    ["q1", "0", "q1"],
    ["q1", "1", "q2"],
    ["q2", "0", "q1"],
    ["q2", "1", "q0"]
  ],
  "cadenas_test": [
    ["1", "0", "1"],
    ["0", "1"],
    ["1", "1", "1"],
    ["0", "0", "1"]
  ]
}
```

---

# Explicación de cada sección

## estados

Lista de todos los estados del autómata.

```json
"estados": ["q0", "q1", "q2"]
```

---

## 🔹 alfabeto

Símbolos permitidos en las cadenas.

```json
"alfabeto": ["0", "1"]
```

---

## 🔹 estado_inicial

Estado donde comienza el autómata.

```json
"estado_inicial": "q0"
```

---

## 🔹 estados_finales

Estados de aceptación.

```json
"estados_finales": ["q2"]
```

---

## 🔹 transiciones

Lista con formato:

```
[estado_origen, simbolo, estado_destino]
```

Ejemplo:

```json
["q1", "1", "q2"]
```


---

## 🔹 cadenas_test

Lista de cadenas que se probarán automáticamente.

Cada cadena debe ser una lista de símbolos:

```json
["1", "0", "1"]
```

---

# Resultado esperado

Al ejecutar el programa verás algo como:

```
Prueba 1: ['1', '0', '1'] → ✅ Válida
Prueba 2: ['0', '1'] → ❌ Inválida
```

---

# Reglas importantes

- Todos los símbolos usados en transiciones deben existir en el alfabeto.
- Todos los estados usados deben existir en la lista de estados.
- No deben existir transiciones duplicadas.
- El AFD debe ser determinista (una transición por símbolo desde cada estado).

---

# 🚀 Crear un nuevo autómata

1. Modifica `automata.json`
2. Cambia estados, alfabeto y transiciones
3. Ejecuta nuevamente:

```bash
python simulador.py
```

No necesitas tocar el código Python.





