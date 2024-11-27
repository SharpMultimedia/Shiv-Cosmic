

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 4,
    spaceBetween: 30,
    loop: true,
    speed: 5000,
    autoplay: {
        delay: 3000, // delay between slides
        disableOnInteraction: false, // keeps autoplay active after user interactions
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1024: {
            slidesPerView: 4,
        },
    },
});

// Select Swiper container and add event listeners
const swiperContainer = document.querySelector('.mySwiper');

swiperContainer.addEventListener('mouseenter', () => {
    if (swiper && swiper.autoplay) {
        swiper.autoplay.stop();
        // console.log('Autoplay stopped');
    }
});

swiperContainer.addEventListener('mouseleave', () => {
    if (swiper && swiper.autoplay) {
        swiper.autoplay.start();
        // console.log('Autoplay resumed');
    }
});


console.log('hey app.js');
