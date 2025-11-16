document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("loginForm");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");

  // Example test credentials (you can replace these)
  const VALID_USERNAME = "admin";
  const VALID_PASSWORD = "12345";

  form.addEventListener("submit", (event) => {
    event.preventDefault(); // Stop page reload

    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    // Simple input validation
    if (username === "" || password === "") {
      showAlert("Please enter both username and password.", "error");
      return;
    }

    // Check credentials
    if (username === VALID_USERNAME && password === VALID_PASSWORD) {
      showAlert("Login successful! Redirecting...", "success");

      // Save user data to localStorage
      localStorage.setItem("loggedInUser", username);

      // Redirect after 1.5 seconds
      setTimeout(() => {
        window.location.href = "./pages/dashboard.html";
      }, 1500);
    } else {
      showAlert("Invalid username or password!", "error");
    }
  });

  // Display alert message dynamically
  function showAlert(message, type) {
    // Remove old alert if exists
    const existing = document.querySelector(".alert");
    if (existing) existing.remove();

    const alertBox = document.createElement("div");
    alertBox.className = `alert ${type}`;
    alertBox.textContent = message;
    form.parentNode.insertBefore(alertBox, form);

    // Auto-remove alert after 3 seconds
    setTimeout(() => alertBox.remove(), 3000);
  }
});
