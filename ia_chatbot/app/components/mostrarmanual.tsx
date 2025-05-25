"use client";
import React, { useEffect, useState } from 'react';
import { Manual } from '@/styles/types';

export const Mostrarmanual = () => {
    const [arraymanual, setArraymanual] = useState<Manual[]>([]);
  useEffect(() => {
    async function fetchManuales() {
      const res = await fetch('/api/manuales');
      const data = await res.json();
      setArraymanual(data);
    }

    fetchManuales();
  }, []);
  return (
    <div>{arraymanual.map((manual,key)=>{
      return(
        <div className='manuales-bonitos' key={key}>
          <h1 className='titulo-manual'>{manual.descripcion}</h1>
          <a className='link-manual' href={manual.url}>{manual.url}</a>
        </div>
      )
    })}</div>
  )
}
