import matplotlib.pyplot as plt
from matplotlib_venn import venn2


# Definir el conjunto total de personas en el ensayo clínico
#  #Definir sets S y H 
X = {"Alice", "Bob", "Charlie", "David", "Eve"}

# DEfinir quiénes tienen VBS
S = {"Alice", "Charlie"}

#Conjunto total
print(f'Conjnto total X: {X}')

#Conjunto de personas con VBS, segundo conjunto
print(f'Conjunto de personas con VBS S: {S}')

#Interseccion and
print(f'Intersección X ∩ S: {S & X}')  # ∩

#Union or 
print(f'Union X ∪ S: {S | X}')  # ∪


#Graficar
venn = venn2([S, X], ('S', 'X'))
venn.get_label_by_id('10').set_text(S - X)  # Solo en S
venn.get_label_by_id('01').set_text(X - S)  # Solo en X
venn.get_label_by_id('11').set_text(S & X)  # Intersección
venn.get_label_by_id('11').set_text(S | X)  # Unión
#Ajustar colores para mejorar la legibilidad
venn.get_patch_by_id('10').set_color('skyblue')
venn.get_patch_by_id('01').set_color('lightgreen')
venn.get_patch_by_id('11').set_color('yellow')
venn.get_patch_by_id('10').set_edgecolor('black')
venn.get_patch_by_id('01').set_edgecolor('black')
venn.get_patch_by_id('11').set_edgecolor('black')

#Ajustar el tamaño de las etiquetas
for label in venn.set_labels:
    label.set_fontsize(8)
for label in venn.subset_labels:
    label.set_fontsize(5)

plt.title("Diagrama de Venn de personas con y sin VBS")
plt.show()