// ------- contact us dropdown button ----- 
document.getElementById("dropdownButton").addEventListener("click", function () {
    const wrapper = document.getElementById("dropdownWrapper");
    const dropdownMenu = document.getElementById("dropdownMenu");

    // Toggle dropdown menu visibility
    dropdownMenu.classList.toggle("hidden");
    dropdownMenu.classList.toggle("show");

    // Adjust the wrapper's bottom property
    if (dropdownMenu.classList.contains("show")) {
        wrapper.style.bottom = "145px"; // Dropdown open
    } else {
        wrapper.style.bottom = "30px"; // Dropdown closed
    }
});


//  Social icons toggle button open / close 

document.addEventListener("DOMContentLoaded", function () {
    const toggleIcon = document.querySelector(".toggleIcon");
    const socialIcons = document.querySelectorAll(".mobileviewSocial ul li:not(.toggleIcon)");
    const toggleIconSymbol = toggleIcon.querySelector("i");

    toggleIcon.addEventListener("click", () => {
        socialIcons.forEach(icon => {
            icon.classList.toggle("visible");
        });

        // Toggle the "+" and "-" icon
        if (toggleIconSymbol.classList.contains("fa-plus")) {
            toggleIconSymbol.classList.replace("fa-plus", "fa-minus");
        } else {
            toggleIconSymbol.classList.replace("fa-minus", "fa-plus");
        }
    });
});


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






