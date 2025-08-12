document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript file loaded. DOM is ready.");

    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;


    if (!themeToggle) {
        console.error("Theme toggle button not found on the page!");
        return; 
    }

    function applyTheme(theme) {
        if (theme === 'light') {
            body.classList.add('light-mode');
            themeToggle.innerHTML = '<i class="fa-solid fa-sun"></i>';
        } else {
            body.classList.remove('light-mode');
            themeToggle.innerHTML = '<i class="fa-solid fa-moon"></i>';
        }
        localStorage.setItem('theme', theme);
    }

    function getInitialTheme() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            return savedTheme;
        }
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }

    const initialTheme = getInitialTheme();
    applyTheme(initialTheme);

    themeToggle.addEventListener('click', function() {
        console.log("Theme toggle button was clicked!"); 
        const isLight = body.classList.contains('light-mode');
        applyTheme(isLight ? 'dark' : 'light');
    });
});