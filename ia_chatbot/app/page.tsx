import Image from "next/image";
import Link from "next/link";

import Dialogo from "./components/dialogo";
export default function Home() {
  return (
    <div className="contenedor-principal">
          <main className="textocentro">
      <h1 >¿En qué puedo ayudarle?</h1>
      <Dialogo/>
    </main>
    </div>

  );
}
