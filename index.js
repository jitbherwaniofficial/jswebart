
gsap.from("#logo img", {
    // y:-60,
    duration:1,
    // delay:0.3,
    rotate:-360,
    scrollTrigger: {
        trigger: "body",
        scroller: "body",
        // markers: true,
        start:"top 0%",
        // end: "top 30%",
        scrub: true,
    }
})

gsap.from(".company_name", {
    y:60,
    duration:1,
    delay:0.3
})

gsap.to("#company_marque #company_marque_name", {
    transform: "translateX(-60%)",
    scrollTrigger: {
        trigger: "#company_marque",
        scroller: "body",
        start:"top 0%",
        end:"top -100%",
        scrub: 2,
        pin:true,
    }
})


gsap.from("#featured_work_section #fw_one", {
    opacity: 0,
    duration:2,
    scrollTrigger: {
        trigger: "#featured_work_section #fw_one",
        scroller: "body",
        // markers: true,
        start:"top 60%",
        end: "top 10%",
        scrub: true,
    }
})

gsap.from("#featured_work_section #fw_two", {
    opacity: 0,
    duration:2,
    scrollTrigger: {
        trigger: "#featured_work_section #fw_two",
        scroller: "body",
        // markers: true,
        start:"top 60%",
        end: "top 10%",
        scrub: true,
    }
})

gsap.from("#featured_work_section #fw_three", {
    opacity: 0,
    duration:2,
    scrollTrigger: {
        trigger: "#featured_work_section #fw_three",
        scroller: "body",
        // markers: true,
        start:"top 60%",
        end: "top 10%",
        scrub: true,
    }
})

gsap.from("#featured_work_section #fw_four", {
    opacity: 0,
    duration:2,
    scrollTrigger: {
        trigger: "#featured_work_section #fw_four",
        scroller: "body",
        // markers: true,
        start:"top 60%",
        end: "top 10%",
        scrub: true,
    }
})

