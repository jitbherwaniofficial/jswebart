
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


