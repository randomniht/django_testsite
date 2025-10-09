document.addEventListener('DOMContentLoaded', function() {


  const button = document.getElementById('randomButton');
  const total = parseInt(document.getElementById('elements-count').dataset.count, 10);

  button.addEventListener('click', function() {
    for (let i = 1; i <= total; i++) {
      const img = document.getElementById('image-' + i);
      if (img) {
        img.style.display = 'none';
      }
    }

    // Random
    const randomIndex = Math.floor(Math.random() * total) + 1;

    // watch random
    const selectedImage = document.getElementById('image-' + randomIndex);
    if (selectedImage) {
      selectedImage.style.display = 'block';
      selectedImage.style.width = '35%';
      selectedImage.style.height = '35%';


    }
  });
});
console.log("randomSkript.js work");