import React from 'react'; // Импортируем React из библиотеки react
import logo from './logo.svg'; //  svg-файл
import './App.css'; // и файл со стилями.
import AuthorList from './components/Author.js' // импортируем компонент AuthorList.


class App extends React.Component {  // Создадим класс App, наследуем его от React.Component.
                                     // Компонент App — это класс, имеющий состояние.
   constructor(props) {    // В конструктор класса передаётся объект props
       super(props)        // super(props) — вызывает родительский конструктор
       this.state = {      // this.state — это объект состояния нашего компонента.
           'authors': []   // Он будет хранить массив авторов, которые мы будем получать с back-end.

       }
   }

   componentDidMount() {  // метод componentDidMount будет вызываться при монтировании компонента на страницу.
                          // В нём создан массив из объектов авторов для проверки работы приложения.
                          // Далее эти данные мы будем получать с back-end.

     const authors = [
           {
               'first_name': 'Фёдор',
               'last_name': 'Достоевский',
               'birthday_year': 1821
           },
           {
               'first_name': 'Александр',
               'last_name': 'Грин',
               'birthday_year': 1880
           },
       ]
       this.setState(  // с помощью метода this.setState меняем состояние компонента App и передаём данные об авторах
           {
               'authors': authors
           }
       )
   }


render () {
           // Отрисовываем компонент App,
           // который включает в себя компонент AuthorList,
           // и передаём в AuthorList данные
           // об авторах {this.state.authors}.
       return (
           <div>
               <AuthorList authors={this.state.authors} />
           </div>
       )
   }

}

export default App;   // Экспортируем наш компонент для использования в других модулях.