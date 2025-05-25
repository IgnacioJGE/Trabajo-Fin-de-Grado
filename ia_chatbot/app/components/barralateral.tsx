import { motion } from 'framer-motion';
import Link from 'next/link';
import { SIDENAV_ITEMS } from '@/styles/components';
import Image from 'next/image'

export default function Barralateral({ isOpen, onClose }: { isOpen: boolean, onClose: () => void }) {
    return (
      <>
        {isOpen && (//pone la pantalla en gris
          <div
            className="fixed inset-0 bg-black bg-opacity-10 z-40"
            onClick={onClose}
          />
        )}
        <motion.div //elemento interactivo que saca la barra lateral 
          initial={{ x: '-100%' }}
          animate={{ x: isOpen ? 0 : '-100%' }}
          transition={{ type: 'spring', stiffness: 200, damping: 25 }}
          className="fixed top-0 left-0 h-full w-64 bg-gray-50  z-50 p-4"
        >
            <Image src="/recursos/logo-imagen.png" alt="Logo" width={200} height={200} className="mx-auto mb-12"/>
  
          <nav className="flex flex-col space-y-5">
            {SIDENAV_ITEMS.map((item) => (
              <Link
                key={item.path}
                href={item.path}
                className="flex items-center space-x-2 custom-hover"
                onClick={onClose}
              >
                {item.icon && <span>{item.icon}</span>}
                <span>{item.title}</span>
              </Link>
            ))}
          </nav>
        </motion.div>
      </>
    );
  }
