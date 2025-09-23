document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", (e) => {
            e.preventDefault(); // Empêche la redirection immédiate
            const taskItem = button.closest("li"); // cible le <li> de la tâche
            taskItem.style.transition = "opacity 0.5s";
            taskItem.style.opacity = "0"; // effet de disparition
            setTimeout(() => {
                window.location.href = button.href; // redirige après l’animation
            }, 500); // attend 0.5s avant la suppression réelle
        });
    });
});
