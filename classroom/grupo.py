from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="Grupo de estudiantes: grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes
        Grupo.grado= "Grado 12"

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        if alumno==None:
            lista=[]
            return
        else:
            lista.append(alumno)
            self.listadoAlumnos = self.listadoAlumnos + lista
            self.agregarAlumno(None,[])

    def __str__(self):
        ch= self._grupo
        return ch
    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
