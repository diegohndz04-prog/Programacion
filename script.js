script.js
document.addEventListener('DOMContentLoaded', () => {
    // 1. Efecto de llenado de las barras de habilidades
    const skillBars = document.querySelectorAll('.skill-bar');

    // Recorre cada barra de habilidad
    skillBars.forEach(bar => {
        // Obtiene el valor 'width' del atributo 'style'
        const finalWidth = bar.style.width; 
        // Reinicia el ancho a 0 para la animación
        bar.style.width = '0%';
        // Con un pequeño retraso, establece el ancho final
        setTimeout(() => {
            bar.style.width = finalWidth;
        }, 500); 
    });

    // 2. Cambio de título dinámico en la pestaña del navegador
    const originalTitle = document.title;
    const newTitle = "¡Bienvenido a mi Portafolio!"; 

    // Al pasar el cursor sobre la pestaña, cambia el título
    window.addEventListener('blur', () => {
        document.title = newTitle;
    });

    // Al volver a la pestaña, restaura el título original
    window.addEventListener('focus', () => {
        document.title = originalTitle;
    });
});