import React from "react";
import Whiteboard from "../components/Whiteboard/Whiteboard";
import ChatBox from "../components/Chat/ChatBox";
import Toolbar from "../components/Toolbar/Toolbar";
import UserList from "../components/UserList/UserList";

const Room = ({ user }) => {
  return (
    <div className="flex flex-col h-screen bg-background text-gray-800">
      {/* HEADER */}
      <header className="flex justify-between items-center px-6 py-3 bg-primary text-white shadow-md">
        <h1 className="text-2xl font-semibold tracking-wide">CollabSpace</h1>
        <div className="flex items-center gap-3">
          <span className="text-sm">👤 {user?.name || "Invitado"}</span>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="flex flex-1 overflow-hidden">
        {/* Whiteboard */}
        <section className="flex-1 bg-white border-r border-gray-200 relative">
          <Whiteboard />
        </section>

        {/* Chat + Users */}
        <aside className="w-80 bg-secondary text-white flex flex-col">
          <div className="flex-1 border-b border-gray-600 overflow-y-auto">
            <ChatBox />
          </div>
          <div className="h-48 overflow-y-auto bg-gray-800">
            <UserList />
          </div>
        </aside>
      </main>

      {/* TOOLBAR */}
      <footer className="p-3 bg-gray-100 border-t shadow-inner">
        <Toolbar />
      </footer>
    </div>
  );
};

export default Room;
