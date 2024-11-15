document.getElementById('language-toggle').addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default anchor behavior

    // Elements to toggle
    const heroTextEnglish = document.getElementById('hero-text-english');
    const heroTextHindi = document.getElementById('hero-text-hindi');
    const heroDescEnglish = document.getElementById('hero-desc-english');
    const heroDescHindi = document.getElementById('hero-desc-hindi');
    const navMenuEnglish = document.getElementById('nav-menu-english');
    const navMenuHindi = document.getElementById('nav-menu-hindi');
    const languageToggle = document.getElementById('language-toggle');

    // Toggle logic for sections that require language switching
    if (languageToggle.textContent.trim() === 'ENGLISH') {
        languageToggle.textContent = 'हिन्दी';
        heroTextEnglish.style.display = 'none';
        heroTextHindi.style.display = 'block';
        heroDescEnglish.style.display = 'none';
        heroDescHindi.style.display = 'block';
        navMenuEnglish.style.display = 'none';
        navMenuHindi.style.display = 'block';
    } else {
        languageToggle.textContent = 'ENGLISH';
        heroTextEnglish.style.display = 'block';
        heroTextHindi.style.display = 'none';
        heroDescEnglish.style.display = 'block';
        heroDescHindi.style.display = 'none';
        navMenuEnglish.style.display = 'block';
        navMenuHindi.style.display = 'none';
    }
});
