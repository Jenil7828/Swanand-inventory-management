document.getElementById("toggleDarkMode").addEventListener("click", () => {
  // Toggle dark mode class
  document.body.classList.toggle("dark-mode");

  // Save theme preference in localStorage
  const isDark = document.body.classList.contains("dark-mode");
  localStorage.setItem("theme", isDark ? "dark" : "light");

  // Change the icon based on the mode
  document.getElementById("toggleDarkMode").textContent = isDark ? "☀️" : "🌙";
});

window.addEventListener("DOMContentLoaded", () => {
  // Check stored theme preference
  if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark-mode");
  }

  // Set the initial icon based on the theme
  document.getElementById("toggleDarkMode").textContent = document.body.classList.contains("dark-mode") ? "☀️" : "🌙";
});

// Sidebar toggle functionality
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  sidebar.classList.toggle("collapsed");

  const btn = document.querySelector(".toggle-sidebar");
  btn.style.left = sidebar.classList.contains("collapsed") ? '1rem' : '240px';
}
