import { useEffect, useRef } from "react";

interface Line {
  startX: number;
  startY: number;
  endX: number;
  endY: number;
  angle?: number;
}

interface Pointer {
  x: number;
  y: number;
  active: boolean;
}

const MagneticFilings = () => {
  // Ref to directly access the <canvas> DOM element
  const canvasRef = useRef<HTMLCanvasElement | null>(null);
  // Ref to store the animation frame ID (for requestAnimationFrame)
  // This allows us to start and later stop the animation loop safely
  const rafRef = useRef<number | null>(null);
  // Store current pointer info
  const pointerRef = useRef<Pointer>({
    x: -9999, // Offscreen initial position
    y: -9999,
    active: false,
  });
  // Collection of all the lines.
  const linesRef = useRef<Line[]>([]);

  // Teh effect runs once after the component mounts
  useEffect(() => {
    const canvas = canvasRef.current; // Get the canvas element
    if (!canvas) return;

    const ctx = canvas.getContext("2d"); // Get 2d drawing context
    if (!ctx) return;

    // Handle high DPR screens (e.g. Retina)
    const DPR = window.devicePixelRatio || 1;

    // These will track canvas size in CSS pixels
    let width = 0;
    let height = 0;

    const lineLength = 20;
    const lineWidth = 2;
    const horizontalSpaceBetweenLines = 45;
    const verticalSpaceBetweenLines = 45;

    // Function to resize the canvas whenever window size changes.
    const resize = () => {
      width = canvas.clientWidth; // Current width in CSS pixels
      height = canvas.clientHeight; // Current height in CSS pixels

      // Scale the actual canvas pixel buffer by device pixel ration
      canvas.width = Math.floor(width * DPR);
      canvas.height = Math.floor(height * DPR);

      // Reset the transform so drawing coordinates are correct
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);

      // Call the initialization lines
      initializeLines();
    };

    const initializeLines = () => {
      linesRef.current = []; // clear old lines
      // Compute the number of lines that can be fitted horizontally
      const nHorizontalLines = Math.floor(
        width / (horizontalSpaceBetweenLines + lineWidth)
      );
      // Compute the number of lines that can be fitted vertically
      const nVerticalLines = Math.floor(height / verticalSpaceBetweenLines);

      // now "initialize" each line in the canvas
      for (let r = 0; r < nVerticalLines; r++) {
        for (let c = 0; c < nHorizontalLines; c++) {
          // Compute the X and Y coordinates of the current line
          const currStartX =
            horizontalSpaceBetweenLines + c * horizontalSpaceBetweenLines;
          const currStartY =
            verticalSpaceBetweenLines + r * verticalSpaceBetweenLines;
          // Define the current line object
          const currLine: Line = {
            startX: currStartX,
            startY: currStartY,
            endX: currStartX,
            endY: currStartY + lineLength,
          };
          // Push the line to the lines
          linesRef.current.push(currLine);
        }
      }
    };

    // Handle mouse movement
    const onPointerMove = (e: PointerEvent) => {
      const rect = canvas.getBoundingClientRect(); // Get canvas position relative to viewport
      pointerRef.current.x = e.clientX - rect.left;
      pointerRef.current.y = e.clientY - rect.top;
      pointerRef.current.active = true;
    };

    // Handle mouse leaving the canvas
    const onPointerLeave = () => {
      pointerRef.current.active = false;
      pointerRef.current.x = -9999;
      pointerRef.current.y = -9999;
    };

    // Handle touch input (mobile)
    const onTouch = (e: TouchEvent) => {
      if (e.touches && e.touches[0]) {
        const t = e.touches[0];
        onPointerMove(t as unknown as PointerEvent);
      }
    };

    // Main logic. Updating the direction of the lines
    const updatePosition = () => {
      // Return if the mouse is not on the canvas
      if (!pointerRef.current.active) return;

      // Retrieve all the mouse X and Y coordinates
      const mouseX = pointerRef.current.x;
      const mouseY = pointerRef.current.y;

      // Loop through all the lines
      linesRef.current.forEach((line) => {
        // Compute the direction from the start point of the line and the mouse
        const dx = mouseX - line.startX;
        const dy = mouseY - line.startY;

        // Compute the angle in radians
        const angle = Math.atan2(dy, dx);

        // Now compute the endpoint coordinates using the line's fixed length
        line.endX = line.startX + Math.cos(angle) * lineLength;
        line.endY = line.startY + Math.sin(angle) * lineLength;
      });
    };

    // Drawing the lines
    const draw = () => {
      // Here we can clear or draw whatever we want every frame
      ctx.clearRect(0, 0, width, height);
      ctx.save();

      const lines = linesRef.current;
      lines.forEach((line) => {
        ctx.beginPath();
        ctx.moveTo(line.startX, line.startY);
        ctx.lineTo(line.endX, line.endY);
        ctx.strokeStyle = "#FFAB00"; // Line color
        ctx.lineWidth = lineWidth;
        ctx.stroke();
      });
    };

    // Example of an animation loop
    const loop = () => {
      draw();

      updatePosition();

      // Schedule next frame
      rafRef.current = requestAnimationFrame(loop);
    };

    // Call it once now to initialize
    resize();
    // Initialize the lines in the canvas
    initializeLines();

    // Event listeners
    window.addEventListener("resize", resize);
    canvas.addEventListener("pointermove", onPointerMove);
    canvas.addEventListener("pointerleave", onPointerLeave);
    canvas.addEventListener("touchend", onTouch);

    // --- Start the animation loop
    rafRef.current = requestAnimationFrame(loop);

    // Cleanup when component unmounts
    return () => {
      // Stop the animation if still running
      if (rafRef.current) cancelAnimationFrame(rafRef.current);

      // Remove event listener
      window.removeEventListener("resize", resize);
      canvas.removeEventListener("pointermove", onPointerMove);
      canvas.removeEventListener("pointerleave", onPointerLeave);
      canvas.removeEventListener("touchend", onTouch);
    };
  }, []);

  // Return the canvas element, filling the parent container
  return (
    <div className="w-full h-full relative overflow-hidden border-2">
      <canvas
        ref={canvasRef} // Link React ref to this canvas element
        className="w-full h-full block"
      />
    </div>
  );
};

export default MagneticFilings;
