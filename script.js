const toggleMenu = () => navbarMenu.classList.toggle("show-menu");
const hideMenu = () => hamburgerBtn.click();
const togglePopup = () => document.body.classList.toggle("show-popup");
const hidePopup = () => showPopupBtn.click();

hamburgerBtn.addEventListener("click", toggleMenu);
hideMenuBtn.addEventListener("click", hideMenu);
showPopupBtn.addEventListener("click", togglePopup);
hidePopupBtn.addEventListener("click", hidePopup);

formPopup.querySelectorAll(".bottom-link a").forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        const isSignupLink = link.id === 'signup-link';
        formPopup.classList.toggle("show-signup", isSignupLink);
    });
});