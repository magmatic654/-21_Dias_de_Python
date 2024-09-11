# En este desafío, vamos a implementar una lista enlazada simple para almacenar información sobre pacientes de un hospital. Cada nodo de la lista representará a un paciente y tendrá los siguientes campos:

# Nombre del paciente (cadena de texto)
# Edad del paciente (número)
# Número de cama asignada al paciente (número)

# La lista enlazada deberá tener los siguientes métodos:

# addPatient(name, age): agrega un nuevo paciente a la lista, asignándole la próxima cama disponible. Si no hay camas disponibles, debe lanzar un error con el mensaje "No hay camas disponibles".

# removePatient(name): remueve al paciente con el nombre especificado de la lista y libera su cama. Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

# getPatient(name): retorna la información del paciente con el nombre especificado en el siguiente formato {name, age, bedNumber}. Si el paciente no se encuentra en la lista, debe lanzar un error con el mensaje "Paciente no encontrado".

# getPatientList(): retorna una lista con la información de todos los pacientes en la lista, cada paciente deberá tener el siguiente formato {name, age, bedNumber}.

# getAvailableBeds(): retorna un número con el total de camas disponibles.

# Recuerda usar la sintaxis raise Exception("mensaje") para lanzar errores.

# Aquí tienes un ejemplo de cómo se utilizaría esta singly linked list:

# Input
# list = PatientList(3)
# list.addPatient("Paciente 1", 20)
# list.addPatient("Paciente 2", 30)
# list.getPatientList()
#
# Output:
# [
#   { 'name': 'Paciente 1', 'age': 20, 'bedNumber': 1 },
#   { 'name': 'Paciente 2', 'age': 30, 'bedNumber': 2 },
# ]

# list.getPatient("Paciente 1")
#
# Output:
# { 'name': 'Paciente 1', 'age': 20, 'bedNumber': 1 }

 
# Input
# list.removePatient("Paciente 1")
# list.getPatientList()
#
# Output:
# [
#   { 'name': 'Paciente 2', 'age': 30, 'bedNumber': 2 },
# ]

class PatientNode:
    def __init__(self, name, age, bed_number):
        self.name = name
        self.age = age
        self.bed_number = bed_number
        self.next = None

class PatientList:
    def __init__(self, max_beds):
        self.max_beds = max_beds
        self.head = None
        self.tail = None
        self.lenght = 0
    
    def addPatient(self, name, age):
        if self.lenght == self.max_beds:
            raise Exception('No hay camas disponibles')
        new_patient = PatientNode(name, age, self.lenght + 1)
        if self.head == None:
            self.head = new_patient
            self.tail = new_patient
        else:
            self.tail.next = new_patient
            self.tail = new_patient

        self.lenght += 1

    def removePatient(self, name):
        if self.head.name == name:
            self.head = self.head.next
            self.lenght -= 1
            return
        
        current_patient = self.head
        while current_patient.next:
            if current_patient.next.name == name:
                current_patient.next = current_patient.next.next
                self.lenght -= 1
                return
            current_patient = current_patient.next
        raise Exception('Paciente no encontrado')
    
    def getPatient(self, name):
        if self.head.name == name:
            return {'name': self.head.name, 'age': self.head.age, 'bedNumber': self.head.bed_number}
        
        current_patient = self.head
        while current_patient.next:
            if current_patient.next.name == name:
                return  {'name': current_patient.name, 'age': current_patient.age, 'bedNumber': current_patient.bed_number}
            current_patient = current_patient.next
        raise Exception('Paciente no encontrado')
    
    def getPatientList(self):
        patient_list = []

        current_patient = self.head
        while current_patient:
            patient_list.append({'name': current_patient.name, 'age': current_patient.age, 'bedNumber': current_patient.bed_number})
            current_patient = current_patient.next
        return patient_list
    
    def getAvailableBeds(self):
        return self.max_beds - self.lenght
    

list = PatientList(4)
list.addPatient("Paciente 1", 20)
list.addPatient("Paciente 2", 20)
list.addPatient("Paciente 3", 30)
list.addPatient("Paciente 4", 30)
print(list.getPatientList())

