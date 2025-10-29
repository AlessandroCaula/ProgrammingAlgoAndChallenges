import { useEffect, useRef } from "react";

interface Line {
  x: number;
  y: number;
  length: number;
  angle: number;
}

const MagneticFilingsImproved = () => {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  const rafRef = useRef<number | null>(null);
  const pointerRef = useRef({ x: -9999, y: -9999 });

  const linesRef = useRef<Line[]>([]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const DPR = window.devicePixelRatio || 1;
    let width = 0;
    let height = 0;

    const lineLength = 20;
    const spacing = 50;
    const lineWidth = 2;

    // Initialize lines grid
    const initLines = () => {
      linesRef.current = [];
      const cols = Math.floor(width / spacing);
      const rows = Math.floor(height / spacing);

      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          linesRef.current.push({
            x: c * spacing + spacing / 2,
            y: r * spacing + spacing / 2,
            length: lineLength,
            angle: 0,
          });
        }
      }
    };

    const resize = () => {
      width = canvas.clientWidth;
      height = canvas.clientHeight;
      canvas.width = width * DPR;
      canvas.height = height * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
      initLines();
    };

    const updateLines = () => {
      linesRef.current.forEach((line) => {
        const dx = pointerRef.current.x - line.x;
        const dy = pointerRef.current.y - line.y;
        line.angle = Math.atan2(dy, dx);
      });
    };

    const draw = () => {
      ctx.clearRect(0, 0, width, height);
      linesRef.current.forEach((line) => {
        ctx.beginPath();
        ctx.moveTo(line.x - Math.cos(line.angle) * (line.length / 2),
                   line.y - Math.sin(line.angle) * (line.length / 2));
        ctx.lineTo(line.x + Math.cos(line.angle) * (line.length / 2),
                   line.y + Math.sin(line.angle) * (line.length / 2));
        ctx.strokeStyle = "#FFAB00";
        ctx.lineWidth = lineWidth;
        ctx.stroke();
      });
    };

    const loop = () => {
      updateLines();
      draw();
      rafRef.current = requestAnimationFrame(loop);
    };

    const onPointerMove = (e: PointerEvent) => {
      const rect = canvas.getBoundingClientRect();
      pointerRef.current.x = e.clientX - rect.left;
      pointerRef.current.y = e.clientY - rect.top;
    };

    const onPointerLeave = () => {
      pointerRef.current.x = -9999;
      pointerRef.current.y = -9999;
    };

    window.addEventListener("resize", resize);
    canvas.addEventListener("pointermove", onPointerMove);
    canvas.addEventListener("pointerleave", onPointerLeave);

    resize();
    loop();

    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
      window.removeEventListener("resize", resize);
      canvas.removeEventListener("pointermove", onPointerMove);
      canvas.removeEventListener("pointerleave", onPointerLeave);
    };
  }, []);

  return (
    <canvas
      ref={canvasRef}
      className="w-full h-full block"
    />
  );
};

export default MagneticFilingsImproved;
