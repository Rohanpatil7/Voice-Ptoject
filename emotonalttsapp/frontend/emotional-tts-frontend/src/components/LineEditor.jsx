export default function LineEditor({ line, index, onChange, onDelete }) {
  return (
    <div className="grid grid-cols-[1fr_160px_40px] gap-3 mb-3">
      <textarea
        className="bg-slate-900 text-white p-3 rounded border border-slate-700 focus:outline-none focus:ring-2 focus:ring-blue-600"
        rows={2}
        value={line.text}
        onChange={e => onChange(index, "text", e.target.value)}
        placeholder="Enter dialogue..."
      />

      <select
        className="bg-slate-800 text-white rounded px-2 focus:outline-none focus:ring-2 focus:ring-blue-600"
        value={line.emotion}
        onChange={e => onChange(index, "emotion", e.target.value)}
      >
        <option value="auto">Auto (AI)</option>
        <option value="cheerful">Cheerful</option>
        <option value="calm">Calm</option>
        <option value="sad">Sad</option>
        <option value="angry">Angry</option>
        <option value="confident">Confident</option>
      </select>

      <button
        onClick={() => onDelete(index)}
        className="bg-red-600 hover:bg-red-700 text-white rounded"
      >
        ✕
      </button>
    </div>
  );
}
