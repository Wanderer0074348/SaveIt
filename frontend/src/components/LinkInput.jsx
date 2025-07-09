import React from "react";

function LinkInput({ link, setLink, onAdd }) {
  return (
    <form onSubmit={onAdd} className="flex gap-2 mb-6">
      <input
        type="url"
        placeholder="Paste your link here..."
        value={link}
        onChange={(e) => setLink(e.target.value)}
        className="flex-1 border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
        required
      />
      <button
        type="submit"
        className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition"
      >
        Add
      </button>
    </form>
  );
}

export default LinkInput;
