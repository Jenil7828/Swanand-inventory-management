document.addEventListener("DOMContentLoaded", () => {
  const body = document.body;
  const toggle = document.getElementById("toggleDarkMode");

  // Check local storage for dark mode preference
  const isDark = localStorage.getItem("dark-mode") === "true";
  if (isDark) {
    body.classList.add("dark-mode");
    toggle.textContent = "☀️"; // Set icon to ☀️ when dark mode is active
  } else {
    toggle.textContent = "🌙"; // Set icon to 🌙 when light mode is active
  }

  // Toggle dark mode on button click
  toggle.addEventListener("click", () => {
    body.classList.toggle("dark-mode");
    const isNowDark = body.classList.contains("dark-mode");

    // Update localStorage with the current theme
    localStorage.setItem("dark-mode", isNowDark);

    // Change the icon based on the current theme
    toggle.textContent = isNowDark ? "☀️" : "🌙";
  });
});
