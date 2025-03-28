encoding="utf-8"
# -*- coding: utf-8 -*-

import random

# lista de regiones (la primera simboliza a la capital)
regiones_america_norte = [
 	"Region1: Yukón, Canadá, Alaska"
 	"Region2: Labrador, Terranova, Nueva York, Groenlandia"
 	"Region3: California, Mexico, Oregón"
]
regiones_america_sur = [
	"Region1: Brasil, Colombia, Perú"
	"Region2: Argentina, Chile, Uruguay"
]
regiones_africa = [
	"Region1: Sahara, Zaire, Sudádrica"
	"Region2: Etiopía, Egipto, Madagascar"
]
regiones_oceania = [
	"Region1: Australia, Sumatra"
	"Region2: Java, Borneo"
]
regiones_asia = [
	"Region1:  Israel, Turquia, Arabia"
	"Region2: Tartaria, Aral, Taymir"
	"Region3: Kamchatka, Japón, Siberia"
	"Region4: Mongolia, Gobi, Irán"
	"Region5: Malasia, China, India"
]
regiones_europa = [
	"Region1: Gran Bretaña, Islandia, Suecia"
	"Region2: Francia, España, Italia"
	"Region3: Polonia, Alemania, Rusia"
]

# Listas de objetivos de victoria
objetivos_victoria1 = [
    "Controlar al menos 7 regiones completas.",

    "Controlar América del Norte, Oceanía y 2 países de África.",
    
    "Controlar África y las siguientes capitales: Francia, Polonia, Yukón, Mongolia.", 
]
objetivos_victoria2 = [
    "Tener bajo control al menos 6 capitales repartidas en: África, Asia, Europa, América del Sur.",
    
    "Controlar Europa y las siguientes capitales: California, Argentina, Australia, Israel.",
    
    "Ocupar Oceanía, 6 países de Asia, 2 de África y 5 de América del Norte.",
]
objetivos_victoria3 = [
    "Controlar Oceanía y las siguientes capitales: Yukón, Etiopía, Malasia, Mongolia, Polonia.",
    
    "Ocupar Asia y 3 paises de América del Norte.",
    
    "Controlar América del Sur, 4 paises de Asia y las siguientes capitales: Labrador, Kamchatka, Gran Bretaña.",
]
objetivos_victoria4 = [
    "Tener bajo control al menos 6 capitales repartidas en: América del Norte, Oceania, África.",
    
    "Controlar América del Norte y las siguientes capitales: Tartaria, Etiopía, Francia.",
    
    "Controlar América del Sur, 5 países de Europa y la siguiente capital: Israel.",
]
objetivos_victoria5 = [
    "Tener bajo control al menos 6 capitales repartidas en: Oceanía, Asia, América del Norte, América del Sur.",
    
    "Tener bajo control al menos 6 capitales repartidas en: Europa, América del Sur, África.",
    
    "Controlar Europa y América del Sur.",
]

