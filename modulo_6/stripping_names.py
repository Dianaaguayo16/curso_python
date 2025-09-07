# 2-7: Stripping Names
nombre_con_espacios = "\t\n  Diana Aguayo  \n\t"
print("Nombre con espacios:", nombre_con_espacios)

print("Sin espacios a la izquierda:", nombre_con_espacios.lstrip())
print("Sin espacios a la derecha:", nombre_con_espacios.rstrip())
print("Sin espacios en ambos lados:", nombre_con_espacios.strip())