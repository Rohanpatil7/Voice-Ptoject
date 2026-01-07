import { useState } from "react";
import ScriptEditor from "./components/ScriptEditor";
import { generateTTS } from "./api";

export default function App() {
  const [lines, setLines] = useState([
    { text: "Yo guys! Kya haal hai?", emotion: "auto" }
  ]);
  const [gender, setGender] = useState("female");
  const [loading, setLoading] = useState(false);

  const submit = async () => {
    setLoading(true);
    await generateTTS({ gender, lines });
    setLoading(false);
    alert("🎉 Audio & subtitles generated!");
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      <div className="max-w-5xl mx-auto p-6">
        <h1 className="text-3xl font-bold mb-6">
          🎙 Emotional Indian TTS
        </h1>

        <div className="flex items-center gap-4 mb-6">
          <label className="text-slate-300">Voice</label>
          <select
            className="bg-slate-800 rounded px-3 py-2 focus:ring-2 focus:ring-blue-600"
            value={gender}
            onChange={e => setGender(e.target.value)}
          >
            <option value="female">Female</option>
            <option value="male">Male</option>
          </select>
        </div>

        <ScriptEditor lines={lines} setLines={setLines} />

        <button
          onClick={submit}
          disabled={loading}
          className="mt-8 w-full py-3 bg-blue-600 hover:bg-blue-700 rounded text-lg font-semibold disabled:opacity-50"
        >
          {loading ? "Generating..." : "🎧 Generate Voice"}
        </button>
      </div>
    </div>
  );
}
