document.addEventListener("DOMContentLoaded", function() {
    var showPopupButton = document.getElementById("showPopup");
    var popup = document.getElementById("popup");

showPopupButton.addEventListener("click", function(event) {
    event.preventDefault();
    popup.style.display = "block";
});

document.addEventListener("click", function(event) {
    if (!popup.contains(event.target) && event.target !== showPopupButton) {
        popup.style.display = "none";
        }
    });
});