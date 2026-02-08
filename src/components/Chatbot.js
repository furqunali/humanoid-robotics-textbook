import React, { useState } from 'react';

export default function Chatbot() {
  const [msg, setMsg] = useState('');
  const [chat, setChat] = useState([]);

  const handleSend = async () => {
    const res = await fetch('http://localhost:8000/ask?query=' + msg);
    const data = await res.json();
    setChat([...chat, { user: msg, bot: data.answer }]);
    setMsg('');
  };

  return (
    <div style={{ padding: '20px', backgroundColor: '#f9f9f9', borderRadius: '10px' }}>
      <h4>🤖 Robotics AI Assistant</h4>
      <div style={{ height: '200px', overflowY: 'scroll', marginBottom: '10px' }}>
        {chat.map((c, i) => (
          <div key={i}><b>You:</b> {c.user}<br/><b>AI:</b> {c.bot}<hr/></div>
        ))}
      </div>
      <input value={msg} onChange={(e) => setMsg(e.target.value)} style={{ width: '80%' }} />
      <button onClick={handleSend}>Send</button>
    </div>
  );
}
