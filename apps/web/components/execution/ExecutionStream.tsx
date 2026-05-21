"use client";

import { useEffect, useState } from "react";

export default function ExecutionStream() {

  const [events, setEvents] = useState<any[]>([]);

  useEffect(() => {

    const ws = new WebSocket("ws://localhost:8000/ws/execution");

    ws.onmessage = (e) => {

      setEvents(prev => [...prev, JSON.parse(e.data)]);
    };

    return () => ws.close();

  }, []);

  return (
    <div>
      <h3>Execution Stream</h3>

      <pre>
        {JSON.stringify(events, null, 2)}
      </pre>
    </div>
  );
}