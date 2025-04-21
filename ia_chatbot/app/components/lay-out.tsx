'use client';

import { useState } from "react";
import HeaderButton from "./header";
import Barralateral from "./barralateral";

export default function ClientLayout({ children }: { children: React.ReactNode }) {
  const [isSidebarOpen, setSidebarOpen] = useState(false);

  const openSidebar = () => {
    
    if (isSidebarOpen==false) {
      setSidebarOpen(true);
    }else{
        setSidebarOpen(false);
    }
  }
  const closeSidebar = () => setSidebarOpen(false);

  return (
    <>
      <HeaderButton onClick={openSidebar} />
      <Barralateral isOpen={isSidebarOpen} onClose={closeSidebar} />
      {children}
    </>
  );
}

