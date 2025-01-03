// Now this is a dynamic route, cause we have put the square brackets in the [id] route. So it can change. In this way we will be able to have a specific rout, /users/... for, i.e., each user. For each user we will have its own rout. /users/user-1, /users/user-2, /users/user-3.. /users/user-n.

// From the params objects, we can extract to which route of the dynamic one it is requested. Meaning, which user has been clicked. Since we are using TypeScript, we have to specify the type of the params. Params will be an object containing a single "id" that should be of the type string. We know that the only object that will be in the params object is the id because we called the dynamic route id within the square brackets [id].
const page = ({ params }: { params: { id: string } }) => {
  // Destructure the id from params.
  const { id } = params;

  return (
    // Rendering the h1 text with the id that comes directly from the params when the user clicks on a certain user in the user page.
    <h1 className="text-3xl">User Profile: {id}</h1>
  );
};

export default page;
