# En este desafío, implementarás la lógica de un planificador de tareas en Python. 

# El objetivo es construir la función closure llamada createTaskPlanner, que devolverá una serie de métodos para administrar las tareas. A continuación, se detallan los métodos que deben implementarse:

# addTask(task): recibe un diccionario que contiene la información de la tarea y la agrega al array de tareas. 

# El diccionario debe contener las siguientes claves: 'id', 'name', 'priority', 'tags' y 'completed'. 

# La clave 'completed' se establecerá automáticamente como False al agregar una tarea.

# removeTask(value): recibe el id o nombre de la tarea y la elimina del array de tareas.

# getTasks(): devuelve el array de tareas.

# getPendingTasks(): devuelve solo las tareas pendientes.

# getCompletedTasks(): devuelve solo las tareas completadas.

# markTaskAsCompleted(value): recibe el id o nombre de la tarea y la marca como completada.

# getSortedTasksByPriority(): devuelve una copia de las tareas ordenadas según su prioridad (3: poco urgente, 2: urgente, 1: muy urgente), sin modificar la lista original de tareas.

# filterTasksByTag(tag): filtra las tareas por una etiqueta específica. 

# updateTask(taskId, updates): busca la tarea correspondiente al id especificado y actualiza sus propiedades con las especificadas en el diccionario de actualizaciones.

# Ejemplo 1:

# Input: 

# planner = createTaskPlanner()

# planner['addTask']({
#     'id': 1,
#     'name': 'Comprar leche',
#     'priority': 1,
#     'tags': ['shopping', 'home']
# })

# planner['addTask']({
#     'id': 2,
#     'name': 'Llamar a Juan',
#     'priority': 3,
#     'tags': ['personal']
# })

# planner['markTaskAsCompleted']('Llamar a Juan')

# print(planner['getCompletedTasks']())

# Output:

# [{
#   'id': 2,
#   'name': 'Llamar a Juan',
#   'completed': True,
#   'priority': 3,
#   'tags': ['personal']
# }]

# Ejemplo 2:


# Input:
# planner = createTaskPlanner()

# planner['addTask']({
#     'id': 1,
#     'name': 'Comprar leche',
#     'priority': 1,
#     'tags': ['shopping', 'home']
# })

# planner['addTask']({
#     'id': 2,
#     'name': 'Llamar a Juan',
#     'priority': 3,
#     'tags': ['personal']
# })

# print(planner['filterTasksByTag']('shopping'))

# Output:

# [{
#     'id': 1,
#     'name': 'Comprar leche',
#     'completed': False,
#     'priority': 1,
#     'tags': ['shopping', 'home']
# }]

def createTaskPlanner():

    tasks = list()
    
    def addTask(task):
        task['completed'] = False
        tasks.append(task)

    def removeTask(value):
        for task in tasks:
            if task['id'] == value:
                tasks.remove(task)
            elif task['name'] == value:
                tasks.remove(task)

    def getTasks():
        return tasks

    def getPendingTasks():
        return [task for task in tasks if task['completed'] == False]

    def getCompletedTasks():
        return [task for task in tasks if task['completed'] == True]
    

    def markTaskAsCompleted(value):
        for task in tasks:
            if task['id'] == value or task['name'] == value:
                task['completed'] = True
                break

    def getSortedTasksByPriority():
        priority = lambda task: task['priority']
        return sorted(tasks, key=priority)
        
    
    def filterTasksByTag(tag):
        return [task for task in tasks if tag in task['tags']]

    def updateTask(taskId, updates):
        for task in tasks:
            if task['id'] == taskId:
                task.update(updates)
    
    return {'addTask': addTask, 'removeTask': removeTask, 'getTasks': getTasks, 'getPendingTasks': getPendingTasks, 'getCompletedTasks': getCompletedTasks, 'markTaskAsCompleted': markTaskAsCompleted, 'getSortedTasksByPriority': getSortedTasksByPriority, 'filterTasksByTag': filterTasksByTag, 'updateTask': updateTask }

planner = createTaskPlanner()

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})
planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

print(planner['getTasks']())
planner['getSortedTasksByPriority']()
print(planner['getTasks']())
print(planner['getSortedTasksByPriority']())
print(planner['filterTasksByTag']('personal'))
planner['markTaskAsCompleted'](2)
print(planner['getTasks']())