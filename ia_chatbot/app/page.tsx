import Image from "next/image";
import Link from "next/link";
import generarSesionUnica from "./components/generadorsesion";

import Dialogo from "./components/dialogo";
export default function Home() {
    const sesion = generarSesionUnica();
  return (
    <div className="contenedor-principal">

      <h1 >¿En qué puedo ayudarle?</h1>
      <Dialogo
      sesion={sesion}/>

    </div>

  );
}
