/*
typedef struct {
    int peso;
    float altura;
} Datos;

Datos laura;
Para recorrer vectores:
#define MF 100 
int v[MF];
for (i=0; i< ML; i++) {
    printf("%i", v[i]);
}

Para recorrer matrices:

for(i=0; i<filas; i++){
    for(j=0; j<columnas; j++){
        printf("%i", m[i][j]);
    }
}

Leer cadenas con fgets:

#include <stdio.h>

int main(){
    char nombre[30];
    printf("INgrese su nombre: ");
    fgets(nombre, 30, stdin);
    printf("Hola %s", nombre);

    return 0;
}

La solucion: Limpieza del Buffer:

void clear_stdin(){
    while(getchar() != '\n'); Se debe aplicar luego de usar un scanf, 
}

La libreria string.h
#include <string.h>
Esta libreria sirve para trabajar con cadenas en C, Incluye funciones para:
- Medir textos -> strlen
- Copiar cadenas -> strcpy
- Unir palabras -> strcat
- Comparar textos -> strcmp
- Buscar texto -> strstr


printf("Cantidad de letras: %zu", strlen(texto)): %zu es el formato para el strlen

strcpy(destino, origen) destino tiene q tener suficiente espacio.

strcat(nombre, apellido): concatena dos cadenas, La segunda se agrega al final, el arreglo debe tener espacio suficiente.

if(strcmp(clave1, clave2) == 0) {
    printf("Las cadenas son iguales") 0= cadenas son iguales, <0 la primera es menor, >0 la primera es mayor. (antes o despues alfabeticamente)
}

if(strstr(frase, "C")) {
    printf("La palabra fue encontrada") se le pasa el vector primero y luego lo q se desea buscar, devuelve null si no encuentra
}

*/

