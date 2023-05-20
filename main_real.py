from Taller_subir_nota import SingleLinkedList

# Crear una instancia de SingleLinkedList
inst_single_linked_list = SingleLinkedList()

# Agregar nodos a la lista
inst_single_linked_list.add_node_at_end(1)
inst_single_linked_list.add_node_at_end(2)
inst_single_linked_list.add_node_at_end(3)
inst_single_linked_list.add_node_at_end(4)
inst_single_linked_list.add_node_at_start(5)
print('-------------------------------------------------------------------------------------------------------------------------')

# Imprimir la lista
print('Estado de la lista:')
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Eliminar el último nodo
print('Eliminar último nodo.')
inst_single_linked_list.delete_at_end()
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Eliminar el primer nodo
print('Eliminar primer nodo.')
inst_single_linked_list.delete_at_start()
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Eliminar nodo por posición
print('Eliminar nodo por posición.')
inst_single_linked_list.remove_node_by_index(3)
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Eliminar nodo por valor
print('Eliminar nodo por valor.')
inst_single_linked_list.remove_node_by_value(2)
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Mostrar la reversa de la lista
print('Mostrar la reversa de la lista.')
inst_single_linked_list.reverse_single_linked_list()
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Obtener el valor del nodo de la mitad de la lista
print('Obtener valor del nodo de la mitad de la lista.')
middle_value = inst_single_linked_list.get_value_middle_node()
print('Valor del nodo de la mitad:', middle_value)
print('-------------------------------------------------------------------------------------------------------------------------')

# Añadir al final únicamente valores pares
inst_single_linked_list.add_odd_values_at_end(4)
inst_single_linked_list.add_odd_values_at_end(6)
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Añadir al inicio únicamente valores impares
inst_single_linked_list.add_not_odd_values_at_start(3)
inst_single_linked_list.add_not_odd_values_at_start(1)
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Obtener el valor de la suma de todos los nodos de la lista
total_sum = inst_single_linked_list.get_sum_all_values()
print('Valor de la suma de todos los nodos:', total_sum)
print('-------------------------------------------------------------------------------------------------------------------------')

# Obtener el tamaño de la lista
size = inst_single_linked_list.get_size()
print('Tamaño de la lista:', size)
print('-------------------------------------------------------------------------------------------------------------------------')

# Buscar posición por valor
position = inst_single_linked_list.find_position_by_value(3)
print('Posición del valor "C":', position)
print('-------------------------------------------------------------------------------------------------------------------------')

# Ordenar elementos de la lista
print('Ordenar elementos de la lista.')
inst_single_linked_list.selection_sort()
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Insertar en una posición
print('Insertar en una posición.')
inst_single_linked_list.insert_at_position('X', 2)
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Actualizar valor en una posición
print('Actualizar valor en una posición.')
inst_single_linked_list.update_value_at_position('Y', 3)
inst_single_linked_list.print_single_linked_list()
print('-------------------------------------------------------------------------------------------------------------------------')

# Verificar si la lista está vacía
print('Verificar si la lista está vacía.')
print('Estado de la lista:')
empty_list = inst_single_linked_list.empty_list()
print('-------------------------------------------------------------------------------------------------------------------------')

