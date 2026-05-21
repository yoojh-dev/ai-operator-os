import TraceViewer from "@/components/trace/TraceViewer";
import ReplayPanel from "@/components/execution/ReplayPanel";
import MemoryInspector from "@/components/memory/MemoryInspector";
import ExecutionStream from "@/components/execution/ExecutionStream";

export default function Dashboard() {
  return (
    <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>

      <TraceViewer />

      <ExecutionStream />

      <MemoryInspector />

      <ReplayPanel />

    </div>
  );
}