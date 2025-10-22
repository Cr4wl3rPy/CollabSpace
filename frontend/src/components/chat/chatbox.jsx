import { useState, useEffect } from "react";
import socket from "../../services/socket";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);
  const [msg, setMsg] = useState("");

  useEffect(() => {
    socket.on("message", (data) => setMessages((prev) => [...prev, data]));
    return () => socket.off("message");
  }, []);

  const sendMessage = () => {
    if (msg.trim()) {
      socket.emit("message", msg);
      setMsg("");
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow flex flex-col gap-3 w-full max-w-md">
      <div className="flex-1 overflow-y-auto h-64 border p-2 rounded">
        {messages.map((m, i) => (
          <div key={i} className="p-1 border-b text-sm">
            {m}
          </div>
        ))}
      </div>
      <div className="flex gap-2">
        <input
          value={msg}
          onChange={(e) => setMsg(e.target.value)}
          className="flex-1 border px-2 py-1 rounded"
          placeholder="Escribe un mensaje..."
        />
        <button
          onClick={sendMessage}
          className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
        >
          Enviar
        </button>
      </div>
    </div>
  );
}
