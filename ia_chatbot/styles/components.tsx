import {SideNavItem} from "./types"


export const SIDENAV_ITEMS: SideNavItem[] = [
    {
        title: "Chatbot",
        path: "/",
        icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 48 48" className="w-6 h-6"><g fill="none" stroke="currentColor" strokeWidth="4"><rect width="30" height="26" x="9" y="17" strokeLinecap="round" strokeLinejoin="round" rx="2"/><path strokeLinecap="round" strokeLinejoin="round" d="m33 9l-5 8M15 9l5 8"/><circle cx="34" cy="7" r="2"/><circle cx="14" cy="7" r="2"/><rect width="16" height="8" x="16" y="24" rx="4"/><path strokeLinecap="round" strokeLinejoin="round" d="M9 24H4v10h5m30-10h5v10h-5"/></g></svg>
    },
    {
        title: "Ayuda",
        path: "/help",
        icon: <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"    className="w-6 h-6"><path fill="currentColor" d="M11.95 18q.525 0 .888-.363t.362-.887t-.362-.888t-.888-.362t-.887.363t-.363.887t.363.888t.887.362m-.9-3.85h1.85q0-.825.188-1.3t1.062-1.3q.65-.65 1.025-1.238T15.55 8.9q0-1.4-1.025-2.15T12.1 6q-1.425 0-2.312.75T8.55 8.55l1.65.65q.125-.45.563-.975T12.1 7.7q.8 0 1.2.438t.4.962q0 .5-.3.938t-.75.812q-1.1.975-1.35 1.475t-.25 1.825M12 22q-2.075 0-3.9-.787t-3.175-2.138T2.788 15.9T2 12t.788-3.9t2.137-3.175T8.1 2.788T12 2t3.9.788t3.175 2.137T21.213 8.1T22 12t-.788 3.9t-2.137 3.175t-3.175 2.138T12 22m0-2q3.35 0 5.675-2.325T20 12t-2.325-5.675T12 4T6.325 6.325T4 12t2.325 5.675T12 20m0-8"/></svg>

    },
    {
        title: "Manuales",
        path: "/manuales",
        icon:<svg xmlns="http://www.w3.org/2000/svg" width={22} height={22} viewBox="0 0 14 14"><g fill="none" stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth={1}><path d="M5.5 4.054a1.5 1.5 0 1 1 1.5 1.5v.5m0 2.062a.25.25 0 0 1 0-.5m0 .5a.25.25 0 0 0 0-.5"></path><path d="M12.5 13.5H3a1.5 1.5 0 1 1 0-3h8.5a1 1 0 0 0 1-1v-8a1 1 0 0 0-1-1H3a1.5 1.5 0 0 0-1.5 1.46v10m10-1.46v3"></path></g></svg>
    }

]