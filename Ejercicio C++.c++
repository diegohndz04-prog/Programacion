//Ejercicio 1
#include <iostream>

int main() {
    std::cout << "¡Hola, Mundo!" << std::endl;

    int entero = 10;
    float flotante = 3.14f;
    char caracter = 'A';
    bool booleano = true;

    std::cout << "Valor del entero: " << entero << std::endl;
    std::cout << "Valor del flotante: " << flotante << std::endl;
    std::cout << "Valor del caracter: " << caracter << std::endl;
    std::cout << "Valor del booleano: " << booleano << std::endl;

    return 0;
}



//Ejercicio2
#include <iostream>
#include <cmath>

int main() {
    double num1, num2;

    std::cout << "Ingresa el primer numero: ";
    std::cin >> num1;
    std::cout << "Ingresa el segundo numero: ";
    std::cin >> num2;

    std::cout << "Suma: " << num1 + num2 << std::endl;
    std::cout << "Resta: " << num1 - num2 << std::endl;
    std::cout << "Multiplicacion: " << num1 * num2 << std::endl;
    std::cout << "Division: " << num1 / num2 << std::endl;

    std::cout << "Potencia (" << num1 << "^" << num2 << "): " << pow(num1, num2) << std::endl;
    std::cout << "Raiz cuadrada de " << num1 << ": " << sqrt(num1) << std::endl;

    return 0;
}


//Ejercicio 3
#include <iostream>

int main() {
    int edad;

    std::cout << "Ingresa tu edad: ";
    std::cin >> edad;

    if (edad >= 18) {
        std::cout << "Eres mayor de edad." << std::endl;
    } else {
        std::cout << "Eres menor de edad." << std::endl;
    }

    return 0;
}



//Ejercicio 4
#include <iostream>

#define LIMITE 10

int main() {
    int numero;

    std::cout << "Ingresa un numero para su tabla de multiplicar: ";
    std::cin >> numero;

    for (int i = 1; i <= LIMITE; ++i) {
        std::cout << numero << " x " << i << " = " << numero * i << std::endl;
    }

    return 0;
}



//Ejercicio 5
#include <iostream>

int main() {
    int numeroSecreto = 42;
    int intento;

    std::cout << "Adivina el numero secreto entre 1 y 100." << std::endl;

    while (intento != numeroSecreto) {
        std::cout << "Ingresa tu intento: ";
        std::cin >> intento;

        if (intento > numeroSecreto) {
            std::cout << "Mas bajo." << std::endl;
        } else if (intento < numeroSecreto) {
            std::cout << "Mas alto." << std::endl;
        }
    }

    std::cout << "¡Felicidades, adivinaste el numero!" << std::endl;

    return 0;
}



//Ejercicio 6
#include <iostream>

int main() {
    int opcion;

    do {
        std::cout << "\n--- Menu ---" << std::endl;
        std::cout << "1. Saludar" << std::endl;
        std::cout << "2. Despedirse" << std::endl;
        std::cout << "3. Salir" << std::endl;
        std::cout << "Selecciona una opcion: ";
        std::cin >> opcion;

        switch (opcion) {
            case 1:
                std::cout << "¡Hola! Bienvenido." << std::endl;
                break;
            case 2:
                std::cout << "¡Adios! Que te vaya bien." << std::endl;
                break;
            case 3:
                std::cout << "Saliendo del programa." << std::endl;
                break;
            default:
                std::cout << "Opcion no valida. Intentalo de nuevo." << std::endl;
                break;
        }
    } while (opcion != 3);

    return 0;
}



//Ejercicio 7
#include <iostream>

float calcularAreaRectangulo(float base, float altura);

int main() {
    float base, altura, area;

    std::cout << "Ingresa la base del rectangulo: ";
    std::cin >> base;
    std::cout << "Ingresa la altura del rectangulo: ";
    std::cin >> altura;

    area = calcularAreaRectangulo(base, altura);

    std::cout << "El area del rectangulo es: " << area << std::endl;

    return 0;
}

float calcularAreaRectangulo(float base, float altura) {
    return base * altura;
}



//Ejercicio 8
#include <iostream>
void modificarPorValor(int numero) {
    numero = numero + 10;
    std::cout << "Dentro de modificarPorValor: " << numero << std::endl;
}

void modificarPorReferencia(int &numero) {
    numero = numero + 10;
    std::cout << "Dentro de modificarPorReferencia: " << numero << std::endl;
}

int main() {
    int numero = 20;

    std::cout << "Valor inicial en main: " << numero << std::endl;

    modificarPorValor(numero);
    std::cout << "Valor despues de modificarPorValor: " << numero << std::endl;

    modificarPorReferencia(numero);
    std::cout << "Valor despues de modificarPorReferencia: " << numero << std::endl;

    return 0;
}



//Ejercicio 9
#include <iostream>
#include <vector>
#include <string>

int main() {
    std::vector<std::string> comidasFavoritas;
    std::string comida;

    for (int i = 0; i < 3; ++i) {
        std::cout << "Ingresa tu comida favorita #" << i + 1 << ": ";
        std::getline(std::cin >> std::ws, comida);
        comidasFavoritas.push_back(comida);
    }

    std::cout << "\nTus comidas favoritas son:" << std::endl;
    for (int i = 0; i < comidasFavoritas.size(); ++i) {
        std::cout << "- " << comidasFavoritas[i] << std::endl;
    }

    return 0;
}



//Ejercicio 10
#include <iostream>

const double PI = 3.14159;
void calcularPerimetro(double radio);

int main() {
    double radio;

    std::cout << "Ingresa el radio del circulo: ";
    std::cin >> radio;

    calcularPerimetro(radio);

    return 0;
}

void calcularPerimetro(double radio) {
    double perimetro = 2 * PI * radio;
    std::cout << "El perimetro del circulo es: " << perimetro << std::endl;
}