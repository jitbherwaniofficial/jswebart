gsap.registerPlugin(ScrollTrigger);

const marquee = gsap.timeline({ repeat: -1, paused: true });
const marqueeContent = document.querySelector(".marquee-content");

// Duplicate content to create an infinite effect
const items = gsap.utils.toArray(".item");
const contentWidth = marqueeContent.offsetWidth;

items.forEach(item => {
  marqueeContent.appendChild(item.cloneNode(true));  // Duplicate items
});

// Animate marquee content
marquee.to(".marquee-content", {
  x: -contentWidth,    // Move the content to the left by its width
  ease: "none",        // Linear animation for smooth movement
  duration: 50,        // Adjust duration to control speed
  repeat: -1           // Infinite loop
}).play();
