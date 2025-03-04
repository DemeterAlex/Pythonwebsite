document.addEventListener("DOMContentLoaded", () => {
    loadQuote();
});

function loadQuote() {
    fetch("/api/quote")
        .then(response => response.json())
        .then(data => {
            document.getElementById("dynamic-text").innerText = data.quote;
        })
        .catch(error => {
            console.error("Chyba při načítání citátu:", error);
        });
}
