tailwind.config = {
  darkMode: 'class',
}
  
  
// grab everything we need
const btn = document.querySelector("button.mobile-menu-button");
const menu = document.querySelector(".mobile-menu");

// add event listeners
btn.addEventListener("click", () => {
  menu.classList.toggle("hidden");
});

// Dark mode
function darkModeListener() {
  document.querySelector("html").classList.toggle("dark");
}
document.querySelector("input[type='checkbox']#dark-toggle").addEventListener("click", darkModeListener);

// Back to top button
const BackToTop = document.createElement('div');
BackToTop.classList.add('back-to-top');
document.body.appendChild(BackToTop);

window.addEventListener('scroll', function() {
    if (window.pageYOffset > 20) {
        BackToTop.classList.add('show');
    } else {
        BackToTop.classList.remove('show');
    }
});

document.body.addEventListener('click', function(event) {
    if (event.target.classList.contains('back-to-top')) {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
});