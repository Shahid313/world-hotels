let CancelButton = document.querySelector(".cancel")
let flashBackground = document.querySelector(".flash-background")

CancelButton.addEventListener("click", function() {
  flashBackground.style.visibility = "hidden"
})