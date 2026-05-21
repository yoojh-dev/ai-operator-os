"use client";

import { useEffect, useState } from "react";
import { getTrace } from "@/lib/api";

export default function TraceViewer() {

  const [trace, setTrace] = useState<any>(null);

  useEffect(() => {

    getTrace("latest").then(setTrace);

  }, []);

  return (
    <div>
      <h3>Trace Viewer</h3>

      <pre>
        {JSON.stringify(trace, null, 2)}
      </pre>
    </div>
  );
}