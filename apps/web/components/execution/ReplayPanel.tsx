"use client";

import { useState } from "react";
import { getReplay } from "@/lib/api";

export default function ReplayPanel() {

  const [data, setData] = useState<any>(null);

  const run = async () => {

    const res = await getReplay("latest");

    setData(res);
  };

  return (
    <div>
      <h3>Replay Panel</h3>

      <button onClick={run}>
        Replay
      </button>

      <pre>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}