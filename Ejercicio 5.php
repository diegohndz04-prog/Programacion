<?php
// Pedimos al usuario que ingrese su edad
echo "Por favor, ingresa tu edad: ";
$edad = (int) readline();

// Verificamos la edad con las condiciones
if ($edad >= 18 && $edad <= 65) {
    echo "¡Felicidades! Con " . $edad . " años, cumples con los requisitos para obtener una licencia de conducir.\n";
} else {
    echo "Lo sentimos. Con " . $edad . " años, no cumples con los requisitos para obtener una licencia de conducir.\n";
}

?>