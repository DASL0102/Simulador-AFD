
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
        recorrido = [self.estado_actual]  # Lista para guardar el recorrido

        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False, recorrido

            clave = (self.estado_actual, simbolo)

            if clave not in self.transiciones:
                return False, recorrido

            self.estado_actual = self.transiciones[clave]
            recorrido.append(self.estado_actual)  # Guardamos el nuevo estado

        return self.estado_actual in self.estados_finales, recorrido



def cargar_desde_txt(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]

    estados = set()
    alfabeto = set()
    estado_inicial = None
    estados_finales = set()
    transiciones = {}

    seccion = None

    for linea in lineas:
        if linea.startswith("#"):
            seccion = linea.lower()
            continue

        if seccion == "#estados":
            estados = set(linea.split(","))

        elif seccion == "#inicial":
            estado_inicial = linea

        elif seccion == "#terminales":
            estados_finales = set(linea.split(","))

        elif seccion == "#alfabeto":
            alfabeto = set(linea.split(","))

        elif seccion == "#transiciones":
            partes = linea.split(",")
            if len(partes) == 3:
                origen, simbolo, destino = partes
                transiciones[(origen, simbolo)] = destino

    afd = AFD(
        estados,
        alfabeto,
        transiciones,
        estado_inicial,
        estados_finales
    )

    return afd

if __name__ == '__main__':

    afd = cargar_desde_txt("automata.txt")

    print("Autómata cargado correctamente.")
    print("Escribe una cadena para evaluar.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        cadena = input("Ingrese cadena: ").strip()

        if cadena.lower() == "salir":
            print("Fin del programa.")
            break

        resultado, recorrido = afd.procesar_cadena(cadena)

        print(f"→ Recorrido de estados: {recorrido}")

        if resultado:
            print("→ Cadena Aceptada\n")
        else:
            print("→ Cadena Inválida\n")