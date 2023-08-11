var indexValue = 0;
function SlideShow() {
    setTimeout(SlideShow, 3500)
    var x;
    const elements = document.querySelectorAll('.slider__img');
    for (x = 0; x < elements.length; x++) {
        elements[x].style.display = "none";
    }
    indexValue++;
    if (indexValue > elements.length) {
        indexValue = 1;
    }
    elements[indexValue - 1].style.display = "block";
}
SlideShow();