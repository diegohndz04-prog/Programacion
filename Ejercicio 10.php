<?php
echo "Presiona Enter para comenzar la cuenta regresiva...\n\n";
// Bucle para la cuenta regresiva desde 10 hasta 1
for ($i = 10; $i >= 1; $i--) {
    echo $i . "...\n";
    // Espera a que el usuario presione Enter
    readline(); 
}

// Mensaje final
echo "\n¡Feliz Año Nuevo! 🎉\n";
?>