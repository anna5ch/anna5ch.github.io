document.addEventListener("DOMContentLoaded", function() {
    fetch('includes/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-placeholder').innerHTML = data;
        })
        .catch(error => console.error("Fehler beim Laden des Footers:", error));

});


