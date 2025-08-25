<?php
// Definimos el tamaño del cuadrado
$tamano = 5;

// Bucle para las filas
for ($i = 0; $i < $tamano; $i++) {
    // Bucle para las columnas
    for ($j = 0; $j < $tamano; $j++) {
        echo "# ";
    }
    echo "\n"; // Salto de línea para pasar a la siguiente fila
}
?>