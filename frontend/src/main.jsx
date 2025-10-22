import React from "react";
import ReactDOM from "react-dom/client";
import Room from "./Room";
import "./index.css";

const testUser = { name: "Alex" };
const testRoomId = "Sala-1";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Room user={testUser} roomId={testRoomId} />
  </React.StrictMode>
);
