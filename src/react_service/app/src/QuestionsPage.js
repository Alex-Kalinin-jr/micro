import React, { useState, useEffect } from 'react';

export default function QuestionsPage() {
  const [categories, setCategories] = useState([]);
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [answers, setAnswers] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const categoriesResponse = await fetch('/data/categories');
        const categoriesData = await categoriesResponse.json();
        setCategories(categoriesData);

        const questionsResponse = await fetch('/data/questions');
        const questionsData = await questionsResponse.json();
        setQuestions(questionsData);
      } catch (error) {
        console.error('Error:', error);
      }
    }
    fetchData();
  }, []);

  const handleCategoryChange = (event) => {
    setSelectedCategory(event.target.value);
    setCurrentQuestionIndex(0);
  };

  const handleNextClick = () => {
    setCurrentQuestionIndex(currentQuestionIndex + 1);
  };

  const filteredQuestions = selectedCategory
    ? questions.filter((question) => question.category === selectedCategory)
    : [];

  const currentQuestion =
    filteredQuestions.length > 0 ? filteredQuestions[currentQuestionIndex] : null;

  const handleAnswerClick = async (answerId) => {
    try {
      const answersResponse = await fetch(`/data/answers/${answerId}`);
      const answersData = await answersResponse.json();
      setAnswers(answersData);
    } catch (error) {
      console.error('Error fetching answers:', error);
    }
  };

  return (
    <div id="tab2">
      <h2>Выбери один из вариантов ответа.</h2>
      <label htmlFor="category-combobox">Category:</label>
      <select id="category-combobox" value={selectedCategory} onChange={handleCategoryChange}>
        <option value="">Select a category</option>
        {categories.map((category, index) => (
          <option key={index} value={category}>
            {category}
          </option>
        ))}
      </select>

      {currentQuestion ? (
        <div>
          <div id="question">{currentQuestion.text}</div>
          <ul id="answers">
            {answers.map((answer, index) => (
              <li key={index} onClick={() => handleAnswerClick(answer.id)}>
                {answer.data}
              </li>
            ))}
          </ul>
          <div id="feedback">
            {answers.some((answer) => answer.is_right) ? 'Correct!' : 'Incorrect. Try again.'}
          </div>
          <button id="next-btn" style={{ display: 'block' }} onClick={handleNextClick}>
            Next
          </button>
        </div>
      ) : (
        <div id="question">No questions available for the selected category.</div>
      )}
    </div>
  );
}
