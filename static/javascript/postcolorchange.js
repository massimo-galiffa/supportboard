const select = document.querySelectorAll(".form-control");
select.forEach(function(element) {
  element.addEventListener("change", function () {
    const supportRequest = document.getElementById(`support-request-${element.id.split("-")[2]}`);
    if (element.value === "easy") {
      supportRequest.classList.remove("difficult");
      supportRequest.classList.add("easy");
    } else if (element.value === "difficult") {
      supportRequest.classList.remove("easy");
      supportRequest.classList.add("difficult");
    }
  });
});




