class Diana1053:
    def _init_(self):
        self.idVehículo = 0
        self.idCliente = 0
        self.marca = ""
        self.modelo = ""
        self.año = 0
        self.tipo = ""
        self.kilometraje = 0

    def mostrar_datos(self):
        return (f"ID Vehículo: {self.idVehículo}, ID Cliente: {self.idCliente}, "
                f"Marca: {self.marca}, Modelo: {self.modelo}, "
                f"Año: {self.año}, Tipo: {self.tipo}, "
                f"Kilometraje: {self.kilometraje}")

    def listar_alumnos():
        alumnos = [Diana1053() for _ in range(5)]
        for i, alumno in enumerate(alumnos):
            # Asignar datos ficticios para cada alumno
            alumno.idVehículo = i + 1
            alumno.idCliente = 100 + i
            alumno.marca = f"Marca {i + 1}"
            alumno.modelo = f"Modelo {i + 1}"
            alumno.año = 2000 + i
            alumno.tipo = "Tipo A"
            alumno.kilometraje = 1000 * (i + 1)
        return [alumno.mostrar_datos() for alumno in alumnos]


    def tupla_profes():
        profes = ("Profesor A", "Profesor B", "Profesor C", "Profesor D", "Profesor E")
        return profes


    def diccionario_materia_califa():
        materias_califas = {
            "Matemáticas": 85,
            "Ciencias": 90,
            "Historia": 75,
            "Lengua": 80,
            "Geografía": 88
        }
        return materias_califas

    def altas(self):
        return "La operación se realizó correctamente para los datos del alumno."

    def bajas(self):
        return "La operación se realizó correctamente para los datos del alumno."


# Creación de objeto y asignación de datos
mabel = Diana1053()
mabel.idVehículo = 1
mabel.idCliente = 101
mabel.marca = "Toyota"
mabel.modelo = "Corolla"
mabel.año = 2020
mabel.tipo = "Sedán"
mabel.kilometraje = 15000

# Utilización de los métodos
print("------")
print(mabel.mostrar_datos())
print("------")
print(Diana1053.listar_alumnos())
print("------")
print(Diana1053.tupla_profes())
print("------")
print(Diana1053.diccionario_materia_califa())
print("------")
print(mabel.altas())
print("------")
print(mabel.bajas())