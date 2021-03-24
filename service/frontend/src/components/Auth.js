import React from 'react'


class LoginForm extends React.Component {
    constructor(props) {
    // Так как в форму пользователь будет вводить данные, мы будем использовать компонент с состоянием.
    // В конструкторе мы создали состояние, в котором будут храниться login и password
      super(props)
      this.state = {login: '', password: ''}
    }
    handleChange(event)
    // Метод handleChange принимает в себя event — это событие, которое произойдёт при вводе данных в поля формы.
    // Этот метод будет менять состояние event.target.name и записывать в него event.target.value.
    // Так как event.target — это input, в который будут вводиться данные, его name будет либо login, либо password,
     // а value — соответствующее введённое значение.
    {
        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );
    }

handleSubmit(event) {
// Метод handleSubmit будет выполняться при отправке формы.
// В нём мы проверим, что правильно получили login и password,
// которые ввёл пользователь. event.preventDefault() отменит отправку формы.
// Это нужно, так как мы сами будем отправлять запрос на сервер с помощью Axios.
      this.props.get_token(this.state.login, this.state.password)
      event.preventDefault()
    }


    render() {
    // Метод render отрисовывает компонент формы.
    // Событие onSubmit формы мы связываем с методом handleSubmit,
    // а событие onChange на input-ах — с методом handleChange.
    // Таким образом, при вводе данных будут меняться login и password в state компонента,
    // а после отправки формы мы будем использовать введённые значения.
      return (
        <form onSubmit={(event)=> this.handleSubmit(event)}>
            <input type="text" name="login" placeholder="login" value={this.state.login} onChange={(event)=>this.handleChange(event)} />
            <input type="password" name="password" placeholder="password" value={this.state.password} onChange={(event)=>this.handleChange(event)} />
            <input type="submit" value="Login" />
        </form>
      );
    }
  }

  export default LoginForm