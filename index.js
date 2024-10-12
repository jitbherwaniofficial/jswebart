
let lastScrollTop = 0;
const header = document.querySelector('#header');
let isScrolling;

window.addEventListener('scroll', function() {
  window.clearTimeout(isScrolling);

  isScrolling = setTimeout(() => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
      header.classList.add('hidden');
    } 
    else {
      header.classList.remove('hidden');
    }

    lastScrollTop = scrollTop;
  }, 50);
});



gsap.from("#logo img", {
    duration:1,
    rotate:-360,
    scrollTrigger: {
        trigger: "body",
        scroller: "body",
        start:"top 0%",
        scrub: true,
    }
})


gsap.from("#absolute_logo img", {
    duration:1,
    rotate:-360,
    scrollTrigger: {
        trigger: "body",
        scroller: "body",
        start:"top 0%",
        scrub: true,
    }
})

gsap.from(".company_name", {
    y:60,
    duration:1,
    delay:0.3
})

// gsap.to("#company_marque #company_marque_name", {
//     transform: "translateX(-60%)",
//     scrollTrigger: {
//         trigger: "#company_marque",
//         scroller: "body",
//         start:"top 14%",
//         end:"top -100%",
//         scrub: 2,
//         pin:true,
//     }
// })

// COUNTER *********************************************************** //
function counter() {
    const valueDisplays = document.querySelectorAll("#counter_box h2"); // Target the h2 elements directly

    valueDisplays.forEach((valueDisplay) => {
        const endValue = parseInt(valueDisplay.getAttribute("data-val"));

        // Create GSAP animation for the counter
        const counterAnimation = gsap.to(valueDisplay, {
            innerText: endValue,
            duration: 2,
            roundProps: "innerText",
            ease: "power1.inOut",
            paused: true, // Keep it paused until ScrollTrigger
            onStart: () => {
                valueDisplay.classList.add("counting"); // Optional: add class to indicate counting started
            },
        });

        // Set up ScrollTrigger
        ScrollTrigger.create({
            trigger: valueDisplay,
            start: "top 80%", // Adjust this based on your layout
            onEnter: () => {
                if (!valueDisplay.classList.contains("counting")) {
                    counterAnimation.play();
                }
            },
            once: true, // Ensures it plays only once
        });
    });
}

counter(); // Call the counter function
// COUNTER *********************************************************** //


// ACCORDION //
// let questions = document.querySelectorAll(".service_name_container");

// // Open the first accordion by default
// if (questions.length > 0) {
//   const firstQuestion = questions[0];
//   const firstIcon = firstQuestion.querySelector(".icon-shape");
//   const firstAnswer = firstQuestion.nextElementSibling;

//   // Add the 'active' class to the first question and icon
//   firstQuestion.classList.add("active");
//   firstIcon.classList.add("active");

//   // Set the maxHeight for the first answer
//   firstAnswer.style.maxHeight = "23vw";
// }

// questions.forEach((question) => {
//   let icon = question.querySelector(".icon-shape");

//   question.addEventListener("click", (event) => {
//     const active = document.querySelector(".service_name_container.active");
//     const activeIcon = document.querySelector(".icon-shape.active");

//     if (active && active !== question) {
//       active.classList.toggle("active");
//       activeIcon.classList.toggle("active");
//       active.nextElementSibling.style.maxHeight = 0;
//     }

//     question.classList.toggle("active");
//     icon.classList.toggle("active");

//     const answer = question.nextElementSibling;
    
//     if (question.classList.contains("active")) {
//       answer.style.maxHeight = "23vw";
//     } else {
//       answer.style.maxHeight = 0;
//     }
//   });
  
// });
// ACCORDION //


// ACCORDION //
let questions = document.querySelectorAll(".faq_question");

questions.forEach((question) => {
  let icon = question.querySelector(".icon-shape");

  question.addEventListener("click", (event) => {
    const active = document.querySelector(".faq_question.active");
    const activeIcon = document.querySelector(".icon-shape.active");

    if (active && active !== question) {
      active.classList.toggle("active");
      activeIcon.classList.toggle("active");
      active.nextElementSibling.style.maxHeight = 0;
    }

    question.classList.toggle("active");
    icon.classList.toggle("active");

    const answer = question.nextElementSibling;

    if (question.classList.contains("active")) {
      answer.style.maxHeight = answer.scrollHeight + "px";
    } else {
      answer.style.maxHeight = 0;
    }
  });
});
// ACCORDION //

const swiper = new Swiper('.swiper-container', {
  grabCursor: true, // Enable grab effect
  loop: false,       // Enable continuous loop mode
  spaceBetween: -114, // Space between slides
  breakpoints: {
    768: {
      spaceBetween: -70
    },
    430: {
      spaceBetween: -70
    },
    400: {
      spaceBetween:-50
    }
  },
  slidesPerView: 1, // Number of slides to show at once
  pagination: {
    el: '.swiper-pagination',
    clickable: true, // Make pagination bullets clickable
  },
  navigation: {
    nextEl: '.swiper-button-next', // Navigation arrows
    prevEl: '.swiper-button-prev',
  },
});

// Get all the pill elements
const pills = document.querySelectorAll('.pill');

// Add click event listener for each pill
pills.forEach(pill => {
  pill.addEventListener('click', function(event) {
    event.preventDefault();  // Prevent default anchor behavior

    // Remove active class from all pills
    pills.forEach(p => p.classList.remove('active'));

    // Add active class to the clicked pill
    this.classList.add('active');

    // Get the slide index from the data attribute
    const slideIndex = this.getAttribute('data-slide');
    
    // Use Swiper's slideTo method to go to the desired slide
    swiper.slideTo(slideIndex);
  });
});


const swiperTwo = new Swiper('.swiper-container-two', {
  grabCursor: true, // Enable grab effect
  loop: false,       // Enable continuous loop mode
  spaceBetween: -114, // Space between slides
  breakpoints: {
    768: {
      spaceBetween: -70
    },
    430: {
      spaceBetween: -70
    }
  },
  slidesPerView: 1, // Number of slides to show at once
  pagination: {
    el: '.swiper-pagination',
    clickable: true, // Make pagination bullets clickable
  },
  navigation: {
    nextEl: '.swiper-button-next', // Navigation arrows
    prevEl: '.swiper-button-prev',
  },
});

// Get all the pill elements
const businessPill = document.querySelectorAll('.business_pill');

// Add click event listener for each pill
businessPill.forEach(pill => {
  pill.addEventListener('click', function(event) {
    event.preventDefault();  // Prevent default behavior
    
    // Remove active class from all pills
    businessPill.forEach(p => p.classList.remove('active'));

    // Add active class to the clicked pill
    this.classList.add('active');

    // Get the slide index from the data attribute
    const slideIndex = this.getAttribute('data-slider');
    
    // Use Swiper's slideTo method to go to the desired slide
    swiperTwo.slideTo(slideIndex);
  });
});

gsap.to(".testimonials", {
  y: "-350%",
    duration: 15, 
  ease: "none", 
  repeat: -1, 
});

const burger = document.querySelector('.burger');
burger.addEventListener('click', function() {
  this.classList.toggle('active');
  const mob_nav = document.querySelector('#mobile_nav')
  mob_nav.classList.toggle('active')
})

const service_arrow = document.querySelector('#service_btn')
service_arrow.addEventListener('click', function() {  
  this.classList.toggle('active')
  const service_link_container = document.querySelector('.service_link_container')
  service_link_container.classList.toggle('active')
})




