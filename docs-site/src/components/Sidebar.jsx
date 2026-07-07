import React, { useState } from 'react';
import { syntaxSections } from '../syntaxData';

export default function Sidebar() {
  const [isOpen, setIsOpen] = useState(false);

  const handleScroll = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setIsOpen(false);
    }
  };

  return (
    <>
      <button className="mobile-menu-btn" onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? '✕ CLOSE' : '☰ MENU'}
      </button>
      <aside className={`sidebar ${isOpen ? 'open' : ''}`}>
        <h1>NL Syntax</h1>
        <nav className="nav-links">
          {syntaxSections.map((section) => (
            <button
              key={section.id}
              className="nav-link"
              onClick={() => handleScroll(section.id)}
            >
              {section.id}. {section.title}
            </button>
          ))}
        </nav>
      </aside>
      {isOpen && <div className="mobile-overlay" onClick={() => setIsOpen(false)}></div>}
    </>
  );
}
