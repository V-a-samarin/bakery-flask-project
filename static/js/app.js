
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".auto-hide").forEach(el => {
        setTimeout(() => el.remove(), 3500);
    });
});
