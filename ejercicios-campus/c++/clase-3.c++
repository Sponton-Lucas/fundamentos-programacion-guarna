

/* busqueda secuencial con vector desordenado
- Parametros:
*vec: es el vector en donde estan los datos
*n: es la longitud del vector
*valor: el dato a buscar
*Devuelve -1 si no lo encuentra la posicion, en caso de encontrarlo 
*/

int busqueda_secuencial2(int vec[], int n, int valor){
    int posicion = -1;
    int i=0;
    while((i<n) && (vec[i] != valor)){
        i++;
    }
    if (i < n)
        posicion = i;
    return posicion;
}

/* busqueda secuencial con vector ordenado*/

int busqueda_secuencial_ordenada(int vec[], int n, int valor){
    int posicion = -1;
    int i = 0;
    while ((i<n) && (vec[i] < valor)){
        i++;
    }
    if ((i<n) && (vec[i] == valor))
        posicion = i;
    return posicion;
}

/* busqueda binaria*/

int busqueda_binaria(int vec[], int n, int valor){
    int inf = 0;
    int sup = n;
    int posicion = -1;
    int medio;
    while((posicion ==-1)&&(inf<=sup)){
        medio = (inf + sup)/2;
        if (vec[medio]==valor)
            posicion = medio;
        else if(vec[medio] > valor)
            sup = medio - 1;
        else
            inf = medio + 1;
    }
    return posicion;
}

/* metodo de ordenamiento x seleccion*/
#define MAX 100000

void intercambiar(int v[], int i, int j){
    int aux = v[i];
    v[i] = v[j];
    v[j] = aux;
}

void seleccion(int vec[]){
    int i,j, pos;
    for(i=0; i< MAX -1; i++){
        pos=i;
        for(j=i+1; j< MAX; j++){
            if(vec[j]<vec[pos])
                pos = j;
        }
        intercambiar(vec, i, pos);
    }
}

/* metodo de ordenamiendo x burbujeo*/

void burbujeo(int vec[]){
    int i,j;
    for(i=0; i< MAX -1; i++)
        for(j=0; j<MAX -i -1; j++){
            if(vec[j]>vec[j+1])
                intercambiar(vec, j, j+1);
        }
}

/* metodo de ordenamiento x insercion <-- este es el mejor q vemos por ahora*/

void insercion(int vec[]){
    int i,j,aux;
    for(i=1; i<MAX; i++){
        aux = vec[i];
        j=i;
        while((j>0) && (vec[j-1] > aux)){
            vec[j]= vec[j-1];
            j--;
        }
        vec[j] = aux;
    }
}