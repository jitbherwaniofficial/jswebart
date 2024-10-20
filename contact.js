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
