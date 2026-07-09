import React from 'react';
import { Link, useLocation } from 'react-router-dom';

export default function Header() {
  const location = useLocation();
  const isHome = location.pathname === '/';

  return (
    <header className="top-header">
      <Link to="/" className="header-logo">NL // Docs</Link>
      <div className="header-nav">
        {!isHome ? (
          <Link to="/" className="header-link">← Home</Link>
        ) : (
          <Link to="/docs" className="header-link">Docs</Link>
        )}
        <a href="https://github.com/PI-Prasaad-Krishna/nl-compile" target="_blank" rel="noreferrer" className="header-btn">
          GitHub
        </a>
      </div>
    </header>
  );
}
