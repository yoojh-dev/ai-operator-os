export function GoalList({ goals }) {
  return (
    <div>
      <h2>Goals</h2>

      {goals.map((g) => (
        <div key={g.goal_id}>
          <strong>{g.description}</strong>
          <div>Status: {g.status}</div>
          <div>Progress: {g.progress}%</div>
        </div>
      ))}
    </div>
  );
}