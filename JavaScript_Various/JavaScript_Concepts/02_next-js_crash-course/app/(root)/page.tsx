import Hello from "../components/hello";

export default function Home() {
  // Check if this component is rendered on the server or on the client.
  console.log("what am I? -- SERVER/CLIENT?");
  // Since it is a server side component (every component is automatically converted to a server component with Next.js) you should not being able to see this console.log. You can still see it by inspecting the web page (F12), with a "server" tag. You can as well see it directly in the terminal.

  return (
    <>
      <h1 className="text-3xl">Welcome to Next.js test </h1>

      {/* The Hello component is a client component */}
      <Hello />
    </>
  );
}
