export async function fetchLinksToGoodArticles() {
    const articleElement = document.getElementById('linksBlock');

    let links = [];

    try {
        const linksResponse = await fetch('/data/links');
        if (!linksResponse.ok) throw new Error('Failed to fetch links');
        links = await linksResponse.json();
        displayArticles();
    } catch (error) {
        console.error('Error:', error);
        articleElement.textContent = 'Error loading articles.';
    }

    function displayArticles() {
        links.forEach(link => {
            const explanationItem = document.createElement('li');
            explanationItem.textContent = link.explanation;
            articleElement.appendChild(explanationItem);
            
            const linkItem = document.createElement('a');
            linkItem.setAttribute('href', link.data);
            linkItem.textContent = "jump";
            articleElement.appendChild(linkItem);
        });
    }
}
