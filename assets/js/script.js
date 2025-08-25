/* AOS (Animate On Scroll) */
AOS.init({
  duration: 800,
  easing: 'ease-in-out',
  once: true
});

/* CONTACT FORM VALIDATION */
(() => {
  const form = document.getElementById('contactForm');
  if (!form) return;
  form.addEventListener('submit', event => {
    if (!form.checkValidity()) {
      event.preventDefault();
      event.stopPropagation();
    } else {
      event.preventDefault();
      alert('Thank you! Your message has been sent.');
      form.reset();
    }
    form.classList.add('was-validated');
  }, false);
})();

/* NAVBAR SHRINK ON SCROLL */
window.addEventListener('scroll', () => {
  const nav = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
});