import React from 'react'; // Импортируем React из библиотеки react
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'; // импортируем компонент UserList.
import axios from 'axios';

class App extends React.Component {  // Создадим класс App, наследуем его от React.Component.
                                     // Компонент App — это класс, имеющий состояние.
   constructor(props) {    // В конструктор класса передаётся объект props
       super(props)        // super(props) — вызывает родительский конструктор
       this.state = {      // this.state — это объект состояния нашего компонента.
           'users': []   // Он будет хранить массив пользователей, которые мы будем получать с back-end.

       }
   }

   componentDidMount() {   // Мы получаем объект response и его данные response.data.
                           // Это и есть список пользователей из API на back-end.
                           // Далее меняем состояние объекта App и передаём полученные данные.
   axios.get('http://127.0.0.1:8000/api/users/')
       .then(response => {
           const users = response.data
               this.setState(
               {
                   'users': users
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
           <div>
               <UserList users={this.state.users} />
           </div>
       )
   }

}

export default App;   // Экспортируем наш компонент для использования в других модулях.
