import React, { useRef, useEffect } from "react";

// Configuration interface defining all tunable parameters of the simulation
interface Settings {
  particleCount: number;     // Number of particles on screen
  particleRadius: number;    // Average radius of each particle
  maxSpeed: number;          // Maximum allowed particle velocity
  attractStrength: number;   // Strength of the magnetic attraction to the pointer
  minDistance: number;       // Minimum distance to avoid infinite attraction
  friction: number;          // Friction factor applied to slow particles over time
  respawnWhenFar: boolean;   // Whether to respawn particles when they go too far away
  respawnMargin: number;     // Margin outside canvas before a particle respawns
}

// Default configuration constants
const SETTINGS: Settings = {
  particleCount: 600,
  particleRadius: 1.2,
  maxSpeed: 8,
  attractStrength: 600,
  minDistance: 20,
  friction: 0.92,
  respawnWhenFar: true,
  respawnMargin: 200,
};

// Particle structure — each one has position, velocity, and radius
interface Particle {
  x: number;
  y: number;
  vx: number;
  vy: number;
  r: number;
}

// Pointer data — stores cursor position and whether it's active
interface Pointer {
  x: number;
  y: number;
  active: boolean;
}

// Helper function to generate random numbers in a range
function rand(min: number, max: number): number {
  return Math.random() * (max - min) + min;
}

// Props interface — allows customizing the particle count externally
interface MagneticFilingsProps {
  particleCount?: number;
}

const MagneticMouse: React.FC<MagneticFilingsProps> = ({
  particleCount = SETTINGS.particleCount, // Default to SETTINGS value if not provided
}) => {
  // Refs for persistent mutable data (React won’t re-render when these change)
  const canvasRef = useRef<HTMLCanvasElement | null>(null); // Reference to canvas element
  const particlesRef = useRef<Particle[]>([]);              // Store all particle data
  const pointerRef = useRef<Pointer>({                      // Store current pointer info
    x: -9999,                                               // Offscreen initial position
    y: -9999,
    active: false,
  });
  const rafRef = useRef<number>();                          // Store the animation frame ID

  useEffect(() => {
    // Get canvas and 2D rendering context
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    // Track canvas dimensions
    let width = 0;
    let height = 0;
    const DPR = window.devicePixelRatio || 1; // Handle high-DPI (Retina) displays

    // Adjust canvas size and scaling when window resizes
    const resize = () => {
      width = canvas.clientWidth;
      height = canvas.clientHeight;
      canvas.width = Math.floor(width * DPR);
      canvas.height = Math.floor(height * DPR);
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0); // Scale drawing context for sharp rendering
    };

    // Initialize all particles with random positions and velocities
    const initParticles = () => {
      particlesRef.current = Array.from({ length: particleCount }, () => ({
        x: rand(0, width),             // Random X position
        y: rand(0, height),            // Random Y position
        vx: rand(-1, 1),               // Random X velocity
        vy: rand(-1, 1),               // Random Y velocity
        r: SETTINGS.particleRadius * (0.6 + Math.random() * 0.9), // Slight radius variation
      }));
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

    // Core physics update — runs every animation frame
    const update = (dt: number) => {
      const particles = particlesRef.current;
      const { x: px, y: py, active } = pointerRef.current;

      for (const p of particles) {
        // Vector from particle to pointer
        let dx = px - p.x;
        let dy = py - p.y;
        const distSq = dx * dx + dy * dy;

        // If pointer active and within influence range
        if (active && distSq < 1e8) {
          const dist = Math.sqrt(distSq);
          const clamped = Math.max(dist, SETTINGS.minDistance); // Avoid too strong forces
          const force = SETTINGS.attractStrength / (clamped * clamped); // Inverse-square law

          // Apply force toward pointer
          const fx = (dx / dist) * force;
          const fy = (dy / dist) * force;
          p.vx += fx * dt;
          p.vy += fy * dt;
        } else {
          // Add slight random motion (Brownian-like)
          p.vx += (Math.random() - 0.5) * 0.02;
          p.vy += (Math.random() - 0.5) * 0.02;
        }

        // Apply friction
        p.vx *= SETTINGS.friction;
        p.vy *= SETTINGS.friction;

        // Limit max speed
        const speedSq = p.vx * p.vx + p.vy * p.vy;
        const maxSpeedSq = SETTINGS.maxSpeed * SETTINGS.maxSpeed;
        if (speedSq > maxSpeedSq) {
          const s = Math.sqrt(speedSq);
          p.vx = (p.vx / s) * SETTINGS.maxSpeed;
          p.vy = (p.vy / s) * SETTINGS.maxSpeed;
        }

        // Update particle position
        p.x += p.vx * dt * 60;
        p.y += p.vy * dt * 60;

        // Handle off-screen behavior
        if (SETTINGS.respawnWhenFar) {
          // Respawn particle if it drifts too far away
          if (
            p.x < -SETTINGS.respawnMargin ||
            p.x > width + SETTINGS.respawnMargin ||
            p.y < -SETTINGS.respawnMargin ||
            p.y > height + SETTINGS.respawnMargin
          ) {
            p.x = rand(0, width);
            p.y = rand(0, height);
            p.vx = rand(-0.6, 0.6);
            p.vy = rand(-0.6, 0.6);
          }
        } else {
          // Bounce back if hitting the borders
          if (p.x < 0 || p.x > width) p.vx *= -0.8;
          if (p.y < 0 || p.y > height) p.vy *= -0.8;
        }
      }
    };

    // Draw all particles
    const draw = () => {
      ctx.clearRect(0, 0, width, height); // Clear previous frame
      ctx.save();
      ctx.globalCompositeOperation = "lighter"; // Additive blending for glow effect
      const particles = particlesRef.current;

      for (const p of particles) {
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(30, 40, 60, 0.9)";
        ctx.fill();
      }

      ctx.restore();
    };

    // Animation loop with delta time for smooth motion
    let last = performance.now();
    const loop = (now: number) => {
      const dt = Math.min(0.05, (now - last) / 1000); // Limit large frame jumps
      last = now;
      update(dt);
      draw();
      rafRef.current = requestAnimationFrame(loop); // Continue the loop
    };

    // Initial setup
    resize();
    initParticles();

    // Event listeners
    window.addEventListener("resize", resize);
    canvas.addEventListener("pointermove", onPointerMove);
    canvas.addEventListener("pointerleave", onPointerLeave);
    canvas.addEventListener("touchmove", onTouch, { passive: true });
    canvas.addEventListener("touchend", onPointerLeave);

    // Start animation
    rafRef.current = requestAnimationFrame(loop);

    // Cleanup on component unmount
    return () => {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
      window.removeEventListener("resize", resize);
      canvas.removeEventListener("pointermove", onPointerMove);
      canvas.removeEventListener("pointerleave", onPointerLeave);
      canvas.removeEventListener("touchmove", onTouch);
      canvas.removeEventListener("touchend", onPointerLeave);
    };
  }, [particleCount]);

  // JSX: wrapper div and the full-size canvas
  return (
    <div
      style={{
        width: "100%",
        height: "100vh",
        position: "relative",
        overflow: "hidden",
      }}
    >
      <canvas
        ref={canvasRef}
        style={{
          width: "100%",
          height: "100%",
          display: "block",
          touchAction: "none",
        }}
      />
    </div>
  );
};

export default MagneticMouse;
