import React, { useState } from 'react';

export default function Chatbot() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { role: 'user', text: input };
    setMessages(prev => [...prev, userMessage]);
    const currentInput = input.toLowerCase();
    setInput('');

    // AI Response Logic (Smart Simulation for Video)
    setTimeout(() => {
      let aiText = "روبوٹکس کے بارے میں آپ کا سوال موصول ہوا۔ میں اس پر تحقیق کر رہا ہوں۔";
      
      if (currentInput.includes("walk") || currentInput.includes("chalna")) {
        aiText = "Humanoid robots learn to walk using 'Reinforcement Learning' and sensors like Gyroscopes to maintain balance, just like humans!";
      } else if (currentInput.includes("physical ai")) {
        aiText = "Physical AI is the branch of robotics where AI interacts with the real world through sensors and motors, not just data on a screen.";
      } else if (currentInput.includes("humanoid")) {
        aiText = "A Humanoid robot is designed to resemble the human body's shape, allowing it to interact with human tools and environments.";
      } else if (currentInput.includes("hi") || currentInput.includes("hello")) {
        aiText = "Hello! I am your Robotics Assistant. Ask me anything about Module 1.";
      }

      const aiMessage = { role: 'ai', text: aiText };
      setMessages(prev => [...prev, aiMessage]);
    }, 1000);
  };

  return (
    <div style={{ border: '2px solid #3578e5', padding: '15px', borderRadius: '10px', backgroundColor: '#f9f9f9', maxWidth: '500px', margin: '20px 0' }}>
      <h3 style={{ marginTop: 0 }}>🤖 Robotics AI Assistant</h3>
      <div style={{ height: '250px', overflowY: 'auto', border: '1px solid #ddd', padding: '10px', marginBottom: '10px', backgroundColor: 'white' }}>
        {messages.length === 0 && <p style={{color: '#888'}}>Ask me about walking, Physical AI, or Humanoids!</p>}
        {messages.map((m, i) => (
          <div key={i} style={{ textAlign: m.role === 'user' ? 'right' : 'left', margin: '10px 0' }}>
            <span style={{ padding: '8px 12px', borderRadius: '15px', backgroundColor: m.role === 'user' ? '#3578e5' : '#e4e6eb', color: m.role === 'user' ? 'white' : 'black', display: 'inline-block' }}>
              {m.text}
            </span>
          </div>
        ))}
      </div>
      <div style={{ display: 'flex', gap: '5px' }}>
        <input value={input} onChange={(e) => setInput(e.target.value)} onKeyPress={(e) => e.key === 'Enter' && handleSend()} placeholder="Type here..." style={{ flexGrow: 1, padding: '10px', borderRadius: '5px', border: '1px solid #ccc' }} />
        <button onClick={handleSend} style={{ padding: '10px 20px', borderRadius: '5px', border: 'none', backgroundColor: '#3578e5', color: 'white', cursor: 'pointer' }}>Send</button>
      </div>
    </div>
  );
}
