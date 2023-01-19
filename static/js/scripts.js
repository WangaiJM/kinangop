// hamburger

const hamburger = document.querySelector("#hamburger");
const nav = document.querySelector(".nav");

hamburger.addEventListener("click", () => {
  nav.classList.toggle("active");
});

// carousel
const next = document.querySelector(".next");
const prev = document.querySelector(".prev");
const images = document.querySelectorAll(".carousel-item");

let current = 0;

next.addEventListener("click", nextSlide);
prev.addEventListener("click", prevSlide);

function nextSlide() {
  current++;

  if (current > images.length - 1) {
    current = 0;
  }

  images.forEach((img) => {
    img.classList.remove("active");
  });

  image = images[current];

  console.log(image);
  image.classList.add("active");
}

function prevSlide() {
  current--;

  if (current < 0) {
    current = images.length - 1;
  }

  images.forEach((img) => {
    img.classList.remove("active");
  });

  image = images[current];

  image.classList.add("active");
}

setInterval(nextSlide, 5000);
