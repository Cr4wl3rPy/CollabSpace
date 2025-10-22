import { useRef, useEffect, useState } from "react";
import socket from "../../services/socket";

export default function Whiteboard() {
  const canvasRef = useRef(null);
  const [drawing, setDrawing] = useState(false);
  const [color, setColor] = useState("#000");

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    socket.on("draw", ({ x, y, color }) => {
      ctx.fillStyle = color;
      ctx.fillRect(x, y, 2, 2);
    });

    return () => socket.off("draw");
  }, []);

  const draw = (e) => {
    if (!drawing) return;
    const { offsetX, offsetY } = e.nativeEvent;
    socket.emit("draw", { x: offsetX, y: offsetY, color });
  };

  return (
    <div className="flex flex-col items-center">
      <canvas
        ref={canvasRef}
        width={600}
        height={400}
        onMouseDown={() => setDrawing(true)}
        onMouseUp={() => setDrawing(false)}
        onMouseMove={draw}
        className="border border-gray-300 rounded"
      />
    </div>
  );
}
