class Alumno():
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
      
        
        

    def __str__(self):
        
        return 'Nombre: {}{}'.format(self.nombre, self.apellidos)
        
class Nota(Alumno):

    def __init__(self, nota):
        self.nota = nota
        if nota in range(3,6):
            print('La nota del estudiante es ', self.nota, 'y ha aprobado')

        else:
            print('La nota del estudiante es ', self.nota, 'y no ha aprobado')

A = Alumno("Rafael ", "Jimenez Cardona")
print(A)
N = Nota(float(input('Ingrese la nota del estudiante: ')))



            
