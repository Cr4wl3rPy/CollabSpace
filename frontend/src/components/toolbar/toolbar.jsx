export default function Toolbar({ color, setColor }) {
  return (
    <div className="flex items-center gap-3 bg-gray-100 p-3 rounded-lg shadow">
      <label className="text-sm font-semibold">Color:</label>
      <input type="color" value={color} onChange={(e) => setColor(e.target.value)} />
    </div>
  );
}
