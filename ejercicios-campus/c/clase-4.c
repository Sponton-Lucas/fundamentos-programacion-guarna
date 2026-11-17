#include <stdio.h>

int func() {
    int counter = 0;
    //static int counter = 0;
    return ++counter;
}

int main() {
    for (int i=0; i<10; i++) {
        printf("Contador: %d\n", func());
    }
    return 0;
}

// Valgrind para chequeo de problemas de memoria
// Memcheck

// instalacion en linux: > sudo apt-get install valgrind