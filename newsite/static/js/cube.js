
    (function () {
 var canvas = document.getElementById("cubeCanvas");
 var size = Math.min (canvas.width,canvas.height);
 var g = canvas.getContext("2d");
 var nodes = //Вершины
  [[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
   [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]];
 var edges = //грани
  [[0, 1], [1, 3], [3, 2], [2, 0], [4, 5], [5, 7], [7, 6],
   [6, 4], [0, 4], [1, 5], [2, 6], [3, 7]];
 
 function scale (factor0, factor1, factor2) { //масштабирование по осям
  nodes.forEach(function (node) {
   node[0] *= factor0; node[1] *= factor1; node[2] *= factor2;
  });
 }
 
 function rotateCuboid (angleX, angleY) { //пересчёт координат вершин для вращения
  var sinX = Math.sin(angleX);
  var cosX = Math.cos(angleX);
  var sinY = Math.sin(angleY);
  var cosY = Math.cos(angleY);
  nodes.forEach(function (node) {
   var x = node[0]; var y = node[1]; var z = node[2];
   node[0] = x * cosX - z * sinX;
   node[2] = z * cosX + x * sinX;
   z = node[2];
   node[1] = y * cosY - z * sinY;
   node[2] = z * cosY + y * sinY;
  });
 }
 
 function drawCuboid () {
  g.save();
  g.clearRect(0, 0, canvas.width, canvas.height); //очистить канву
  g.translate(canvas.width / 2, canvas.height / 2); //сместить в центр куба начало координат
  g.strokeStyle = "#ff8c00ff"; //цвет граней
  g.beginPath();
  edges.forEach(function (edge) {
   var p1 = nodes[edge[0]];
   var p2 = nodes[edge[1]];
   g.moveTo(p1[0], p1[1]);
   g.lineTo(p2[0], p2[1]);
  });
  g.closePath();
  g.stroke();
  g.restore();
 }
 
 scale (size/3.5, size/3.5, size/3.5); //масштаб указан здесь!
 rotateCuboid (Math.PI / 4, Math.atan(Math.sqrt(4))); //угол определён здесь!
 setInterval( function() {
  rotateCuboid (Math.PI / 60, Math.PI / 30); //поворот при вращении задан здесь!
  drawCuboid ();
 }, 10);
})(); 