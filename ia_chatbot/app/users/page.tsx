import Boton from '../components/boton'
import React from 'react'


interface User{
    userId:Number;
    title:String;
}
const UsersPage = async() => {
  const random:Number=Math.floor(Math.random()*20)
  const res= await fetch('https://jsonplaceholder.typicode.com/todos/'+random)

  const usuario:User= await res.json()

  return (
  <div>
     <p>{usuario.title}</p> 
     <Boton location={"/"} uso={"inicio"}/>

  </div>
)
}

export default UsersPage