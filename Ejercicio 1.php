<?php
// Inicializamos los contadores
$pares = 0;
$impares = 0;

// Recorremos los números del 1 al 50
for ($i = 1; $i <= 50; $i++) {
    // Verificamos si el número es par (el residuo de la división por 2 es 0)
    if ($i % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

// Mostramos los resultados
echo "Cantidad de números pares del 1 al 50: " . $pares . "\n";
echo "Cantidad de números impares del 1 al 50: " . $impares . "\n";
?>