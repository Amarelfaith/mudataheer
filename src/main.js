// Mobile Menu Toggle
const mobileBtn = document.getElementById('mobile-menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

mobileBtn.addEventListener('click', () => {
  if (mobileMenu.classList.contains('hidden')) {
    mobileMenu.classList.remove('hidden');
    mobileMenu.classList.add('block');
  } else {
    mobileMenu.classList.add('hidden');
    mobileMenu.classList.remove('block');
  }
});

// Close mobile menu when clicking a link
const mobileLinks = mobileMenu.querySelectorAll('a');
mobileLinks.forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.add('hidden');
    mobileMenu.classList.remove('block');
  });
});

// Navbar Scroll Effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar.classList.add('shadow-md');
  } else {
    navbar.classList.remove('shadow-md');
  }
});

// Advanced scroll animations using IntersectionObserver
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.1
};

const observer = new IntersectionObserver((entries, observer) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('opacity-100', 'translate-y-0');
      entry.target.classList.remove('opacity-0', 'translate-y-10');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Add animation classes to elements we want to animate
const animatedElements = document.querySelectorAll('section > div');

animatedElements.forEach((el, index) => {
  // Add base transition classes first
  el.classList.add('transition-all', 'duration-1000', 'ease-out', 'opacity-0', 'translate-y-10');

  // Stagger delays slightly based on index just in case they appear at same time
  el.style.transitionDelay = `${(index % 3) * 150}ms`;

  observer.observe(el);
});
