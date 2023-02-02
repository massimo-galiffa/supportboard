var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', ];
var i = 0;
setInterval(function() {
  var buttons = document.getElementsByClassName('rainbow-button');
  for (var button of buttons) {
    button.style.color = colors[i];
  }
  i = (i + 1) % colors.length;
}, 0.1);


