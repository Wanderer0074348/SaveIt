import React, { useState } from "react";
import Dashboard from "./components/Dashboard";

function App() {
  const [link, setLink] = useState("");
  const [links, setLinks] = useState([]);

  const handleAdd = (e) => {
    e.preventDefault();
    if (link.trim() === "") return;
    setLinks([link, ...links]);
    setLink("");
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center pt-12">
      <Dashboard
        link={link}
        setLink={setLink}
        links={links}
        handleAdd={handleAdd}
      />
    </div>
  );
}

export default App;
