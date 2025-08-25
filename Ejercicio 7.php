<?php
// Pedimos al usuario que ingrese un número
echo "Por favor, ingresa un número: ";
$numero = (int) readline();

// Verificamos si el número es positivo, negativo o cero
if ($numero > 0) {
    echo "El número " . $numero . " es positivo.\n";
} elseif ($numero < 0) {
    echo "El número " . $numero . " es negativo.\n";
} else {
    echo "El número es cero.\n";
}
?>