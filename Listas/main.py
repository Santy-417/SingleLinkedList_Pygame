from listas import Listas
from recorrido_listas import Recorridolistas
from listas_simplemente_enlazadas import SingleLinkedlist


inst_listas_mascotas = Listas()
inst_listas_recorrido_listas = Recorridolistas()
inst_single_linked_list = SingleLinkedlist()

inst_single_linked_list.add_node_at_end('A')
inst_single_linked_list.add_node_at_end('B')
inst_single_linked_list.add_node_at_end('C')
inst_single_linked_list.add_node_at_end('D')
inst_single_linked_list.print_single_linked_list()

# ins_listas_recorrido_listas.agregarValoreslista()
# ins_listas_mascotas.menu_opciones()