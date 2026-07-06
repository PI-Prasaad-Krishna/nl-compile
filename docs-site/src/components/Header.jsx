import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header className="top-header">
      <Link to="/" className="header-logo">NL // Docs</Link>
      <div className="header-nav">
        <Link to="/docs" className="header-link">Documentation</Link>
        <a href="https://github.com/PI-Prasaad-Krishna/nl-compile" target="_blank" rel="noreferrer" className="header-btn">
          View on GitHub
        </a>
      </div>
    </header>
  );
}
