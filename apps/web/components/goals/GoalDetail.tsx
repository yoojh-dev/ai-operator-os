export function GoalDetail({ goal }) {
  return (
    <div>
      <h2>Goal Detail</h2>

      <pre>{JSON.stringify(goal, null, 2)}</pre>
    </div>
  );
}