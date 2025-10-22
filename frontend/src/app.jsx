import React from "react";
import "./index.css";

function App() {
  return (
    <div className="min-h-screen bg-background flex flex-col items-center justify-center text-center text-gray-800">
      <header className="mb-10">
        <h1 className="text-5xl font-extrabold text-primary drop-shadow-lg">
          CollabSpace
        </h1>
        <p className="mt-3 text-lg text-secondary">
          Colabora en tiempo real con tu equipo
        </p>
      </header>

      <main className="flex flex-col gap-4 w-full max-w-md bg-white shadow-xl rounded-2xl p-6">
        <input
          type="text"
          placeholder="Ingresa tu nombre"
          className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
        />
        <input
          type="text"
          placeholder="ID de sala o crea una nueva"
          className="w-full border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-primary"
        />
        <button className="bg-primary text-white font-semibold py-2 px-4 rounded-lg hover:bg-blue-700 transition">
          Entrar a la sala
        </button>
      </main>

      <footer className="mt-10 text-sm text-gray-500">
        © {new Date().getFullYear()} CollabSpace. Creado con 💻 y ☕
      </footer>
    </div>
  );
}

export default App;

