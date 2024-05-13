async function fetchQuestionsAndAnswers() {
    const container = document.getElementById('qa-container');
    container.innerHTML = '';

    try {
        const questionsResponse = await fetch('/data/questions');
        if (!questionsResponse.ok) throw new Error('Failed to fetch questions');
        const questions = await questionsResponse.json();

        for (const question of questions) {
            const questionDiv = document.createElement('div');
            questionDiv.innerHTML = `<h2>${question.text}</h2>`;

            const answersResponse = await fetch(`/data/answers/${question.id}`);
            if (!answersResponse.ok) throw new Error('Failed to fetch answers');
            const answers = await answersResponse.json();

            const answersList = document.createElement('ul');
            for (const answer of answers) {
                const answerItem = document.createElement('li');
                answerItem.textContent = answer.data;
                answersList.appendChild(answerItem);
            }

            questionDiv.appendChild(answersList);
            container.appendChild(questionDiv);
        }
    } catch (error) {
        console.error('Error:', error);
        container.innerHTML = '<p>Error loading questions and answers.</p>';
    }
}

document.addEventListener("DOMContentLoaded", () => {
    async function loadTabContent(tabId) {
        try {
            const response = await fetch(`${tabId}.html`);
            if (!response.ok) throw new Error(`Failed to load ${tabId}`);
            const content = await response.text();
            document.getElementById("content").innerHTML = content;
        } catch (error) {
            console.error('Error:', error);
            document.getElementById("content").innerHTML = `<p>Error loading ${tabId} content.</p>`;
        }
    }

    document.getElementById('tab1').addEventListener('click', (event) => {
        event.preventDefault();
        loadTabContent('tab1');
    });

    document.getElementById('tab2').addEventListener('click', (event) => {
        event.preventDefault();
        loadTabContent('tab2').then(() => {
            fetchQuestionsAndAnswers();
        });
    });

    document.getElementById('tab3').addEventListener('click', (event) => {
        event.preventDefault();
        loadTabContent('tab3');
    });

    loadTabContent('tab1');
});