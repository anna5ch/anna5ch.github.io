document.addEventListener("DOMContentLoaded", function() {
    // Load the header
    fetch('../includes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-placeholder').innerHTML = data;
        });

});