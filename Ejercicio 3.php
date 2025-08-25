<?php
// Definimos el número secreto. Puedes cambiar este valor.
$numeroSecreto = 64;

// Inicializamos la variable del intento del usuario
$intento = 0;

echo "¡Bienvenido al juego 'Adivina el Número'!\n";
echo "Estoy pensando en un número entre 1 y 100. ¿Cuál es?\n\n";

// El bucle se ejecuta mientras el intento del usuario no sea el número secreto
while ($intento != $numeroSecreto) {
    // Pedimos al usuario que ingrese su intento
    echo "Adivina el número: ";
    $intento = (int) readline();

    // Comparamos el intento con el número secreto y damos una pista
    if ($intento < $numeroSecreto) {
        echo "¡El número que buscas es más grande! Intenta de nuevo.\n\n";
    } elseif ($intento > $numeroSecreto) {
        echo "¡El número que buscas es más pequeño! Intenta de nuevo.\n\n";
    }
}

echo "\n¡Felicidades! ¡Has adivinado el número! El número secreto era " . $numeroSecreto . ".\n";
?>