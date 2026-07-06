import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';

const CodeTypingTerminal = () => {
  const code = `create list servers containing "us-east-1", "eu-west-1"\nadd "ap-south-1" to servers\n\nprint "Deploying to all regions..."\nfor each region in servers do\n    print "Deployed successfully to: " plus region\nend`;
  const [displayedText, setDisplayedText] = useState("");

  useEffect(() => {
    let i = 0;
    const intervalId = setInterval(() => {
      setDisplayedText(code.slice(0, i));
      i++;
      if (i > code.length) {
        clearInterval(intervalId);
      }
    }, 45);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="terminal-window">
      <div className="terminal-header">
        <span className="dot red"></span>
        <span className="dot yellow"></span>
        <span className="dot green"></span>
      </div>
      <pre className="terminal-body">
        <code>{displayedText}<span className="cursor"></span></code>
      </pre>
    </div>
  );
};

export default function Home() {
  return (
    <div className="home-container">
      <main className="home-main">
        <section className="hero-section">
          <motion.div 
            className="hero-content"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <h1 className="huge-title">Code in Pure English.</h1>
            <p className="hero-subtitle">The first AST-based interpreted programming language designed to be read aloud. No semicolons. No brackets. Just conversation.</p>
            <div className="hero-buttons">
              <Link to="/docs" className="btn-primary">Read Documentation</Link>
              <a href="https://github.com/PI-Prasaad-Krishna/nl-compile" target="_blank" rel="noreferrer" className="btn-secondary">View Source</a>
            </div>
          </motion.div>
          <motion.div 
            className="hero-visual"
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <CodeTypingTerminal />
          </motion.div>
        </section>

        <section className="features-grid">
          <div className="feature-card">
            <h3>Conversational Syntax</h3>
            <p>Write robust multi-line blocks, condition chains, and loops using natural English phrases instead of archaic symbols.</p>
          </div>
          <div className="feature-card">
            <h3>Native OS Control</h3>
            <p>Delete files, fetch APIs, and spawn native graphical alerts straight from the interpreter without any imported modules.</p>
          </div>
          <div className="feature-card">
            <h3>Instant REPL</h3>
            <p>Start an interactive shell that persists variables across commands and evaluates expressions in real-time.</p>
          </div>
        </section>
      </main>
    </div>
  );
}
