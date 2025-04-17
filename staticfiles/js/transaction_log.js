// Sidebar toggle
function toggleSidebar() {
  const sidebar = document.getElementById("sidebar");
  const btn = document.querySelector(".toggle-sidebar");
  sidebar.classList.toggle("collapsed");
  btn.style.left = sidebar.classList.contains("collapsed") ? '1rem' : '240px';
}

// Dark mode toggle and persistence + icon change
const toggleBtn = document.getElementById("toggleDarkMode");

toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
  const isDark = document.body.classList.contains("dark-mode");
  localStorage.setItem("theme", isDark ? "dark" : "light");
  toggleBtn.textContent = isDark ? "☀️" : "🌙";
});

// Load theme from localStorage and update icon
window.addEventListener("DOMContentLoaded", () => {
  const isDark = localStorage.getItem("theme") === "dark";
  if (isDark) {
    document.body.classList.add("dark-mode");
    toggleBtn.textContent = "☀️";
  } else {
    toggleBtn.textContent = "🌙";
  }

  // Set active nav link
  const currentUrl = window.location.pathname;
  document.querySelectorAll('.sidebar a').forEach(link => {
    if (link.href.includes(currentUrl)) {
      link.classList.add('active');
    }
  });
});
