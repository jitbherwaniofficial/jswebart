
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
let questions = document.querySelectorAll(".service_name_container");

// Open the first accordion by default
if (questions.length > 0) {
  const firstQuestion = questions[0];
  const firstIcon = firstQuestion.querySelector(".icon-shape");
  const firstAnswer = firstQuestion.nextElementSibling;

  // Add the 'active' class to the first question and icon
  firstQuestion.classList.add("active");
  firstIcon.classList.add("active");

  // Set the maxHeight for the first answer
  firstAnswer.style.maxHeight = "23vw";
}

questions.forEach((question) => {
  let icon = question.querySelector(".icon-shape");

  question.addEventListener("click", (event) => {
    const active = document.querySelector(".service_name_container.active");
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
      answer.style.maxHeight = "23vw";
    } else {
      answer.style.maxHeight = 0;
    }
  });
  
});
// ACCORDION //

const swiper = new Swiper('.swiper-container', {
  grabCursor: true, // Enable grab effect
  loop: false,       // Enable continuous loop mode
  spaceBetween: -120, // Space between slides
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

