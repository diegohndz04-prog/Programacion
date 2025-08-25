<?php
// Definimos el número para la tabla
$numero = 8;

// Encabezado de la tabla
echo "--- Tabla de Multiplicar del " . $numero . " ---\n";

// Recorremos del 1 al 10 para cada multiplicación
for ($i = 1; $i <= 10; $i++) {
    $resultado = $numero * $i;
    echo $numero . " x " . $i . " = " . $resultado . "\n";
}
?>