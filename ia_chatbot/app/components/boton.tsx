'use client';
import React from 'react'

type propsdepagina={
  location:string
  uso:string
}

const Boton =  (pageprops:propsdepagina) => {
  return (
    <div>
      <button onClick={()=>{window.location.href=pageprops.location}}>{pageprops.uso}</button>
    </div>
  )
}

export default Boton