function scrollToElement(id, event) {
    event.preventDefault();
    const element = document.getElementById(id);
    const headerOffset = 100; 
    const elementPosition = element.getBoundingClientRect().top;
    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

    window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
    });
}