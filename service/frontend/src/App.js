import React from 'react'; // Импортируем React из библиотеки react
import './App.css';
import UserList from './components/User.js'; // импортируем компонент UserList.
import ProjectList from './components/Project.js';
import TodoList from './components/Todo.js';
import {BrowserRouter, Route, Link, Switch, Redirect} from 'react-router-dom'
import axios from 'axios';
import LoginForm from './components/Auth.js'
import Cookies from 'universal-cookie';


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

  set_token(token) {
  // Метод set_token в классе App принимает токен, устанавливает его в cookies и записывает в состояние приложения.
  // Токен в cookies нужен для сохранения пользователя при закрытии браузера,
  // а токен в состоянии — для обновления приложения React при авторизации пользователя.
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token': token})
  }

  is_authenticated() {
  // Метод is_authenticated будет определять, авторизован пользователь или нет.
  // Он авторизован, если токен в состоянии не пустой.

  // Expected '!==' and instead saw '!='  eqeqeq
  // To ignore, add
  // eslint-disable-next-line
    return this.state.token != ''
  }

  logout() {
  // Метод logout будет обнулять токен.
    this.set_token('')
  }

  get_token_from_storage() {
  // Метод get_token_from_storage нужен нам, когда мы снова открываем страницу сайта.
  // Он считывает токен из cookies и записывает его в состояние.
  // Таким образом при первом открытии страницы мы узнаем, был ли ранее авторизован пользователь
    const cookies = new Cookies()
    const token = cookies.get('token')
    this.setState({'token': token})
  }

  get_token(username, password) {
  // После получения токена с backend вызываем this.set_token(response.data['token'])
  // для сохранения токена в cookies и state.
    axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
    .then(response => {
        this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }



   componentDidMount() {   // Мы получаем объект response и его данные response.data.
                           // Это и есть список пользователей из API на back-end.
                           // Далее меняем состояние объекта App и передаём полученные данные.

    this.get_token_from_storage()

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
              <li>
                    {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
              </li>
            </ul>
          </nav>
            <Switch>
              <Route exact path='/users' component={() => <UserList users={this.state.users} />}  />
              <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects} />}  />
              <Route exact path='/todos' component={() => <TodoList todos={this.state.todos} />}  />
              <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
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
