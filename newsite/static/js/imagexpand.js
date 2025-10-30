// Обработка кнопки развернуть/свернуть для картинок
document.querySelectorAll('.expand-btn').forEach(button => {
    button.addEventListener('click', function() {
        const articleId = this.getAttribute('data-article-id');
        const image = document.getElementById('image-' + articleId);
        const isExpanded = this.getAttribute('data-expanded') === 'true';
        
        if (!isExpanded) {
            // Развернуть - показываем 35% высоты картинки
            const originalHeight = image.naturalHeight;
            const halfHeight = originalHeight * 0.3;
            image.style.maxHeight = halfHeight + 'px';
            this.textContent = 'Свернуть ▼';
            this.setAttribute('data-expanded', 'true');
        } else {
            // Свернуть 
            image.style.maxHeight = '150px';
            this.textContent = 'Развернуть ▲';
            this.setAttribute('data-expanded', 'false');
        }
    });
});