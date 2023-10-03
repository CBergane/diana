document.addEventListener("DOMContentLoaded", function () {
    // LinkedIn Element
    const linkedinElement = document.getElementById('linkedinElement');
    if (!linkedinElement) console.error('linkedinElement not found!');

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
    }

    // Menu Toggle
    

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




