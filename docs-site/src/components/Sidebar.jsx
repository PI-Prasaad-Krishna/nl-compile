import React from 'react';
import { syntaxSections } from '../syntaxData';

export default function Sidebar() {
  const scrollTo = (id) => {
    document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
  };

  return (
    <aside className="sidebar">
      <h1>NL Syntax</h1>
      <nav className="nav-links">
        {syntaxSections.map((section) => (
          <button 
            key={section.id} 
            className="nav-link"
            onClick={() => scrollTo(section.id)}
          >
            {section.title}
          </button>
        ))}
      </nav>
    </aside>
  );
}
