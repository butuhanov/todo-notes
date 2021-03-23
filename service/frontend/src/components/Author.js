import React from 'react'
import {Link} from 'react-router-dom'

const AuthorItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`author/${item.id}`}>{item.id}</Link></td>
            <td>{item.name}</td>
            <td>{item.birthday_year}</td>
        </tr>
    )
}



const AuthorList = ({items}) => { // аuthors — это массив данных об авторах, который мы передадим в компонент.

 // Используем функцию map,
 // чтобы превратить каждого автора из массива
 // в соответствующий компонент AuthorItem.
   return (
       <table>
           <th>
               ID
           </th>
           <th>
               NAME
           </th>
           <th>
               BIRTHDAY_YEAR
           </th>
           {items.map((item) => <AuthorItem item={item} />)}

       </table>
   )
}

export default AuthorList  // Экспортируем компонент для дальнейшего использования в других модулях.

