let currentSlide = 0;
const slides = document.querySelectorAll('.carousel-inner img');
const totalSlides = slides.length;
const carouselInner = document.querySelector('.carousel-inner');

setInterval(() => {
    currentSlide = (currentSlide + 1) % totalSlides;
    const moveLeftBy = -currentSlide * 100; // Slide width is 100% of viewport width
    carouselInner.style.transform = `translateX(${moveLeftBy}vw)`; 
}, 4000);  // Change slides every 3 seconds
