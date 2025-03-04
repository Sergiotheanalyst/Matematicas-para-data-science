import matplotlib.pyplot as plt
from matplotlib_venn import venn2


# Definir el conjunto total de personas en el ensayo clínico
#  #Definir sets S y H 
X = {"Alice", "Bob", "Charlie", "David", "Eve"}

# DEfinir quiénes tienen VBS
S = {"Alice", "Charlie"}

# El complemento de S en X es H (quienes no tienen VBS "very bad syndrome”")
H = X - S  # También se puede escribir como: H = {x for x in X if x not in S}

# Verificamos las propiedades mencionadas en el problema
assert S | H == X  # X = S ∪ H  #Union
assert S & H == set()  # S ∩ H = ∅  #Intersección

# Función para determinar si una persona tiene VBS o no
def test_person(person):
    if person in S:
        return f"{person} tiene VBS (pertenece a S)"
    elif person in H:
        return f"{person} no tiene VBS (pertenece a H)"
    else:
        return f"{person} no está en el estudio"

# Pruebas
print(test_person("Alice"))
print(test_person("Bob"))
print(test_person("Charlie"))
print(test_person("David"))         
print(test_person("Eve"))
print(test_person("Zoe"))  # Persona fuera del conjunto


