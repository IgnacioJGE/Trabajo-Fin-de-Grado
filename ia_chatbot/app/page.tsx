import generarSesionUnica from "./components/generadorsesion";
import Dialogo from "./components/dialogo";


export default function Home() {
  const session = generarSesionUnica();
  return (
    <div className="contendor-global">
    <div className="contenedor-principal">

      <h1 >HelpDesk Departamento Innovación y Proyectos</h1>
      <Dialogo sesion={session}/>

    </div>
    </div>
  );
}
