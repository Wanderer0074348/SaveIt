import React from "react";
import LinkInput from "./LinkInput";
import LinkList from "./LinkList";

function Dashboard({ link, setLink, links, handleAdd }) {
  return (
    <div className="bg-white rounded-lg shadow-lg p-8 w-full max-w-md">
      <h1 className="text-2xl font-bold mb-6 text-center">SaveIt Dashboard</h1>
      <LinkInput link={link} setLink={setLink} onAdd={handleAdd} />
      <LinkList links={links} />
    </div>
  );
}

export default Dashboard;
