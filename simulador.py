import json
class AFD:
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.estado_actual = estado_inicial
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales

    def reiniciar(self):
        self.estado_actual = self.estado_inicial

    def procesar_cadena(self, cadena):
        self.reiniciar()

        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False

            clave = (self.estado_actual, simbolo)

            if clave not in self.transiciones:
                return False

            self.estado_actual = self.transiciones[clave]

        return self.estado_actual in self.estados_finales



def cargar_desde_json(ruta):
    with open(ruta, "r") as f:
        data = json.load(f)

    estados = set(data["estados"])
    alfabeto = set(data["alfabeto"])
    estado_inicial = data["estado_inicial"]
    estados_finales = set(data["estados_finales"])
    
    transiciones = {}
    for origen, simbolo, destino in data["transiciones"]:
        transiciones[(origen, simbolo)] = destino

    afd = AFD(
        estados,
        alfabeto,
        transiciones,
        estado_inicial,
        estados_finales
    )

    return afd, data["cadenas_test"]

if __name__ == '__main__':

    afd, pruebas = cargar_desde_json("automata.json")

    for i, cadena in enumerate(pruebas, 1):
        resultado = afd.procesar_cadena(cadena)
        estado = "Cadena Aceptada" if resultado else "Cadena Inválida"
        print(f"Prueba {i}: {cadena} → {estado}")

   