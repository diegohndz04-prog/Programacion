<?php

// Pedimos al usuario que ingrese un número
echo "Ingresa un número para clasificarlo: ";
$numero = (int) readline();

// Verificamos las condiciones para el número ingresado
if ($numero % 3 == 0 && $numero % 5 == 0) {
    echo "El número " . $numero . " es 'MarTierra'\n";
} elseif ($numero % 3 == 0) {
    echo "El número " . $numero . " es 'Mar'\n";
} elseif ($numero % 5 == 0) {
    echo "El número " . $numero . " es 'Tierra'\n";
} else {
    echo "El número " . $numero . " no es múltiplo de 3 ni de 5, por lo tanto, es el número mismo.\n";
}
?>