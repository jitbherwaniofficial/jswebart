gsap.from("#logo img", {
  duration: 1,
  rotate: -360,
  scrollTrigger: {
    trigger: "body",
    scroller: "body",
    start: "top 0%",
    scrub: true,
  },
});

gsap.from("#absolute_logo img", {
  duration: 1,
  rotate: -360,
  scrollTrigger: {
    trigger: "body",
    scroller: "body",
    start: "top 0%",
    scrub: true,
  },
});

const tl = gsap.timeline({
  default: {
    duration: 2,
  },
});

tl.from(".company_name", {
  y: 60,
  stagger: 0.2,
});

gsap.from(".strip", {
  duration: 1,
  // opacity: 0,
  stagger: 0.2,
  ease: "power2.out",
  y: 1600,
});

gsap.from(".w_line", {
  duration: 2,
  height: 0,
  scrollTrigger: {
    trigger: ".w_line",
    scroller: "body",
    start: "top 60%",
    end: "top 25%",
    scrub: 5,
  },
});

gsap.from(".w_hor", {
  duration: 2,
  width: 0,
  scrollTrigger: {
    trigger: ".w_hor",
    scroller: "body",
    start: "top 60%",
    end: "top 25%",
    scrub: 5,
  },
});

gsap.from(".w2_line", {
  duration: 2,
  height: 0,
  scrollTrigger: {
    trigger: ".w2_line",
    scroller: "body",
    start: "top 60%",
    end: "top 25%",
    scrub: 5,
  },
});

gsap.from(".w2_hor", {
  duration: 2,
  width: 0,
  scrollTrigger: {
    trigger: ".w2_hor",
    scroller: "body",
    start: "top 60%",
    end: "top 25%",
    scrub: 5,
  },
});

gsap.from(".w3_line", {
  duration: 2,
  height: 0,
  scrollTrigger: {
    trigger: ".w3_line",
    scroller: "body",
    start: "top 60%",
    end: "top 25%",
    scrub: 5,
  },
});

gsap.from(".w3_hor", {
  duration: 2,
  width: 0,
  scrollTrigger: {
    trigger: ".w3_hor",
    scroller: "body",
    start: "top 60%",
    end: "top 25%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor1", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor1",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});



gsap.to("#featured_work_anchor2", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor2",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor3", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor3",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor4", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor4",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor5", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor5",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor6", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor6",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor7", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor7",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

gsap.to("#featured_work_anchor8", {
  duration: 2,
  scale: 1,
  scrollTrigger: {
    trigger: "#featured_work_anchor8",
    scroller: "body",
    start: "top 100%",
    end: "top 90%",
    scrub: 5,
  },
});

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

const swiper = new Swiper(".swiper-container", {
  grabCursor: true, // Enable grab effect
  loop: false, // Enable continuous loop mode
  spaceBetween: -114, // Space between slides
  breakpoints: {
    768: {
      spaceBetween: -40,
    },
    430: {
      spaceBetween: 0,
    },
    400: {
      spaceBetween: 0,
    },
    375: {
      spaceBetween: -5,
    },
    360: {
      spaceBetween: 0,
    },
  },
  slidesPerView: 1, // Number of slides to show at once
  pagination: {
    el: ".swiper-pagination",
    clickable: true, // Make pagination bullets clickable
  },
  navigation: {
    nextEl: ".swiper-button-next", // Navigation arrows
    prevEl: ".swiper-button-prev",
  },
});

// Get all the pill elements
const pills = document.querySelectorAll(".pill");

// Add click event listener for each pill
pills.forEach((pill) => {
  pill.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default anchor behavior

    // Remove active class from all pills
    pills.forEach((p) => p.classList.remove("active"));

    // Add active class to the clicked pill
    this.classList.add("active");

    // Get the slide index from the data attribute
    const slideIndex = this.getAttribute("data-slide");

    // Use Swiper's slideTo method to go to the desired slide
    swiper.slideTo(slideIndex);
  });
});

const swiperTwo = new Swiper(".swiper-container-two", {
  grabCursor: true, // Enable grab effect
  loop: false, // Enable continuous loop mode
  spaceBetween: -114, // Space between slides
  breakpoints: {
    768: {
      spaceBetween: -40,
    },
    430: {
      spaceBetween: -20,
    },
    400: {
      spaceBetween: -10,
    },
    375: {
      spaceBetween: -20,
    },
    360: {
      spaceBetween: -5,
    },
  },
  slidesPerView: 1, // Number of slides to show at once
  pagination: {
    el: ".swiper-pagination",
    clickable: true, // Make pagination bullets clickable
  },
  navigation: {
    nextEl: ".swiper-button-next", // Navigation arrows
    prevEl: ".swiper-button-prev",
  },
});

// Get all the pill elements
const businessPill = document.querySelectorAll(".business_pill");

// Add click event listener for each pill
businessPill.forEach((pill) => {
  pill.addEventListener("click", function (event) {
    event.preventDefault(); // Prevent default behavior

    // Remove active class from all pills
    businessPill.forEach((p) => p.classList.remove("active"));

    // Add active class to the clicked pill
    this.classList.add("active");

    // Get the slide index from the data attribute
    const slideIndex = this.getAttribute("data-slider");

    // Use Swiper's slideTo method to go to the desired slide
    swiperTwo.slideTo(slideIndex);
  });
});

// gsap.to(".testimonials", {
//   y: "-350%",
//   duration: 15,
//   ease: "none",
//   repeat: -1,
// });

// gsap.to(".testimonials_mob", {
//   x: "-290%",
//   duration: 15,
//   ease: "none",
//   repeat: -1,
// });

function applyGsapAnimations() {
  // Clear any existing GSAP animations
  gsap.killTweensOf(".testimonials");
  gsap.killTweensOf(".testimonials_mob");

  if (window.innerWidth > 768) {
    // Apply the animation for .testimonials if the viewport is greater than 768px
    gsap.to(".testimonials", {
      y: "-350%",
      duration: 15,
      ease: "linear",
      repeat: -1,
    });
  } else {
    // Apply the animation for .testimonials_mob if the viewport is 768px or less
    gsap.to(".testimonials_mob", {
      x: "-290%",
      duration: 15,
      ease: "linear",
      repeat: -1,
    });
  }
}

// Debounce function to limit how often a function is called
function debounce(func, wait) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

// Run the function on page load
applyGsapAnimations();

// Add debounced event listener to handle window resize
window.addEventListener("resize", debounce(applyGsapAnimations, 200));
