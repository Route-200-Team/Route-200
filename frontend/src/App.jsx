import { useEffect, useState } from 'react'

function App() {
  const [message, setMessage] = useState("Connecting to Backend...")
  
  useEffect(() => {
  const getTrips = async () => {
    try {
      // Use backticks ` (next to the 1 key), NOT single quotes '
      const response = await fetch(`${import.meta.env.VITE_API_URL}/api/trips/`);
      const data = await response.json();
      console.log(data);
      // setTrips(data);
    } catch (error) {
      console.error("Connection Failed:", error);
    }
  };
  getTrips();
}, []);

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