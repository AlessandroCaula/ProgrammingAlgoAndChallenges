import React from 'react'

// In Next.js, routing refers to the way pages are organized and accessed within the application. 
// Next.js provides a file-based routing system, meaning that the structure of your files in the pages directory determines the routes (URLs) of your application.

// This is gonna render at /posts

const page = () => {
    return (
        <div>POSTS</div>
    )
}

export default page

// Data fetching with Next.js
//
// 1. Server Side Rendering (SSR)
// 2. Static Side Generation (SSG)
// 3. Incremental Static Generation (ISR)