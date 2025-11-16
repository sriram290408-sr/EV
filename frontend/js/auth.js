document.addEventListener('DOMContentLoaded', function() {
    // Check if the user is logged in
    const isLoggedIn = localStorage.getItem('isLoggedIn');

    // If not logged in and not on the login page, redirect to login
    if (isLoggedIn !== 'true' && !window.location.href.endsWith('index.html')) {
        // Adjust the path to index.html based on the current file's location
        if (window.location.pathname.includes('/pages/')) {
            window.location.href = '../index.html';
        } else {
            window.location.href = 'index.html';
        }
    }

    // Handle logout functionality
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            localStorage.removeItem('isLoggedIn');
            // Adjust the path for redirection after logout
            if (window.location.pathname.includes('/pages/')) {
                window.location.href = '../index.html';
            } else {
                window.location.href = 'index.html';
            }
        });
    }
});