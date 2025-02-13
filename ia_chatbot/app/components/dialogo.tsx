"use client";
import React from "react";
import { useState } from "react";
import respuestachatbot from "./respuestachatbot"
const dialogo = () => {
  const [inputValue, setInputValue] = useState("");
  const [displayValue, setDisplayValue] = useState<string[]>([]);
  async function handlesubmit(e: any) {
    e.preventDefault();
    if(inputValue!=""){
      setDisplayValue(prevDisplay=>[inputValue,...prevDisplay]);
      const respuesta = await respuestachatbot(inputValue)
      setDisplayValue(prevDisplay=>[respuesta,...prevDisplay ]);
      console.log(respuesta)
      setInputValue("")

    }
 
  }

  return (
    <div>
      <br />
      <div className="message-container">

        {displayValue.map((val: string, index: number) => {
          if(index%2==0){
            return <p className="text-left-box" key={index}>{val}</p>
          }else{
            return <p className="text-right-box" key={index}>{val}</p>
          }
        }) }

      </div>

      <form onSubmit={handlesubmit} 
      autoComplete="off"
      className="contenedor-inputs">
        <input  
          className="inputbonito"
          type="text"
          id="contenido"
          name="contenido"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button type="submit" className="imagenbutton" ></button>
      </form>
    </div>
  );
};

export default dialogo;
