// This is a nested routes. From the dashboard route you can reach the analytics and the users routes. 

import Link from "next/link"

const page = () => {
  // In this case we are gonna dynamically create a specific rout for each specific user. This is thanks to the [id] (dynamic rout) that we have created inside this user route (folder). 
  return (
    <div>
      <h1>Dashboard Users</h1>

      {/* Create an unordered <ul> list which will contain all the users. */}
      <ul className="mt-10">
        {/* In order to make the user clickable, and being redirected to its own dynamic route, we can use the next.js link component */}
        <li><Link href="users/1">User 1</Link></li>
        <li><Link href="users/2">User 2</Link></li>
        <li><Link href="users/3">User 3</Link></li>
        <li><Link href="users/4">User 4</Link></li>
      </ul>
      
    </div>
  )
}

export default page