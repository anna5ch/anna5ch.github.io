document.addEventListener("DOMContentLoaded", function() {
    // Load the header
    fetch('../includes/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-placeholder').innerHTML = data;
        });

});