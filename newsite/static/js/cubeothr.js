let canvas = document.getElementById("mycanvas0");
canvas.width = 250; // фиксированный размер
canvas.height = 250;
let ctx = canvas.getContext("2d");

let isDragging = false; // флаг зажатой кнопки мыши
let prevMouseX = 0;
let prevMouseY = 0;
let mouseX = 0;
let mouseY = 0;

// Обработчик нажатия мыши
canvas.addEventListener("mousedown", function(event) {
  isDragging = true;
  prevMouseX = event.x;
  prevMouseY = event.y;
});

// Обработчик отпускания мыши
canvas.addEventListener("mouseup", function() {
  isDragging = false;
});

// Обработчик движения мыши
canvas.addEventListener("mousemove", function(event) {
  if(!isDragging) return; // вращаем только при зажатой мыши

  prevMouseX = mouseX;
  prevMouseY = mouseY;
  mouseX = event.x;
  mouseY = event.y;

  // Модифицируем чувствительность вращения
  let incrX = (mouseX - prevMouseX) * 0.01;
  let incrY = (mouseY - prevMouseY) * 0.01;

  rotateCuboid(incrX, incrY);
  drawCuboid();
});

// Инициализация объектов
let nodes = [
  [-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
  [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]
];

let edges = [
  [0, 1], [1, 3], [3, 2], [2, 0],
  [4, 5], [5, 7], [7, 6], [6, 4],
  [0, 4], [1, 5], [2, 6], [3, 7]
];

function scale(fx, fy, fz) {
  nodes.forEach(function(node) {
    node[0] *= fx;
    node[1] *= fy;
    node[2] *= fz;
  });
}

// Вращение кубика по X и Y
function rotateCuboid(angleX, angleY) {
  let sinX = Math.sin(angleX);
  let cosX = Math.cos(angleX);
  let sinY = Math.sin(angleY);
  let cosY = Math.cos(angleY);
  
  nodes.forEach(function(node) {
    let x = node[0];
    let y = node[1];
    let z = node[2];

    // Вращение вокруг X
    node[0] = x;
    node[1] = y * cosX - z * sinX;
    node[2] = y * sinX + z * cosX;

    // Вращение вокруг Y
    let nx = node[0];
    let ny = node[1];
    z = node[2];
    node[0] = nx * cosY + z * sinY;
    node[1] = ny;
    node[2] = -nx * sinY + z * cosY;
  });
}

function drawCuboid() {
  ctx.save();
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.translate(canvas.width / 2, canvas.height / 2);
  ctx.strokeStyle = "#fff";
  ctx.beginPath();
  edges.forEach(function(edge) {
    let p1 = nodes[edge[0]];
    let p2 = nodes[edge[1]];
    ctx.moveTo(p1[0], p1[1]);
    ctx.lineTo(p2[0], p2[1]);
  });
  ctx.stroke();
  ctx.restore();
}

// Инициализация
scale(20, 20, 20); // равномерное увеличение
rotateCuboid(Math.PI / 5, Math.PI / 9);
drawCuboid();