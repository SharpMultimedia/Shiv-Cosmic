


// Navigation 

function Menu(e) {
    let list = document.querySelector('ul');
    if (e.querySelector('i').classList.contains('fa-bars')) {
        e.querySelector('i').classList.remove('fa-bars');
        e.querySelector('i').classList.add('fa-times');
        list.classList.add('open');
        list.style.position = 'absolute';
    } else {
        closeMenu(); // Calls the function to close the menu
    }
}

function closeMenu() {
    let list = document.querySelector('ul');
    let menuIcon = document.querySelector('.fa-times');
    if (menuIcon) {
        menuIcon.classList.remove('fa-times');
        menuIcon.classList.add('fa-bars');
    }
    list.classList.remove('open');
}


// testimonial slider 

var swiper = new Swiper(".testimonial-slider", {
    slidesPerView: 3,
    spaceBetween: 30,
    loop: true,
    speed: 9000,
    // autoplay: {
    //     delay: 1,
    //     disableOnInteraction: false
    // },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
    },
    breakpoints: {
        320: {
            slidesPerView: 1,
        },
        1024: {
            slidesPerView: 2,
            spaceBetween: 20
        },
        1280: {
            slidesPerView: 3,
            spaceBetween: 30
        }
    }
});

