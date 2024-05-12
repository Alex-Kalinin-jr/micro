async function fetchQuestionsAndAnswers() {
    const container = document.getElementById('qa-container');
    container.innerHTML = '';  // Clear previous content

    try {
        // Fetch all questions
        const questionsResponse = await fetch('http://localhost:8001/questions');
        if (!questionsResponse.ok) throw new Error('Failed to fetch questions');
        const questions = await questionsResponse.json();

        // Iterate over each question
        for (const question of questions) {
            const questionDiv = document.createElement('div');
            questionDiv.innerHTML = `<h2>${question.text}</h2>`;

            // Fetch answers for the question
            const answersResponse = await fetch(`http://localhost:8001/answers/${question.id}`);
            if (!answersResponse.ok) throw new Error('Failed to fetch answers');
            const answers = await answersResponse.json();

            const answersList = document.createElement('ul');
            for (const answer of answers) {
                const answerItem = document.createElement('li');
                answerItem.textContent = answer.text;  // Assuming 'text' field for answers
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

// Load questions and answers when the page is loaded
document.addEventListener('DOMContentLoaded', fetchQuestionsAndAnswers);