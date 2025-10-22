import React, { useState } from "react";
import Whiteboard from "./components/Whiteboard/Whiteboard.jsx";
import ChatBox from "./components/Chat/Chatbox.jsx";
import Toolbar from "./components/Toolbar/Toolbar.jsx";
import UserList from "./components/UserList/UserList.jsx";
import { FaRocket } from "react-icons/fa";

const Room = ({ user, roomId: initialRoomId }) => {
  const [roomId, setRoomId] = useState(initialRoomId || "Sin sala");
  const [showModal, setShowModal] = useState(false);
  const [newRoom, setNewRoom] = useState("");

  const handleEnterRoom = () => {
    if (newRoom.trim()) {
      setRoomId(newRoom.trim());
      setShowModal(false);
      setNewRoom("");
    }
  };

  return (
    <div className="flex flex-col h-screen bg-background text-gray-800">
      <header className="flex justify-between items-center px-6 py-3 bg-primary text-white shadow-md">
        <h1 className="text-2xl font-semibold tracking-wide flex items-center gap-2 relative">
          <span className="relative flex items-center">
            <FaRocket className="text-yellow-400 transform transition-transform duration-300 hover:animate-rocketFly" />
            <span className="absolute -bottom-2 left-1/2 w-1 h-3 bg-yellow-300 rounded-full animate-rocketTrail"></span>
          </span>
          CollabSpace
        </h1>
        <div className="flex items-center gap-4">
          <span className="text-sm">👤 {user?.name || "Invitado"}</span>
          <span className="text-sm">🏷 Sala: {roomId}</span>
          <button
            onClick={() => setShowModal(true)}
            className="bg-yellow-400 text-primary px-3 py-1 rounded hover:bg-yellow-300 transition"
          >
            Entrar a otra sala
          </button>
        </div>
      </header>

      {showModal && (
        <div className="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded shadow-lg w-80">
            <h2 className="text-lg font-semibold mb-4">Ingrese nueva sala</h2>
            <input
              type="text"
              value={newRoom}
              onChange={(e) => setNewRoom(e.target.value)}
              className="w-full border border-gray-300 rounded px-2 py-1 mb-4"
              placeholder="Nombre de la sala"
            />
            <div className="flex justify-end gap-2">
              <button
                onClick={() => setShowModal(false)}
                className="px-3 py-1 rounded bg-gray-300 hover:bg-gray-400"
              >
                Cancelar
              </button>
              <button
                onClick={handleEnterRoom}
                className="px-3 py-1 rounded bg-yellow-400 text-primary hover:bg-yellow-300"
              >
                Entrar
              </button>
            </div>
          </div>
        </div>
      )}

      <main className="flex flex-1 overflow-hidden">
        <section className="flex-1 bg-white border-r border-gray-200 relative">
          <Whiteboard />
        </section>
        <aside className="w-80 bg-secondary text-white flex flex-col">
          <div className="flex-1 border-b border-gray-600 overflow-y-auto">
            <ChatBox />
          </div>
          <div className="h-48 overflow-y-auto bg-gray-800">
            <UserList />
          </div>
        </aside>
      </main>

      <footer className="p-3 bg-gray-100 border-t shadow-inner">
        <Toolbar />
      </footer>
    </div>
  );
};

export default Room;
