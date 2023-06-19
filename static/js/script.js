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

// Get all the Sub-Menu triggers
const accordionTriggers = document.querySelectorAll('.sub-menu-trigger');

// Attach click event listener to each accordion trigger
accordionTriggers.forEach((trigger) => {
  // Toggle the visibility of the Sub-Menu content on click
  trigger.addEventListener('click', () => {
    trigger.nextElementSibling.classList.toggle('hidden');
  });
});

// Carousel
document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".sliderAx > div");
  const prevButton = document.querySelector(".slider-button.prev");
  const nextButton = document.querySelector(".slider-button.next");
  let currentIndex = 0;

  function showSlide(index) {
    slides.forEach((slide) => {
      slide.classList.remove("active");
    });

    slides[index].classList.add("active");
  }

  function nextSlide() {
    currentIndex++;
    if (currentIndex >= slides.length) {
      currentIndex = 0;
    }
    showSlide(currentIndex);
  }

  function prevSlide() {
    currentIndex--;
    if (currentIndex < 0) {
      currentIndex = slides.length - 1;
    }
    showSlide(currentIndex);
  }

  function startCarousel() {
    setInterval(nextSlide, 5000); // Change slide every 5 seconds
  }

  // Event listeners for previous and next buttons
  prevButton.addEventListener("click", prevSlide);
  nextButton.addEventListener("click", nextSlide);

  // Start the carousel
  startCarousel();
});


// CONTACT FORM

/* 
 * Wait for the DOM to finish loading, and add form submit event listener
 * Code adapted from EmailJS tutorial at
 * https://www.emailjs.com/docs/tutorial/creating-contact-form/
 */

// EmailJS Contact Form
document.addEventListener('DOMContentLoaded', function () {
  const feedbackSubmit = document.getElementsByClassName("submit-contact-button");

  document.getElementById('contact-form').addEventListener('submit', function (event) {
      event.preventDefault();
      emailjs.init("LgGJwNhTPTHbw2LbP"); // https://dashboard.emailjs.com/admin/account

      // generate a five digit number for the contact_number variable EG. #7659
      this.contact_number.value = Math.random() * 100000 | 0;

      feedbackSubmit.value = 'Sending...';

      emailjs.sendForm('send_rainbow', 'sci_fi_quiz_feedback', this)
          .then(function () {
              feedbackSubmit.value = 'Send Email';
              showThankYou();
          }, function (error) {
              console.log(JSON.stringify(err));
          });
  });
});

/**
* Shows a thank you message in the form area once the form
* has been sent
* @function showThankYou
*/
function showThankYou() {
  let messageArea = document.getElementById('contact-container');
  let thankyouMessage = `
  <h2>YOUR MESSAGE HAS BEEN SENT</h2>
  <br>
  <p>Thank you for reaching out to us. We have received your message and will get back to you as soon as possible.</p>
  <p>In the meantime, feel free to explore our website for more information about our services and resources.</p>
  <p>Best regards,</p>
  <p>Your Website Team</p>`;

  messageArea.innerHTML = thankyouMessage;
}