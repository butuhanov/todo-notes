import React from 'react'


const ProjectItem = ({project}) => {
   return (
   <tbody>
           <tr>
               <td>
                   {project.name}
               </td>
               <td>
                   {project.repo_link}
               </td>
           </tr>
           </tbody>
   )
}

const ProjectList = ({projects}) => {
   return (
       <table>
       <thead>
       <tr>
           <th>
               Название проекта
           </th>
           <th>
               Ссылка на репозиторий
           </th>
           </tr>
           </thead>
           {projects.map((project) => <ProjectItem project={project} />)}
       </table>
   )
}

export default ProjectList