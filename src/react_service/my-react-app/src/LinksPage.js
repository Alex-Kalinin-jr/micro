
import React, { useState, useEffect } from 'react';


export default function LinksPage() {
  const [links, setLinks] = useState([]);

  useEffect(() => {
    async function fetchLinks() {
      try {
        const response = await fetch('/data/links');
        if (!response.ok) throw new Error('Failed to fetch links');
        const data = await response.json();
        setLinks(data);
      } catch (error) {
        console.error('Error:', error);
      }
    }
    fetchLinks();
  }, []);

  return (
    <div>
      <div id="linksBlock">
        {links.map((link, index) => (
          <React.Fragment key={index}>
            <li>{link.explanation}</li>
            <a href={link.data}>Перейти</a>
          </React.Fragment>
        ))}
      </div>
    </div>
  );
}

