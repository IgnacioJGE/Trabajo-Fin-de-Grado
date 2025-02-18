import Image from "next/image";
import Link from "next/link";

import Dialogo from "./components/dialogo";
export default function Home() {
  return (
    <div className="contenedor-principal">

      <h1 >¿En qué puedo ayudarle?</h1>
      <Dialogo/>

    </div>

  );
}
