// By adding the use client, we are saying that this component needs to run on the client side (web browser). This is needed for example when the user can interact with the component.
"use client";

// Actually, everything within the client component that doesn't require interactivity or isn't dependent on the browser is still rendered on the server. In this case this component it is indeed rendered on the server as well, even if we have specified that it needs to be a client component. This is server-side pre-rendering. 

// A good rule-of-thumb when deciding if we need Next.js to leave the component as a server component, or manually change it to a client component by adding "use client", is to leave it as a server component UNTIL you need some browser interactivity -> At that point change it to a client component. Refer to this guide when unsure (https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns)

function Hello() {
  console.log("I am a Client Component");

  return (
    <div>
      <h1>Hello</h1>
    </div>
  );
}

export default Hello;
