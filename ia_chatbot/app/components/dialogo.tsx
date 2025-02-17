"use client";
import React from "react";
import { useState, useEffect } from "react";
import respuestachatbot from "./respuestachatbot"
const dialogo = () => {
  const [inputValue, setInputValue] = useState("");
  const [displayValue, setDisplayValue] = useState<{text: string, usuario:string}[]>([]);
  async function handlesubmit(e: any) {
    e.preventDefault();
    if(inputValue!=""){
      setDisplayValue(prevDisplay=>[...prevDisplay,{text:inputValue, usuario:"persona"}]);
      const respuesta = await respuestachatbot(inputValue)
      setTimeout(() => {
        setDisplayValue((prevDisplay) => [...prevDisplay,{text:respuesta, usuario:"bot"}]);}, 500);
      console.log(respuesta)
      setInputValue("") 

    }
 
  }
  const handleKeyPress = (e:any) => {
    if (e.key === 'Enter') {
      e.preventDefault();  // Prevenir que se añada una nueva línea en el textarea
      handlesubmit(e);  // Llamar a la función de envío del formulario
      setInputValue("") 
    }
  };

  return (
    <div>
      <br />
      <div className="message-container">

        {[...displayValue].reverse().map((val, index) => {
          if(val.usuario== "persona"){
            return <p className="text-right-box" key={index}>{val.text}</p>

          }else{
            return <p className="text-left-box" key={index}>{val.text}</p>

          }
        
        }) }

      </div>

      <form onSubmit={handlesubmit} 
      autoComplete="off"
      className="contenedor-inputs">
        <textarea  
          className="inputbonito"
          id="contenido"
          name="contenido"
          placeholder="Enviar un mensaje"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyPress} 
        />
        <button type="submit" className="imagenbutton" ></button>
      </form>
    </div>
  );
};

export default dialogo;
