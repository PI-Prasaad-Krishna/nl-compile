import React from 'react';
import { motion } from 'framer-motion';
import CodeSnippet from './CodeSnippet';

export default function DocSection({ section }) {
  return (
    <motion.div 
      id={section.id}
      className="doc-section"
      initial={{ opacity: 0, x: -20 }}
      whileInView={{ opacity: 1, x: 0 }}
      viewport={{ once: true, margin: "-100px" }}
      transition={{ duration: 0.4, ease: "easeOut" }}
    >
      <h2>{section.title}</h2>
      <p>{section.description}</p>
      <CodeSnippet code={section.code} />
    </motion.div>
  );
}
