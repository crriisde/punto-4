print (" ") #este linea deja el espacio para el nombre 
print ("Cristian David Salas De La O 3,W") #este linea define el nombre del programador 
print (" ") #este linea defa el espacio para el nonbre 
# Crear un archivo de ejemplo y leer los primeros 5 caracteres
with open("demofile.txt", "w") as f: #este linea define el whith
    f.write("Este es un archivo de ejemplo.") #este linea muestra el aviso

with open("demofile.txt", "r") as f: #este linea define el whith
    print("Primeros 5 caracteres:", f.read(5)) #este linea muestra el aviso
