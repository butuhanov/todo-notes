import React from 'react'


const AuthorItem = ({author}) => {  // Это простой компонент без состояния.
                                    // Такие компоненты удобнее создавать как функции.
                                    // В нашем случае применяется стрелочная функция,
                                    // но можно использовать и обычную function.
                                    // В параметры каждого компонента на react приходит объект props.
                                    // Он содержит в себе все переданные в компонент данные.
                                    // Параметр {author} означает,
                                    // что из всех props мы ожидаем получить author — объект автора,
                                    // и далее работать только с ним.
   return (             // Функция возвращает разметку компонента.

       <tr>
           <td>
               {author.first_name}  // {author.first_name}. В неё мы помещаем данные из объекта author.
           </td>
           <td>
               {author.last_name}
           </td>
           <td>
               {author.birthday_year}
           </td>
       </tr>
   )
}


const AuthorList = ({authors}) => { // аuthors — это массив данных об авторах, который мы передадим в компонент.

   return (
       <table>
           <th>
               First name
           </th>
           <th>
               Last Name
           </th>
           <th>
               Birthday year
           </th>
           {authors.map((author) => <AuthorItem author={author} />)} // Используем функцию map,
                                                                     // чтобы превратить каждого автора из массива
                                                                     // в соответствующий компонент AuthorItem.
       </table>
   )
}

export default AuthorList  // Экспортируем компонент для дальнейшего использования в других модулях.

