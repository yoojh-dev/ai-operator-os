type ExecutionGraphProps = {
  data?: {
    dag?: unknown;
  };
};

export default function ExecutionGraph({
  data
}: ExecutionGraphProps) {

  return (
    <pre>
      {JSON.stringify(data?.dag || {}, null, 2)}
    </pre>
  );
}