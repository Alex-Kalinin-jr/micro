import {fetchLinksToGoodArticles} from "./article_script.js";
import {getData, getElementsForQuestionsFillings, displayNoQuestionsAvailable} from "./utils.js";
import {fillComboBox} from "./utils.js";


document.addEventListener("DOMContentLoaded", () => {
    document.getElementById('tab1').addEventListener('click', (event) => {
        event.preventDefault();
        loadTabContent('tab1');
    });

    document.getElementById('tab2').addEventListener('click', (event) => {
        event.preventDefault();
        loadTabContent('tab2');
    });
    
    document.getElementById('tab3').addEventListener('click', (event) => {
        event.preventDefault();
        loadTabContent('tab3');
    });
    
    loadTabContent('tab1');
});


async function loadTabContent(tabId) {
    try {
        const response = await fetch(`${tabId}.html`);
        if (!response.ok)
            throw new Error(`Failed to load ${tabId}`);
        document.getElementById("content").innerHTML = await response.text();

        if (tabId === 'tab1') {
            fetchLinksToGoodArticles();
        } else if (tabId === 'tab2') {
            fetchQuestionsAndAnswers();
        }

    } catch (error) {
        console.error('Error:', error);
        document.getElementById("content").innerHTML = `<p>Error loading ${tabId} content.</p>`;
    }
}

var currentQuestionIndex = 0;

async function fetchQuestionsAndAnswers() {
    const elements = getElementsForQuestionsFillings();
    if (!elements) return;
    
    const categories = await getData('/data/categories');
    fillComboBox(elements.categoryCombobox, categories);
    
    let questions = await getData('/data/questions');

    elements.categoryCombobox.addEventListener('change', () => {
        currentQuestionIndex = 0;
        displayQuestion(elements, questions);
    });

    displayQuestion(elements, questions);

    elements.nextButton.addEventListener('click', () => {
        currentQuestionIndex++;
        displayQuestion(elements, questions);
    });
}


function displayQuestion(elements, questions) {
    const selectedCategoryId = elements.categoryCombobox.value;
    const filteredQuestions = questions.filter(question => question.category === selectedCategoryId);

    if (filteredQuestions.length === 0) {
        displayNoQuestionsAvailable(elements);
        return;
    }

    const question = filteredQuestions[currentQuestionIndex];
    elements.questionElement.textContent = question.text;
    elements.answersElement.innerHTML = '';
    elements.feedbackElement.textContent = '';
    elements.nextButton.style.display = 'none';

    fetchAndDisplayAnswers(elements, question.id);
}


async function fetchAndDisplayAnswers(elements, questionId) {
    try {
        const answers = await getData(`/data/answers/${questionId}`);
        displayAnswers(elements, answers);
    } catch (error) {
        console.error('Error fetching answers:', error);
        elements.answersElement.innerHTML = '<li>Error loading answers.</li>';
    }
}


function displayAnswers(elements, answers) {
    elements.answersElement.innerHTML = '';

    answers.forEach(answer => {
        const answerItem = document.createElement('li');
        answerItem.textContent = answer.data;
        answerItem.addEventListener('click', () => {
            if (answer.is_right) {
                elements.feedbackElement.textContent = 'Correct!';
            } else {
                elements.feedbackElement.textContent = 'Incorrect. Try again.';
            }
            elements.nextButton.style.display = 'block';
        });
        elements.answersElement.appendChild(answerItem);
    });
}