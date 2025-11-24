console.log("JS loaded");

// Получение контекста канваса
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d"); // рисовать типо

// Загрузка изображений
const ground = new Image();
ground.src = "/media/game/snake/area.png";

const foodImg = new Image();
foodImg.src = "/media/game/snake/apple.png";

let imagesLoaded = 0;
const totalImages = 2;

// Обработчики загрузки изображений
ground.onload = checkImagesLoaded;
foodImg.onload = checkImagesLoaded;


document.addEventListener("keydown", function(event) {
    // Отменяем стандартное поведение стрелочных клавиш
    if (
        event.keyCode === 37 || // стрелка влево
        event.keyCode === 38 || // стрелка вверх
        event.keyCode === 39 || // стрелка вправо
        event.keyCode === 40    // стрелка вниз
    ) {
        event.preventDefault();
    }

    // Ваша логика обработки направления
    direction(event);
});



// Check img download
function checkImagesLoaded() {
    imagesLoaded++;
    if (imagesLoaded === totalImages) {
        startGame(); // if download => start game
    }
}

const box = 32; // 1 jacheyka razmer cell size
let score = 0;

// начальное положение змейки
let snake = [{ x: 9 * box, y: 10 * box }]; 
// начальное положение еды
let food = {
    x: Math.floor((Math.random() * 15 + 1)) * box,
    y: Math.floor((Math.random() * 15 + 3)) * box,
};
let dir; // переменная для хранения текущего направления движения змейки по умолчанию она стоит если что
let game; // интервал скорость мейби

// Keyboard processing(obrabotka)
document.addEventListener("keydown", direction);

// Obrabotka najatiy
function direction(event) {
    if (event.keyCode == 37 && dir != "right") dir = "left";
    else if (event.keyCode == 38 && dir != "down") dir = "up";
    else if (event.keyCode == 39 && dir != "left") dir = "right";
    else if (event.keyCode == 40 && dir != "up") dir = "down";
}

// Проверка столкновения с хвостом
function eatTail(head, arr) {
    for (let i = 0; i < arr.length; i++) {
        if (head.x == arr[i].x && head.y == arr[i].y) {
            clearInterval(game); // игра закончена
        }
    }
}

// Основная функция отрисовки и логики игры
function drawGame() {
    ctx.drawImage(ground, 0, 0); //метод для отрисовки
    ctx.drawImage(foodImg, food.x, food.y, 25, 25);//метод для жратвы

// раскраска
    for (let i = 0; i < snake.length; i++) {
        ctx.fillStyle = i === 0 ? "yellow" : "white"; // цвет
        ctx.fillRect(snake[i].x, snake[i].y, box, box);
    }

    ctx.fillStyle = "white";
    ctx.font = "50px Arial";
    ctx.fillText(score, box * 2.5, box * 1.7);

    let snakeX = snake[0].x;
    let snakeY = snake[0].y;

    // Проверка поедания еды
    if (snakeX == food.x && snakeY == food.y) {
        score++;
        // Генерация новой позиции для еды
        // Генерация еды внутри границ
    food = {
    x: Math.floor(Math.random() * 15 + 3) * box, // от 3 до 15
    y: Math.floor(Math.random() * 15 + 3) * box, // от 3 до 15
    };
    } else {
        snake.pop(); // убираем хвост, если не поел 
    }

    // Проверка столкновения с границами
    if (snakeX < box || snakeX > box * 17 || snakeY < 3 * box || snakeY > box * 17) {
        clearInterval(game); // игра закончена
    }

    // Обновление координат головы
    if (dir == "left") snakeX -= box;
    if (dir == "right") snakeX += box;
    if (dir == "up") snakeY -= box;
    if (dir == "down") snakeY += box;

    let newHead = { x: snakeX, y: snakeY };
    eatTail(newHead, snake); // проверка на столкновение с хвостом
    snake.unshift(newHead); // добавляем новую голову в начало массива
}

// Старт игры
function startGame() {
    console.log("Game started");
}

// Получаем кнопку по ID
const restartBtn = document.getElementById("restartBtn");

// Обработчик на кнопку
restartBtn.addEventListener("click", restartGame);

function restartGame() {
    clearInterval(game); // останавливаем текущий интервал
    // Сбрасываем все переменные, связанные с игрой
    score = 0;
    snake = [{ x: 9 * box, y: 10 * box }];
    dir = undefined; // или начальное направление
    // Генерируем новую позицию еды
    food = {
    x: Math.floor(Math.random() * 15 + 3) * box,
    y: Math.floor(Math.random() * 15 + 3) * box,
    };
    // Запускаем игру заново
    game = setInterval(drawGame, 100);
}