import React from 'react';
import Sidebar from '../components/Sidebar';
import DocSection from '../components/DocSection';
import { syntaxSections } from '../syntaxData';

export default function Docs() {
  return (
    <div className="app-container">
      <Sidebar />
      <main className="main-content">
        <div className="hero">
          <h1>NL Documentation</h1>
          <p>A dynamically typed, AST-based interpreted programming language built entirely in Python.</p>
        </div>

        <div className="sections-container">
          {syntaxSections.map(section => (
            <DocSection key={section.id} section={section} />
          ))}
        </div>
      </main>
    </div>
  );
}
