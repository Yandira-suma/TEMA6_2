class Alumno:
   
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
 
 
    # función imprimir
    def imprimir(self):
               print("Nombre: ",self.nombre)
               print("Nota: ",self.nota)
 
 
    # función para ver si el alumno ha aprobado o ha desaprobado
    def resultado(self):
            if self.nota < 11:
                print("El estudiante ha desaprobado")
            else:
                print("El estudiante ha aprobado")
 
 
 
# bloque principal

alumno1=Alumno()
alumno1.inicializar("Milagros",10)
alumno1.imprimir()
alumno1.resultado()

alumno2=Alumno()
alumno2.inicializar("Angelica",19)
alumno2.imprimir()
alumno2.resultado()
