let lastScrollTop = 0;
const header = document.querySelector("#header");
let isScrolling;

window.addEventListener("scroll", function () {
  window.clearTimeout(isScrolling);

  isScrolling = setTimeout(() => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
      header.classList.add("hidden");
    } else {
      header.classList.remove("hidden");
    }

    lastScrollTop = scrollTop;
  }, 50);
});

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


const burger = document.querySelector(".burger");
burger.addEventListener("click", function () {
  this.classList.toggle("active");
  const mob_nav = document.querySelector("#mobile_nav");
  mob_nav.classList.toggle("active");
});

const service_arrow = document.querySelector("#service_btn");
service_arrow.addEventListener("click", function () {
  this.classList.toggle("active");
  const service_link_container = document.querySelector(
    ".service_link_container"
  );
  service_link_container.classList.toggle("active");
});


