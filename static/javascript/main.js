
// Navigation

function Menu(e) {
    let list = document.querySelector('.menuList');
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
    let list = document.querySelector('.menuList');
    let menuIcon = document.querySelector('.fa-times');
    if (menuIcon) {
        menuIcon.classList.remove('fa-times');
        menuIcon.classList.add('fa-bars');
    }
    list.classList.remove('open');
}

// Toggle dropdown on mobile view
document.querySelectorAll('.relative').forEach(item => {
    item.addEventListener('click', function () {
        if (window.innerWidth <= 767) {
            this.classList.toggle('open');
        }
    });
});



// ------ sticky navigation ------ 

let lastScrollTop = 0;
const navbar = document.getElementById('navbar');

window.addEventListener('scroll', () => {
    const scrollTop = window.scrollY;

    // Change navbar background on scroll
    if (scrollTop > 0) {
        navbar.style.backgroundColor = '#AE633F'; // Change to your desired color
    } else {
        navbar.style.backgroundColor = 'transparent'; // Restore transparency
    }

    // Throttle scroll event to reduce flickering
    if (Math.abs(scrollTop - lastScrollTop) > 5) {
        lastScrollTop = scrollTop;
    }
});


// ---------------- faqs ------------- 

const items = document.querySelectorAll('.accordion button');

function toggleAccordion() {
    const itemToggle = this.getAttribute('aria-expanded');

    for (i = 0; i < items.length; i++) {
        items[i].setAttribute('aria-expanded', 'false');
    }

    if (itemToggle == 'false') {
        this.setAttribute('aria-expanded', 'true');
    }
}

items.forEach((item) => item.addEventListener('click', toggleAccordion));

// astroTalk div hide & show 

let isScrolling;

window.addEventListener('scroll', () => {
    clearTimeout(isScrolling);

    isScrolling = setTimeout(() => {
        const navbar = document.getElementById('astroTalk');
        if (window.scrollY > 0) {
            navbar.style.display = 'none';
        } else {
            navbar.style.display = 'flex';
        }
    }, 50); // Adjust this value as needed
});




// --------- Testimonial slider ----------

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




// -------------- 


function changeInfo(option) {
    // Hide all content sections
    document.getElementById('basicKundli').style.display = 'none';
    document.getElementById('proKundli').style.display = 'none';
    document.getElementById('proNumerology').style.display = 'none';
    document.getElementById('astroVastu').style.display = 'none';

    // Show selected option
    document.getElementById(option).style.display = 'block';
}


// ------------- 


document.addEventListener("DOMContentLoaded", function () {
    // Get the selected plan from localStorage
    const selectedPlan = localStorage.getItem("selectedPlan");

    if (selectedPlan === "Numerology") {
        // Hide specific input fields
        document.getElementById("hourDiv").closest("div").style.display = "none";
        document.getElementById("minDiv").closest("div").style.display = "none";
        document.getElementById("placeDiv").closest("div").style.display = "none";
    }
});
  