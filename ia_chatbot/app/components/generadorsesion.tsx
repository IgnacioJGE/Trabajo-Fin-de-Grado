

function generarSesionUnica(): string {
    return 'sesion-' + Math.random().toString(36).substring(2, 15);  // Puedes usar una librería como uuid para un id más robusto.
  }

export default generarSesionUnica;