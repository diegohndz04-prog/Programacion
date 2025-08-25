<?php
// Inicializamos la variable para la suma en 0
$sumaImpares = 0;

// Recorremos los números del 1 al 100
for ($i = 1; $i <= 100; $i++) {
    // Verificamos si el número es impar
    if ($i % 2 != 0) {
        $sumaImpares += $i; // Sumamos el número impar
    }
}

// Mostramos el resultado
echo "La suma de todos los números impares del 1 al 100 es: " . $sumaImpares . "\n";
?>