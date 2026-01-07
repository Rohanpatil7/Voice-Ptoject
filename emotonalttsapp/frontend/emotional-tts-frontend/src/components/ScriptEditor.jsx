import LineEditor from "./LineEditor";

export default function ScriptEditor({ lines, setLines }) {
  const updateLine = (i, key, value) => {
    const copy = [...lines];
    copy[i][key] = value;
    setLines(copy);
  };

  const removeLine = i => {
    setLines(lines.filter((_, idx) => idx !== i));
  };

  const addLine = () => {
    setLines([...lines, { text: "", emotion: "auto" }]);
  };

  return (
    <div>
      {lines.map((line, i) => (
        <LineEditor
          key={i}
          index={i}
          line={line}
          onChange={updateLine}
          onDelete={removeLine}
        />
      ))}

      <button
        onClick={addLine}
        className="mt-3 px-4 py-2 bg-green-600 hover:bg-green-700 rounded text-white"
      >
        ➕ Add Line
      </button>
    </div>
  );
}
