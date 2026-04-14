import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState("Connecting to Backend...")

  useEffect(() => {
    const response = await fetch(`${import.meta.env.VITE_API_URL}/api/test/`);
      .then(response => {
        if (!response.ok) throw new Error("Network response was not ok");
        return response.json();
      })
      .then(data => setMessage(data.message))
      .catch(err => {
        console.error(err);
        setMessage("Connection Failed. Check if Django is running!");
      })
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '50px', fontFamily: 'sans-serif' }}>
      <h1>Route 200 Travel Tracker</h1>
      <div style={{ padding: '20px', border: '1px solid #ccc', borderRadius: '8px', display: 'inline-block' }}>
        <p>Backend Status: <strong>{message}</strong></p>
      </div>
    </div>
  )
}

export default App