import React from "react";

function LinkList({ links }) {
  return (
    <div>
      <h2 className="text-lg font-semibold mb-2">Your Links</h2>
      <ul className="space-y-2">
        {links.length === 0 && (
          <li className="text-gray-400 italic">No links added yet.</li>
        )}
        {links.map((l, idx) => (
          <li key={idx} className="bg-gray-50 rounded px-3 py-2 break-all">
            <a
              href={l}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 underline"
            >
              {l}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default LinkList;
