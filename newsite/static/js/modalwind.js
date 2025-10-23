document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');

    // Открытие изображения
    document.querySelectorAll('.article-image').forEach(function(img) {
        img.addEventListener('click', function() {
            modal.style.display = 'flex';
            modalImg.src = this.src;
            modalImg.alt = this.alt;
            // сброс масштаба при открытии
            modalImg.style.transform = 'scale(1)';
        });
    });

    // Закрытие модалки
    modal.addEventListener('click', function(e) {
        if(e.target !== modalImg) {
            modal.style.display = 'none';
        }
    });

    // Обработка колесика мыши
    modal.addEventListener('wheel', function(e) {
        if (modal.style.display === 'flex') {
            e.preventDefault(); // отключить прокрутку страницы при активном увеличении изображения

            // Получаем текущий масштаб
            const style = window.getComputedStyle(modalImg);
            const matrix = new WebKitCSSMatrix(style.transform);
            let currentScale = matrix.a; // масштаб по X (по Y такой же для scale)

            // Определяем направление прокрутки
            const delta = Math.sign(e.deltaY);

            // Если прокрутка вверх — увеличиваем
            const scaleStep = 0.3; // шаг увеличения
            if (delta < 0) {
                currentScale += scaleStep;
            } else {
                // Можно оставить, чтобы только увеличивать
                currentScale -= scaleStep; // для уменьшения
            }

            // Ограничения: минимальный и максимальный масштаб
            const minScale = 1;
            const maxScale = 10;
            currentScale = Math.max(minScale, Math.min(maxScale, currentScale));

            // Устанавливаем масштаб
            modalImg.style.transform = `scale(${currentScale})`;
        }
    }, { passive: false });
});