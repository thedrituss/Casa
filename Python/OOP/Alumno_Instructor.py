class Person:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def Greet(self):
        print(f"Hola, yo soy {self.nombre}")
        
    def SetAge(self, age):
        self.age = age

class Estudiante(Person):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def GoToClasses(self):
        print("Yo voy a clase.")
        
    def ShowAge(self):
        print(f"Mi edad es {self.age}")
        
class Profe(Person):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def Explain(self):
        print(f"Empieza la asignatura de {self._asignatura}")
        
    def SetSubject(self, asignatura):
        self._asignatura = asignatura
    
class EstudianteProfeTEST:
    @staticmethod
    def Main():
        person1 = Person('Pepardo')
        person1.Greet()
        
        Estudiante1 = Estudiante('Pepe')
        Estudiante2 = Estudiante('Jose')
        
        Estudiante2.Greet()
        Estudiante2.SetAge(21)
        Estudiante2.Greet()
        Estudiante2.ShowAge()
        
        
        profesor1 = Profe('Enrique')
        profesor1.SetAge(30)
        profesor1.Greet()
        profesor1.SetSubject('Matematicas')
        profesor1.Explain()
        
EstudianteProfeTEST.Main(
        