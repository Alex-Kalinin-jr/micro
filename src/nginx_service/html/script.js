
async function fetchLinksToGoodArticles() {
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


// async function fetchQuestionsAndAnswers() {
//     const questionElement = document.getElementById('question');
//     const answersElement = document.getElementById('answers');
//     const feedbackElement = document.getElementById('feedback');
//     const nextButton = document.getElementById('next-btn');

//     if (!questionElement || !answersElement || !feedbackElement || !nextButton) {
//         console.error('Required elements not found in the DOM.');
//         return;
//     }

//     let currentQuestionIndex = 0;
//     let questions = [];
//     let categories = [];

//     try {
//         // 
//         const categoryResponse = await fetch('/data/categories');
//         if (!categoryResponse.ok) throw new Error('Failed to fetch categories');
//         categories = await categoryResponse.json();
//         console.log(categories);
//         // 
//         const questionsResponse = await fetch('/data/questions');
//         if (!questionsResponse.ok) throw new Error('Failed to fetch questions');
//         questions = await questionsResponse.json();
//         displayQuestion();
//     } catch (error) {
//         console.error('Error:', error);
//         questionElement.textContent = 'Error loading questions.';
//     }

//     function displayQuestion() {
//         const question = questions[currentQuestionIndex];
//         questionElement.textContent = question.text;
//         answersElement.innerHTML = '';
//         feedbackElement.textContent = '';
//         nextButton.style.display = 'none';

//         fetch(`/data/answers/${question.id}`)
//             .then(response => {
//                 if (!response.ok) throw new Error('Failed to fetch answers');
//                 return response.json();
//             })
//             .then(answers => {
//                 answers.forEach(answer => {
//                     const answerItem = document.createElement('li');
//                     answerItem.textContent = answer.data;
//                     answerItem.addEventListener('click', () => {
//                         if (answer.is_right) {
//                             feedbackElement.textContent = 'Correct!';
//                         } else {
//                             feedbackElement.textContent = 'Incorrect. Try again.';
//                         }
//                         nextButton.style.display = 'block';
//                     });
//                     answersElement.appendChild(answerItem);
//                 });
//             })
//             .catch(error => {
//                 console.error('Error:', error);
//                 answersElement.innerHTML = '<li>Error loading answers.</li>';
//             });
//     }

//     nextButton.addEventListener('click', () => {
//         currentQuestionIndex++;
//         if (currentQuestionIndex < questions.length) {
//             displayQuestion();
//         } else {
//             questionElement.textContent = 'Quiz completed!';
//             answersElement.innerHTML = '';
//             feedbackElement.textContent = '';
//             nextButton.style.display = 'none';
//         }
//     });
// }

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

    async function loadTabContent(tabId) {
        try {
            const response = await fetch(`${tabId}.html`);
            if (!response.ok) throw new Error(`Failed to load ${tabId}`);
            const content = await response.text();
            document.getElementById("content").innerHTML = content;
    
            // Call the appropriate function based on the loaded tab
            if (tabId === 'tab1') {
                fetchLinksToGoodArticles();
            } else if (tabId === 'tab2') {
                // Wait for the content to be fully loaded before calling fetchQuestionsAndAnswers
                setTimeout(() => {
                    fetchQuestionsAndAnswers();
                }, 0);
            }
        } catch (error) {
            console.error('Error:', error);
            document.getElementById("content").innerHTML = `<p>Error loading ${tabId} content.</p>`;
        }
    }
    loadTabContent('tab1');
});






async function fetchQuestionsAndAnswers() {
    const questionElement = document.getElementById('question');
    const answersElement = document.getElementById('answers');
    const feedbackElement = document.getElementById('feedback');
    const nextButton = document.getElementById('next-btn');
    const categoryCombobox = document.getElementById('category-combobox');

    if (!questionElement || !answersElement || !feedbackElement || !nextButton || !categoryCombobox) {
        console.error('Required elements not found in the DOM.');
        return;
    }

    let currentQuestionIndex = 0;
    let questions = [];
    let categories = [];

    try {
        const categoryResponse = await fetch('/data/categories');
        if (!categoryResponse.ok) throw new Error('Failed to fetch categories');
        categories = await categoryResponse.json();
        console.log(categories);

        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category.id;
            option.textContent = category.name;
            categoryCombobox.appendChild(option);
        });

        const questionsResponse = await fetch('/data/questions');
        if (!questionsResponse.ok) throw new Error('Failed to fetch questions');
        questions = await questionsResponse.json();

        categoryCombobox.addEventListener('change', () => {
            currentQuestionIndex = 0;
            displayQuestion();
        });

        displayQuestion();
    } catch (error) {
        console.error('Error:', error);
        questionElement.textContent = 'Error loading questions.';
    }

    function displayQuestion() {
        const selectedCategoryId = categoryCombobox.value;
        const filteredQuestions = questions.filter(question => question.category_id === parseInt(selectedCategoryId));

        if (filteredQuestions.length === 0) {
            questionElement.textContent = 'No questions available for the selected category.';
            answersElement.innerHTML = '';
            feedbackElement.textContent = '';
            nextButton.style.display = 'none';
            return;
        }

        const question = filteredQuestions[currentQuestionIndex];
        questionElement.textContent = question.text;
        answersElement.innerHTML = '';
        feedbackElement.textContent = '';
        nextButton.style.display = 'none';

        fetch(`/data/answers/${question.id}`)
            .then(response => {
                if (!response.ok) throw new Error('Failed to fetch answers');
                return response.json();
            })
            .then(answers => {
                answers.forEach(answer => {
                    const answerItem = document.createElement('li');
                    answerItem.textContent = answer.data;
                    answerItem.addEventListener('click', () => {
                        if (answer.is_right) {
                            feedbackElement.textContent = 'Correct!';
                        } else {
                            feedbackElement.textContent = 'Incorrect. Try again.';
                        }
                        nextButton.style.display = 'block';
                    });
                    answersElement.appendChild(answerItem);
                });
            })
            .catch(error => {
                console.error('Error:', error);
                answersElement.innerHTML = '<li>Error loading answers.</li>';
            });
    }

    nextButton.addEventListener('click', () => {
        currentQuestionIndex++;
        const selectedCategoryId = categoryCombobox.value;
        const filteredQuestions = questions.filter(question => question.category_id === parseInt(selectedCategoryId));
        if (currentQuestionIndex < filteredQuestions.length) {
            displayQuestion();
        } else {
            questionElement.textContent = 'Quiz completed!';
            answersElement.innerHTML = '';
            feedbackElement.textContent = '';
            nextButton.style.display = 'none';
        }
    });
}