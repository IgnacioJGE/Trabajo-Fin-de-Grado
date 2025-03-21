/* eslint-disable @typescript-eslint/no-explicit-any */
"use client";

import React from "react";
import { useState } from "react";
import respuestachatbot from "./respuestachatbot";

type Propssesion = {
  sesion: string;
};

function Dialogo({ sesion }: Propssesion) {
  const regexemail = RegExp("/recursos/[A-Za-z0-9]+.png");
  const [inputValue, setInputValue] = useState("");
  const [displayValue, setDisplayValue] = useState<
    { text: string; usuario: string }[]
  >([]);
  async function handlesubmit(e:any) {
    e.preventDefault();
    if (inputValue != "") {
      setDisplayValue((prevDisplay) => [
        ...prevDisplay,
        { text: inputValue, usuario: "persona" },
      ]);
      console.log(sesion);
      const respuesta = await respuestachatbot(inputValue, sesion);

      setTimeout(() => {
        if (regexemail.test(respuesta)) {
          setDisplayValue((prevDisplay) => [
            ...prevDisplay,
            { text: respuesta, usuario: "bot_imagen" },
          ]);
        } else {
          setDisplayValue((prevDisplay) => [
            ...prevDisplay,
            { text: respuesta, usuario: "bot" },
          ]);
        }
      }, 500);
      setInputValue("");
    }
  }
  const handleKeyPress = (e:any) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handlesubmit(e);
      setInputValue("");
    }
  };

  return (
    <div>
      <br />
      <div className="message-container">
        {[...displayValue].reverse().map((val, index) => {
          if (val.usuario == "persona") {
            return (
              <p className="text-right-box" key={index}>
                {val.text}
              </p>
            );
          } else if (val.usuario == "bot") {
            return (
              <p
                className="text-left-box"
                key={index}
                dangerouslySetInnerHTML={{ __html: val.text }}
              ></p>
            );
          } else {
            return (
              <img className="imagen-left-box" key={index} src={val.text}></img>
            );
          }
        })}
      </div>

      <form
        onSubmit={handlesubmit}
        autoComplete="off"
        className="contenedor-inputs"
      >
        <textarea
          className="inputbonito"
          id="contenido"
          name="contenido"
          placeholder="Enviar un mensaje"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyDown={handleKeyPress}
        />
        <button type="submit" className="imagenbutton"></button>
      </form>
    </div>
  );
}

export default Dialogo;