# lista de efectos climáticos
efectos_climaticos = [
    "Fuertes tormentas: ningún jugador podrá reacomodar fichas. Duración: 1 turno.",
    "Fuertes tormentas: ningún jugador podrá reacomodar fichas. Duración: 2 turnos.",
    
    "Revuelta local: un país neutral obtiene +1 ejércitos.",
    "Revuelta local: un país neutral obtiene +2 ejércitos.",
    "Revuelta local: un país neutral obtiene +3 ejércitos.",
    "Revuelta local: un país neutral obtiene +4 ejércitos.",
    "Revuelta local: un país neutral obtiene +5 ejércitos.",
    "Revuelta local: un país neutral obtiene +6 ejércitos.",
    
    "Logística: todos los jugadores reciben menos ejércitos este turno. (la mitad de lo que deberían redondeando hacia arriba).",
    
    "Reclutamiento masivo: todos los jugadores pueden reforzar un país con +1 ejército.",
    "Reclutamiento masivo: todos los jugadores pueden reforzar un país con +3 ejércitos.",
    
    "Terremoto: un país pierde la mitad de sus ejércitos (redondeando hacia abajo).",
    
    "Niebla densa: los jugadores no pueden atacar esta ronda. Duración: 1 turno.",
    
    "Inundación: un país perteneciente a un jugador pierde 2 ejércitos.",
    
    "Tormenta de arena: todos los paises controlados por un jugador en el continente africano pierden 1 ficha.",
    
    "Ola de calor: los ejércitos en el desierto (áfrica) controlados por un jugador, podrán atacar con un máximo de dos fichas. Duración: 2 turnos.",
    
    "Vientos favorables: los refuerzos a paises aliados se producirán en forma instantanea. Duración: 1 turnos.",
    
    "Ruta de la seda: Todos los paises asiáticos controlados por un jugador reciben +1 ficha y los paises neutrales reciben +2.",
    
    "Hambruna: todos los paises controlados por jugadores pierden 1 fichas.",
    "Hambruna: todos los paises controlados por jugadores pierden 2 fichas.",
    
    "Crisis mundial: No se podrá incorporar fichas al comienzo del siguiente turno. Duración: 1 turno.",
    "Crisis mundial: No se podrá incorporar fichas al comienzo del siguiente turno. Duración: 2 turnos.",
    "Crisis mundial: No se podrá incorporar fichas al comienzo del siguiente turno. Duración: 3 turnos.",
    
    "Rebelión: El pais seleccionado (excluyendo capitales) se vuelve neutral. Se le asignan 3 fichas y el jugador recupera la mitad de las fichas que habia en ese país.",
    "Rebelión2: 2 paises (excluyendo capitales) se vuelven neutrales. Se le asignan 3 fichas y el jugador/ los jugadores recuperan la mitad de las fichas que habia en sus paises correspondientes.",
    "Rebelión3: 3 paises (excluyendo capitales) se vuelven neutrales. Se le asignan 3 fichas y el jugador/ los jugadores recuperan la mitad de las fichas que habia en sus paises correspondientes.",
    "Rebelión!: una capital controlada por un jugador se rebela y se queda con la mitad de las fichas que el jugador tenia en dicha capital (número impar redondea hacia arriba).",
    "Rebelión!!: 2 capitales controladas por un jugador se rebelan y se queda con la mitad de las fichas que el/ los jugadores tenian en dichas capitales (número impar redondea hacia arriba).",
    
    "Fronteras abiertas: Solo se podrán realizar ataques de un continente a otro. Duración: 1 turno.",
    "Fronteras cerradas: Solo se podrán realizar ataques dentro del mismo continente. Duración: 1 turno.",
    
    "Crisis: Todos los jugadores deberán tirar un dado, el jugador que saque el número más chico, no podrá atacar en el siguiente turno pero si reacomodar fichas.",
    "Crisis2: Todos los jugadores deberán tirar un dado, el jugador que saque el número más chico, no podrá reacomodar fichas luego de su turno.",
    "Crisis3: Todos los jugadores deberán tirar un dado, el jugador que saque el número más alto, podrá incorporar dos fichas en cualquiera de sus paises.",
    
    "Guerra de secesión: Los paises norteamericanos controlados por jugadores, pierden 1 ficha.",
    
    "Comercio favorable: los jugadores con al menos un pais en norteamérica reciben +2 fichas que puesen ubicar en donde quieran.",
    
    "epidemia: Los paises de sudamérica pierden 1 ficha.",
    "epidemia: Los paises de norteamérica pierden 1 ficha.",
    "epidemia: Los paises de asia pierden 1 ficha.",
    "epidemia: Los paises de áfrica pierden 1 ficha.",
    "epidemia: Los paises de oceania pierden 1 ficha.",
    "epidemia: Los paises de europa pierden 1 ficha.",
    
    "Pandemia: Todos los paises controlados por jugadores pierden 1 ficha.",
    
    "Imperialismo: Los paises europeos controlados por jugadores suman +1 ficha.",
    
    "Migración: 5 paises controlados por jugadores pierden 1 ficha.",
    
    "Altamar: Solo se pueden atacar paises conectados por puentes.",
    "Naufragio: No se pueden atacar paises conectados por puentes.",
    
    "Congreso: No se pueden atacar paises europeos. Duración: 1 turnos.",
    
    "Marcha forzosa: Se pueden mover fichas ilimitadas incluso antes de atacar. Duración: 1 turno.",
    
    "Exportación: Los paises sudamericanos controlados por jugadores reciben +1 ficha.",
]

# almacena los nombres de las listas
listas = {
    (1.): objetivos_victoria1,
    (2.): objetivos_victoria2,
    (3.): objetivos_victoria3,
    (4.): objetivos_victoria4,
    (5.): objetivos_victoria5,
}

# Obtener la entrada del usuario
numero_lista = int(input("¿A qué lista quieres acceder?: "))

# Validar la entrada del usuario
if numero_lista in listas:
    # Seleccionar un elemento aleatorio de la lista elegida
    elemento_aleatorio = random.choice(listas[numero_lista])
    print(f"El elemento aleatorio de la lista {numero_lista} es: {elemento_aleatorio}")
else:
    print("Número de lista incorrecto."),

def seleccionar_efecto():
    return random.choice(efectos_climaticos)

def main():
    while True:
        print("\nSeleccione una opción:")
        print("1. Obtener un efecto climático aleatorio")
        print("2. Salir")
        
        opcion = input("Ingrese el número de la opción: ").strip()
        
        if opcion == "1":
            efecto = seleccionar_efecto()
            print(f"\nEfecto climático aplicado: {efecto}")

        elif opcion == "2":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()


