// We are now creating a new routing. Therefore, in your web page, if you add "/about" in your url it will render this component.
// In next.js folder are used to create routes, and the tsx file within the folder it becomes the file that gets rendered for that route.

const page = () => {
  return (
    <div>About</div>
  )
}

export default page