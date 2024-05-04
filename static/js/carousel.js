// Define global variables
let currentSlideIndex = 0;
const slides = document.querySelectorAll('.carousel-item');
const numSlides = slides.length;
const interval = 2000; // Interval in milliseconds (5 seconds)

// Function to show the specified slide
function showSlide(index) {
    // Hide all slides
    slides.forEach((slide, i) => {
        slide.classList.remove('active');
    });

    // Show the specified slide
    slides[index].classList.add('active');
}

// Function to move to the next slide
function nextSlide() {
    currentSlideIndex = (currentSlideIndex + 1) % numSlides;
    showSlide(currentSlideIndex);
}

// Function to move to the previous slide
function prevSlide() {
    currentSlideIndex = (currentSlideIndex - 1 + numSlides) % numSlides;
    showSlide(currentSlideIndex);
}

// Set an interval to automatically change slides
setInterval(nextSlide, interval);

// Add event listeners for the carousel navigation buttons
document.querySelector('.carousel-control-prev').addEventListener('click', prevSlide);
document.querySelector('.carousel-control-next').addEventListener('click', nextSlide);
