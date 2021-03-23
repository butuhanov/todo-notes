import React from 'react'; // Импортируем React из библиотеки react
import './App.css';
import UserList from './components/User.js'; // импортируем компонент UserList.
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import axios from 'axios';


const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}

class App extends React.Component {  // Создадим класс App, наследуем его от React.Component.
                                     // Компонент App — это класс, имеющий состояние.
   constructor(props) {    // В конструктор класса передаётся объект props
       super(props)        // super(props) — вызывает родительский конструктор
       this.state = {      // this.state — это объект состояния нашего компонента.
           'users': [],   // Он будет хранить массив пользователей, которые мы будем получать с back-end.
           'projects': [],
           'todos': [],

       }
   }

   componentDidMount() {   // Мы получаем объект response и его данные response.data.
                           // Это и есть список пользователей из API на back-end.
                           // Далее меняем состояние объекта App и передаём полученные данные.
   axios.get('http://127.0.0.1:8000/api/user/')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
               }
           )
       }).catch(error => console.log(error));

   axios.get('http://127.0.0.1:8000/api/project/')
       .then(response => {
           const projects = response.data.results
               this.setState(
               {
                   'projects': projects
               }
           )
       }).catch(error => console.log(error));

   axios.get('http://127.0.0.1:8000/api/todo/')
       .then(response => {
           const todos = response.data.results
               this.setState(
               {
                   'todos': todos
               }
           )
       }).catch(error => console.log(error))
}


render () {
           // Отрисовываем компонент App,
           // который включает в себя компонент UserList,
           // и передаём в UserList данные
           // о пользователях {this.state.users}.
       return (
          <div className="App">
          <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/users'>Список пользователей</Link>
              </li>
              <li>
                <Link to='/projects'>Список проектов</Link>
              </li>
              <li>
                <Link to='/todos'>Список задач</Link>
              </li>

            </ul>
          </nav>
            <Switch>
              <Route exact path='/users' component={() => <UserList users={this.state.users} />}  />
              <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />}  />
              <Route exact path='/todos' component={() => <TodoList todos={this.state.todos} />}  />
              <Route path="/users/:id">
                <UserList users={this.state.users} />
              </Route>
              <Redirect from='/authors' to='/' />
              <Route component={NotFound404} />
            </Switch>
          </BrowserRouter>
        </div>

       )
   }

}

export default App;   // Экспортируем наш компонент для использования в других модулях.
