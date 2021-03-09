import logo from './logo.svg';
import './App.css';
import React from 'react'; // Импортируем React из библиотеки react

class App extends React.Component {  // Создадим класс App, наследуем его от React.Component.
                                     // Компонент App — это класс, имеющий состояние.
   constructor(props) {    // В конструктор класса передаётся объект props
       super(props)        // super(props) — вызывает родительский конструктор
       this.state = {      // this.state — это объект состояния нашего компонента.
           'users': []   // Он будет хранить массив пользователей, которые мы будем получать с back-end.

       }
   }

   render () {     // Метод render отвечает за отрисовку нашего компонента.
       return (
           <div>
               Main App
           </div>
       )
   }
}

export default App;   // Экспортируем наш компонент для использования в других модулях.
