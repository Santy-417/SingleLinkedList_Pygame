# Estudio de las LinkedList

# Lo primero que hacemos es crear la clase Node que es la que va a almacenar el valor del nodo
# y hacia donde debe de apuntar, con los valore data(valor) y next(puntero). 
class Node:

    def __init__(self,data):

        self.value = data
        self.next = None


# Lo segundo seria que una vez con la clase Node creada lo que vamos a hacer es crea una nueva clase
# que es la que va a contener como tal la lista enlazada(LinkedList), la cual va a tener nuevos atributos
# como lo son la cabeza(head), la cola(tail) que hace referencia al ultimo nodo de la lista y la 
# longitu(lenght) que es la referencia al numero de nodos que hay en la lista.


class SingleLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
        self.lenght = 0

# Lo tercero una vez ya con la clase creada que es SingleLinkedList lo que hacemo es que empezamos a crear
# los metodos o la funciones que nos van a permitir crear, eliminar, agregar, etc. 
    

# Ahora lo que vamos a hacer es una funcion que nos agregue un nodo al inicio de la lista, la manera en que 
# se hace es que el nuevo nodo que vamos a agregar, le vamos a pasar el atributo next para que nos apunte
# a la cabeza que pasaria a ser el segundo nodo de la lista y ahora la cabeza que seria seria el new_nodo
# tomaria el nuevo valor
    def agregar_nodo_al_inicio(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
# Este self.head.next lo que hace es que apunta hacia el primer nodo de la lista
# Luego self.head lo que hace es que al ya estar actualizada apunta al nuevo nodo
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1

# Vamos a hacer la funcion que nos agregue un nodo al final de la lista, la manera en que se hace es simple
# lo que hacemos es que el ultimo nodo osea la cola(tail) le pasamos el atributo de next para que apunte al nuevo
# nodo, con esto quedaria actualizada la cola(tail), luego lo que se hace es que la nueva cola o el ultimo nodo
# tome el valor del nuevo nodo
    def agregar_nodo_al_final(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
# Este self.tail.next lo que hace es que apunta hacia el ultimo nodo de la lista
# Luego self.tail lo que hace es que al ya estar actualizada apunta al nuevo nodo
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1

# Vamos a hacer un metodo que elimine el primer nodo de la lista
# Lo que se hace es que primero evaluamos que si tenga nodos la lista con el if not
# Luego evaluamos si la listo solo tiene un nodo, de manera que se elimina ese
# solo nodo e igualamos la cabeza(head) y la cola(tail) en None y la longuitud(0)
# luego solo queda eliminar el primer nodo creando una nueva variable que va a almacenar
# el nodo que se va a eliminar y lo igualamos a la cabeza, de manera que la nueva 
# cabeza va a ser el segundo nodo y para ello debes decir que la cabeza es igual
# a la cabeza.next y disminuimos la longuitud en 1
    def eliminar_primer_nodo(self):

        if not self.head:
            return None
        elif not self.head.next:
            node_to_remove = self.head
            self.head = None
            self.tail = None
            self.lenght -= 1
            return node_to_remove.value
        else:
            node_to_remove = self.head
            self.head = self.head.next
            self.lenght -= 1
            return node_to_remove.value

# Vamos a hacer un metodo que elimine el ultimo nodo de la lista
# Lo que hacemos es primero validar si al menos tenemos un nodo en la lisa con el
# if not, de manera que si no hay nodos devuelva None, luego validamos que al menos
# tenga un solo nodo, de manera que eliminamos ese igualando la caeza(head) y la 
# cola(tail) en None para que asi se elimine el unico nodo que habia, y luego la
# longuitud se decrementa en 1, luego si tiene mas de un solo nodo lo que se hace es
# que creamos una nueva variable que va a ser current_node(nodo actual) que va a 
# almacenar la cabeza para luego recorrer con un while desde la cabez hasta el penultimo
# nodo de la lista, pasandoles los parametros next para evaluar en donde la en None
# luego decimos que la cola(tail) va a ser igual al nodo actual, el cual ocupo
# la posicion del penultimo nodo que se va a convertir en el ultimo nodo y la 
# longuitud se decremente en 1 
    def eliminar_ultimo_nodo(self):
        if not self.head:
            return None
        elif not self.head.next:
            nodo_to_remove = self.head
            self.head = None
            self.tail = None
            self.lenght -= 1
            return nodo_to_remove
        else: 
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            nodo_to_remove = current_node.next
            current_node.next = None
            self.tail = current_node
            self.lenght -= 1
            return nodo_to_remove.value

    