export type SideNavItem = {
    title:string;
    path: string;
    icon?:JSX.Element;
    submenu?: boolean;
    submenuItems?: SideNavItem[];
}


export type Manual={
    url:string;
    descripcion:string;
}