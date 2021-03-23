import React from 'react'


const TodoItem = ({todo}) => {
   return (
   <tbody>
       <tr>
           <td>
               {todo.name}
           </td>
           <td>
               {todo.project}
           </td>
       </tr>
       </tbody>
   )
}

const TodoList = ({todos}) => {
   return (
       <table>
       <thead>
       <tr>
           <th>
               Название задачи
           </th>
           <th>
               Проект
           </th>
           </tr>
           </thead>
           {todos.map((todo) => <TodoItem todo={todo} />)}
       </table>
   )
}

export default TodoList