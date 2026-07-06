import React from 'react';

const highlightCode = (code) => {
  const keywords = ['set', 'to', 'create', 'variable', 'and', 'it', 'print', 'if', 'then', 'do', 'end', 'is', 'greater', 'than', 'less', 'equal', 'contains', 'loop', 'till', 'while', 'for', 'each', 'in', 'define', 'action', 'with', 'return', 'run', 'list', 'containing', 'object', 'as', 'add', 'remove', 'item', 'from', 'property', 'of', 'length', 'uppercase', 'lowercase', 'replace', 'by', 'split', 'write', 'into', 'file', 'read', 'ask', 'try', 'but', 'fails', 'get', 'current', 'time', 'wait', 'seconds', 'execute', 'command', 'terminal', 'fetch', 'include', 'convert', 'number', 'string', 'json', 'parse', 'show', 'alert', 'prompt', 'user', 'secret', 'matches', 'pattern', 'starts', 'ends', 'template', 'background', 'folder', 'delete', 'files', 'random', 'between', 'round', 'nearest', 'integer', 'plus', 'minus', 'times', 'divided'];
  
  // Very basic regex tokenizer
  const tokens = code.split(/(".*?"|\b\d+(?:\.\d+)?\b|\b\w+\b|[^\w\s"'])/g).filter(Boolean);
  
  return tokens.map((token, index) => {
    if (token.startsWith('"') && token.endsWith('"')) {
      return <span key={index} className="token string">{token}</span>;
    }
    if (/^\d+(?:\.\d+)?$/.test(token)) {
      return <span key={index} className="token number">{token}</span>;
    }
    if (keywords.includes(token.toLowerCase())) {
      return <span key={index} className="token keyword">{token}</span>;
    }
    if (!/^\w+$/.test(token) && token.trim() !== '') {
      return <span key={index} className="token punctuation">{token}</span>;
    }
    return <span key={index}>{token}</span>;
  });
};

export default function CodeSnippet({ code }) {
  return (
    <div className="code-snippet">
      {highlightCode(code)}
    </div>
  );
}
