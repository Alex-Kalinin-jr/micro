export async function getData(path) {
    const response = await fetch(path);
    if (!response.ok) {
        throw new Error('Failed to fetch', path);
    }
    let data = await response.json();
    return data;
}

export function getElementsForQuestionsFillings() {
    const questionElement = document.getElementById('question');
    const answersElement = document.getElementById('answers');
    const feedbackElement = document.getElementById('feedback');
    const nextButton = document.getElementById('next-btn');
    const categoryCombobox = document.getElementById('category-combobox');

    if (!questionElement || !answersElement || !feedbackElement || !nextButton || !categoryCombobox) {
        console.error('Required elements not found in the DOM.');
        return null;
    }

    return { questionElement, answersElement, feedbackElement, nextButton, categoryCombobox };
}

export function displayNoQuestionsAvailable(elements) {
    elements.questionElement.textContent = 'No questions available for the selected category.';
    elements.answersElement.innerHTML = '';
    elements.feedbackElement.textContent = '';
    elements.nextButton.style.display = 'none';
}

export function fillComboBox(combobox, categories) {
    categories.forEach(category => {
        const option = document.createElement('option');
        option.textContent = category;
        combobox.appendChild(option);
    });
}