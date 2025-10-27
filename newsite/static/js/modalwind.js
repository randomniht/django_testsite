document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImage');

    let isDragging = false; // состояние перетаскивания
    let startX = 0;
    let startY = 0;
    let currentTranslateX = 0;
    let currentTranslateY = 0;

    // Открытие изображения
    document.querySelectorAll('.article-image').forEach(function(img) {
        img.addEventListener('click', function() {
            modal.style.display = 'flex';
            modalImg.src = this.src;
            modalImg.alt = this.alt;
            modalImg.style.transform = 'scale(1) translate(0, 0)'; // сброс масштаба и положения
            currentTranslateX = 0;
            currentTranslateY = 0;
        });
    });

    // Закрытие модалки при клике за пределами изображения
    modal.addEventListener('click', function(e) {
        if (e.target !== modalImg && e.target !== modal.querySelector('#closeButton')) {
            modal.style.display = 'none';
            // сбросить позицию при закрытии
            modalImg.style.transform = 'scale(1) translate(0, 0)';
        }
    });

    // Обработка колесика мыши для масштабирования
    modal.addEventListener('wheel', function(e) {
        if (modal.style.display === 'flex') {
            e.preventDefault();
            const style = window.getComputedStyle(modalImg);
            const matrix = new WebKitCSSMatrix(style.transform);
            let currentScale = matrix.a;

            const delta = Math.sign(e.deltaY);
            const scaleStep = 0.3;

            if (delta < 0) {
                currentScale += scaleStep;
            } else {
                currentScale -= scaleStep;
            }

            const minScale = 1;
            const maxScale = 10;
            currentScale = Math.max(minScale, Math.min(maxScale, currentScale));

            // Важное: сохраняем текущий сдвиг при масштабировании
            modalImg.style.transform = `scale(${currentScale}) translate(${currentTranslateX}px, ${currentTranslateY}px)`;
        }
    }, { passive: false });

    // Обработка перетаскивания
    modalImg.addEventListener('mousedown', function(e) {
        e.preventDefault();

        isDragging = true;
        startX = (e.clientX - currentTranslateX);
        startY = (e.clientY - currentTranslateY);

        // Добавляем слушатели для перемещения и отпускания мыши
        document.addEventListener('mousemove', onMouseMove);
        document.addEventListener('mouseup', onMouseUp);
    });

const dragSensitivity = 0.5; // или любое другое значение < 1 для замедления

function onMouseMove(e) {
    if (!isDragging) return;

    // Вычисляем смещение с учетом чувствительности
    currentTranslateX = (e.clientX - startX) * dragSensitivity;
    currentTranslateY = (e.clientY - startY) * dragSensitivity;

    // Получение текущего масштаба
    const style = window.getComputedStyle(modalImg);
    const matrix = new WebKitCSSMatrix(style.transform);
    const currentScale = matrix.a;

    // Обновляем трансформацию
    modalImg.style.transform = `scale(${currentScale}) translate(${currentTranslateX}px, ${currentTranslateY}px)`;
}

    function onMouseUp() {
        isDragging = false;
        document.removeEventListener('mousemove', onMouseMove);
        document.removeEventListener('mouseup', onMouseUp);
    }

});