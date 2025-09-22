// Effet visuel au clic sur "Supprimer"
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".delete-btn").forEach(button => {
        button.addEventListener("click", () => {
            // petit effet avant redirection
            button.parentElement.style.opacity = "0.5";
        });
    });
});
