# Fetching Data in **Next.js**

In **Next.js**, the proper way to fetch data depends on **where** and **when** you want the data to be fetched and rendered. The framework provides specific lifecycle method for this.

---

## 1. `getServerSideProps` (Server-Side Rendering - SSR)

- Fetches data **on the server at request time**.
- Suitable for dynamic content that needs to be fresh for every request (e.g. user-specific data, live updates)

```js
export async function getServerSideProps(context) {
  const res = await fetch("https://api.example.com/data");
  const data = await res.json();

  return { props: { data } }; // The data is passed as props to the page component
}

export default function Page({ data }) {
  return <div>{data.title}</div>;
}
```

---

## 2. `getStaticProps` (Static Site Generation - SSG)

- Fetches data **at build time**
- Suitable for static content that doesn't change often (e.g., blog posts, product listing).

```js
export async function getStaticProps() {
  const res = await fetch("https://api.example.com/data");
  const data = await res.json();

  return { props: { data } }; // Data is embedded in the static HTML
}

export default function Page({ data }) {
  return <div>{data.title}</div>;
}
```

## 3. Client-Side Fetching

- Done with React's `useEffect`, usually for **dynamic interaction** (e.g., search, filters) or **hydrating static content**.
- This method still works in Next.js but is typically used alongside SSR/SSG for data updates after the initial render.

```js
import { useEffect, useState } from "react";

export default function Page() {
    const [data, setData] = useState(null);

    useEffect(() => {
        async function fetchData() {
            const res = await fetch('https://api.example.com/data');
            const result = await res.json()l
            setData(result);
        }
        fetchData();
    }, []);

    return <div>{data ? data.title : 'Loading...'}</div>;
}
```

---

## Fetching Data in React.js

React does not have a server-side rendering feature built-in. All data fetching is done **on the client-side** using hooks like `useEffect`.

```js
import { useEffect, useState } from "react";

export default function Page() {
  const [data, setData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      const res = await fetch("https://api.example.com/data");
      const result = await res.json();
      setData(result);
    }
    fetchData();
  }, []);

  return <div>{data ? data.title : "Loading..."}</div>;
}
```
- This data is fetched only **after** the page is loaded in the browser.
- There's no static generation or server-side pre-rendering. 

---

## Key Differences: Next.js vs React.js

| **Aspect**                 | **Next.js**                                     | **React.js**                                   |
|----------------------------|------------------------------------------------|-----------------------------------------------|
| **Server-Side Fetching**   | Supports `getServerSideProps` for SSR.          | Not available. Data is fetched on the client. |
| **Static Generation**      | Supports `getStaticProps` for SSG.              | Not available.                                |
| **Pre-Rendering**          | Pre-renders HTML on the server (SSG/SSR).       | No pre-rendering; relies on client rendering. |
| **SEO Benefits**           | Fully rendered HTML is sent to crawlers.        | Requires additional libraries for SSR/SSG.   |
| **Performance**            | Faster load with SSG, and less JS runtime work. | All rendering happens in the browser.         |

---

# Summary

In **Next.js**, fetching data can happen on the server (`getServerSideProps`) or at build time (`getStaticProps`), giving you better SEO and faster performance. In **React.js**, you fetch all data client-side, which can lead to slower initial loads and less SEO-friendly pages. **Next.js enhances React's functionality for more advanced use cases**.