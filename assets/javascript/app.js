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

    // Helper function to update the view based on screen size
    const updateView = () => {
        if (window.innerWidth > 768) {
            // Desktop view: Icons visible by default, toggle shows minus
            socialIcons.forEach(icon => icon.classList.add("visible"));
            toggleIconSymbol.classList.replace("fa-plus", "fa-minus");
        } else {
            // Mobile view: Icons hidden by default, toggle shows plus
            socialIcons.forEach(icon => icon.classList.remove("visible"));
            toggleIconSymbol.classList.replace("fa-minus", "fa-plus");
        }
    };

    // Toggle functionality for both mobile and desktop views
    toggleIcon.addEventListener("click", () => {
        const isAnyIconVisible = Array.from(socialIcons).some(icon => icon.classList.contains("visible"));

        if (isAnyIconVisible) {
            // Hide icons and switch to plus
            socialIcons.forEach(icon => icon.classList.remove("visible"));
            socialIcons.forEach(icon => icon.classList.add("hiddenn"));
            toggleIconSymbol.classList.replace("fa-minus", "fa-plus");
        } else {
            // Show icons and switch to minus
            socialIcons.forEach(icon => icon.classList.add("visible"));
            socialIcons.forEach(icon => icon.classList.remove("hiddenn"));
            toggleIconSymbol.classList.replace("fa-plus", "fa-minus");
        }
    });

    // Handle resizing to update view
    window.addEventListener("resize", updateView);

    // Initial setup
    updateView();
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






