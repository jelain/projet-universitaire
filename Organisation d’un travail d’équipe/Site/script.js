document.addEventListener("DOMContentLoaded", function () {
  let sliderImages = document.querySelectorAll(".slider-image");
  let prevArrow = document.querySelector(".slider-arrow.prev");
  let nextArrow = document.querySelector(".slider-arrow.next");

  let currentIndex = 0;

  function showImage(index) {
    sliderImages.forEach((image) => (image.style.display = "none"));
    sliderImages[index].style.display = "block";
  }

  function showNextImage(event) {
    event.preventDefault();
    currentIndex = (currentIndex + 1) % sliderImages.length;
    showImage(currentIndex);
  }

  function showPrevImage(event) {
    event.preventDefault();
    currentIndex =
      (currentIndex - 1 + sliderImages.length) % sliderImages.length;
    showImage(currentIndex);
  }

  nextArrow.addEventListener("click", showNextImage);
  prevArrow.addEventListener("click", showPrevImage);
  showImage(currentIndex);
});
