document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    let query = document.getElementById('searchInput').value;
    fetch('/search?query=' + encodeURIComponent(query))
        .then(response => response.json())
        .then(data => {
            let resultsDiv = document.getElementById('searchResults');
            resultsDiv.innerHTML = '';
            data.forEach(result => {
                let resultItem = document.createElement('div');
                resultItem.textContent = result;
                resultsDiv.appendChild(resultItem);
            });
        })
        .catch(error => console.error('Error:', error));
});
