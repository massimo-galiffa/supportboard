var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', ];
var i = 0;
setInterval(function() {
  var buttons = document.getElementsByClassName('rainbow-button');
  for (var button of buttons) {
    button.style.transition = "color 0.5s ease-in-out";
    button.style.color = colors[i];
  }
  i = (i + 1) % colors.length;
}, 1000);


