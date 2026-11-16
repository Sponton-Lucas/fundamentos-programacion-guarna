#include <stdio.h>

int main(){
    int cantHorasMes;
    float valorPorHora;
    float resultado;
    printf("Ingrese la cantidad de horas trabajadas en este mes y el valor por hora: ");
    scanf("%d %f", &cantHorasMes, &valorPorHora);
    resultado = cantHorasMes * valorPorHora;
    printf("Su sueldo es %f", resultado);

    return 0;
}