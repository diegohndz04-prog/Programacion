<?php
// Pedimos al usuario que ingrese la temperatura
echo "Por favor, ingresa la temperatura en grados Celsius: ";
$temperatura = (int) readline();

// Clasificamos la temperatura
if ($temperatura < 10) {
    echo "❄️ Fría\n";
} elseif ($temperatura >= 10 && $temperatura <= 25) {
    echo "🌤️ Templada\n";
} else {
    echo "🔥 Calurosa\n";
}
?>