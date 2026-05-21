export function ExecutionTimeline({ traces }) {
  return (
    <div>
      <h2>Execution Timeline</h2>

      {traces.map((t, i) => (
        <div key={i}>
          <div>Step: {t.step}</div>
          <pre>{JSON.stringify(t, null, 2)}</pre>
        </div>
      ))}
    </div>
  );
}