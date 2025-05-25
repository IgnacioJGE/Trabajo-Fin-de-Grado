'use client';
import React from 'react'
import { cn } from '../lib/utils';


export default function HeaderButton({ onClick }: { onClick: () => void}){
  return (
    <button
    onClick={onClick}    
    className={cn(
        'fixed top-3 right-3 z-50 p-3 rounded-full bg-white text-black shadow-lg hover:bg-gray-300 transition'
      )}>
        <svg xmlns="http://www.w3.org/2000/svg" width={24} height={24} viewBox="0 0 24 24"><path fill="currentColor" d="M4 18q-.425 0-.712-.288T3 17t.288-.712T4 16h16q.425 0 .713.288T21 17t-.288.713T20 18zm0-5q-.425 0-.712-.288T3 12t.288-.712T4 11h16q.425 0 .713.288T21 12t-.288.713T20 13zm0-5q-.425 0-.712-.288T3 7t.288-.712T4 6h16q.425 0 .713.288T21 7t-.288.713T20 8z"></path></svg>
      </button>
  )
}

