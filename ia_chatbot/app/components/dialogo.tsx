"use client";

import React from "react";
import { useState } from "react";

const dialogo = () => {
  const [inputValue, setInputValue] = useState("");
  const [displayValue, setDisplayValue] = useState<string[]>([]);
  function handlesubmit(e: any) {
    e.preventDefault();
    if(inputValue!=""){
      setDisplayValue([inputValue,...displayValue]);
      setInputValue("")
    }
  }

  return (
    <div>
      <br />
      <div className="message-container">
        
        {displayValue.map((val: string, index: number) => (
          <p className="text-right-box" key={index}>{val}</p>
        )) }
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
