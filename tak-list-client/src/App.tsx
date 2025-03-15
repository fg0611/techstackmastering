import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import Home from './pages/Home';
import Tasks from './pages/tasks';

enum ROUTE_NAME {
  Home = 'home',
  Tasks = 'tasks'
}

function App() {
    return (
        <Router>
          <nav> <Link to='home'>Home</Link> | <Link to='Tasks'>Tasks</Link></nav>
          <Routes>
            <Route path={ROUTE_NAME.Home} element={<Home/>}></Route>
            <Route path={ROUTE_NAME.Tasks} element={<Tasks/>}></Route>
          </Routes>
        </Router>
    )
}

export default App;