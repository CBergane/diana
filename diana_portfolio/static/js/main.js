document.addEventListener("DOMContentLoaded", function () {
    // LinkedIn Element
    const linkedinElement = document.getElementById('linkedinElement');
    if (linkedinElement) {
        const showLinkedinElementAt = 0.8;
        const body = document.body;
        const html = document.documentElement;
        window.addEventListener('scroll', function () {
            const documentHeight = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);
            const windowHeight = window.innerHeight || html.clientHeight || body.clientHeight;
            const windowBottom = windowHeight + window.pageYOffset;
            if (windowBottom >= documentHeight * showLinkedinElementAt) {
                linkedinElement.style.opacity = '1';
                linkedinElement.classList.add('bounce');
            } else {
                linkedinElement.style.opacity = '0';
                linkedinElement.classList.remove('bounce');
            }
        });
    } else {
        console.error('linkedinElement not found!');
    }

    // Menu Toggle
    const menuToggle = document.getElementById('menuToggle');
    const menuClose = document.getElementById('menuClose');
    const menu = document.getElementById('menu');
    if (menuToggle && menuClose && menu) {
        menuToggle.addEventListener('click', toggleMenu);
        menuClose.addEventListener('click', toggleMenu);
    } else {
        console.error('Menu Elements not found!');
    }

    // AOS and Swiper initialization
    AOS.init({ once: false });

    const swiper = new Swiper('.swiper-container', {
        direction: 'horizontal',
        loop: true,
        autoplay: {
            delay: 5000,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });
});

function toggleMenu() {
    const menu = document.getElementById('menu');
    const hamburger = document.getElementById('menuToggle');
    if (menu && hamburger) {
        if (menu.classList.contains('invisible')) {
            menu.classList.remove('invisible');
            hamburger.classList.add('active');
            setTimeout(function () {
                menu.classList.add('translate-x-0');
            }, 50);
        } else {
            menu.classList.remove('translate-x-0');
            hamburger.classList.remove('active');
            setTimeout(function () {
                menu.classList.add('invisible');
            }, 500);
        }
    }
}
