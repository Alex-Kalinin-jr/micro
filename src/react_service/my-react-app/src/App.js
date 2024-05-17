import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

import LinksPage from './LinksPage';
import QuestionsPage from './QuestionsPage';
import Tab3Page from './Tab3Page';

export default function App() {
  return (
    <Router>
      <div>
        <h1>Знания - сила!</h1>
        <ul className="tabs">
          <li><Link to="/links">Полезные сылки</Link></li>
          <li><Link to="/questions">Проверь себя</Link></li>
          <li><Link to="/tab3">Пока не придумал</Link></li>
        </ul>

        <Route path="/links" component={LinksPage} />
        <Route path="/questions" component={QuestionsPage} />
        <Route path="/tab3" component={Tab3Page} />
      </div>
    </Router>
  );
}
