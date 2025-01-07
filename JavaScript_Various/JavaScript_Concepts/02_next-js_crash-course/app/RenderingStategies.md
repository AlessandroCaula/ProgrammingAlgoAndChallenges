# Static Site Generation (SSG)

Is a method in Next.js where HTML pages are pre-rendered at **build-time** instead of at runtime (the content is created when you deploy your site, not when a user requests it. It is extremely fast). This means that the HTML for a page is generated once during the build process and then served as static files to users.

### Key Features of SSG:

- **Pre-rendered HTML**: Pages are generated ahead of time with all content in place.
- **Faster Performances**: Since pre-generated HTML is served, no rendering is required on the server or client at request time.
- **SEO-Friendly**: Search engines can easily crawl and index the pre-rendered HTML.
- **Build-Time Data Fetching**: You can fetch data during the build process using `getStaticProps`.

### Example of SSG in Next.js

```js
export async function getStaticProps() {
  const data = await fetch("https://api.example.com/data").then((res) =>
    res.json()
  );

  return {
    props: {
      data,
    },
  };
}

export default function Page({ data }) {
  return (
    <div>
      <h1>Static Site Generation Example</h1>
      <p>{data.title}</p>
    </div>
  );
}
```

### When to Use SSG:

- When the content does not change frequently (eg, blogs, documentation).
- When you prioritize performance and SEO.

**It is not suitable for website that need frequently update content**

---

# Incremental Static Regeneration (ISR)

https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration

Is a feature in **Next.js** that allows you to update static pages **after the site has been built** without needing to rebuild the entire site. ISR enables you to regenerate static pages on demand while keeping the benefits of **Static Site Generation (SSG)**, like performances and SEO.

### Key Features of ISR

- **On-demand page regeneration**: Pages can be regenerated after a certain interval, without rebuilding the entire site.
- **Dynamic content with static performance**: It combines the advantages of static content (fast loading) with dynamic data (ability to update content).
- **Background regeneration**: When a request is made for a page that has expired, it is regenerated in the background, and the new content is served for future requests.
- **Configurable Revalidation Time**: You can set a time interval to control how often the page should be regenerated.

### Example of ISR in Next.js

```js
export async function getStaticProps() {
  const data = await fetch("https://api.example.com/data").then((res) =>
    res.json()
  );

  return {
    props: { data },
    revalidate: 60, // Page will be regenerated every 60 seconds
  };
}

export default function Page({ data }) {
  return (
    <div>
      <h1>Incremental Static Regeneration (ISR) Example</h1>
      <p>{data.title}</p>
    </div>
  );
}
```

### How it Works:

1. **Initial Static Generation**: On the first request, the page is generated and served as a static page (like traditional SSG).
2. **Regeneration Interval**: When the `revalidate` value (set in `getStaticProps`) expires, Next.js will regenerate the page in the background for subsequent requests.
3. **Serving State Content**: During the regeneration process, the old (state) content will still be served until the new version is ready.

### Advantage of ISR:

- **Fresh Data**: Allows you to keep static pages fresh without rebuilding the entire site.
- **Scalable**: You can use ISR on large sites, where rebuilding the whole site for every small change would be inefficient.
- **Improved Performance**: The static page is served to users until the regeneration happens, ensuring fast loading.

### Use Case for ISR

- **E-commerce websites**: Product prices, stock levels, or other dynamic data can be kept up-to-dat without rebuilding the entire site.
- **Blogs or new sites**: When you want to regularly update articles but don't need to regenerate the whole website on every change.

### comparison with SSG:

- **SSG**: Pages are generated at build time and are static until the next build.
- **ISR**: Pages are generated at build time but can be re-generated on-demand with a specified revalidation period, making content more dynamic.

## Time-based revalidation

In Next.js is a feature used with **Incremental Static Regeneration (ISR)** that allows static pages to be revalidated at regular intervals. You specify the revalidation period (in seconds) using the `revalidate` property in `getStaticProps`.  
This ensure that the page's content is kept up-to-date without requiring a full rebuild of the application.

### How It Works:

1. **Initial Build**: The page is pre-rendered as a static page during the build process or on the first request.
2. **Serving Cached Page**: The page remains static and is served as-is until the revalidation time expires.
3. **Background Revalidation**:

- When a new request is made **after the revalidation period**, the page is regenerated in the background.
- The old pafe is served to the user until the new one is ready.

4. **Serving Updated Page**: Subsequent requests will serve the newly regenerated page.

### Example: Time-based Revalidation

Here’s how to set up time-based revalidation in `getStaticProps`:

```js
export async function getStaticProps() {
  const data = await fetch("https://api.example.com/data").then((res) =>
    res.json()
  );

  return {
    props: { data },
    revalidate: 60, // Revalidate every 60 seconds
  };
}

export default function Page({ data }) {
  return (
    <div>
      <h1>Time-based Revalidation Example</h1>
      <p>{data.title}</p>
    </div>
  );
}
```

### Key Points:

- **`revalidate` property**:
  - It defines the number of seconds before the page is eligible for regeneration.
  - Example: revalidate: 60 means the page will regenerate every 60 seconds.
- **Background Process**:
  - Revalidation happens in the background without impacting the user experience.
    Old content is served until the new one is ready.

### Advantages of Time-based Revalidation:

1. **Fresh Content**: Ensures content is updated regularly without manual intervention.
2. **Improved Performance**: Maintains fast load times by serving static pages while still allowing updates.
3. **Efficient Updates**: Reduces the need for a full site rebuild for minor content changes.
4. **SEO-friendly**: Static pages generated are optimized for search engines.

### Use Cases:

- **E-commerce**: Keeping product prices or stock availability up-to-date.
- **News sites**: Regularly updating breaking news headlines.
- **Event listings**: Periodically refreshing event schedules.

---

# Server Side Rendering (SSR)

**Server-Side Rendering (SSR)** in Next.js means that the content of a page is dynamically generated on the server for every request. This ensures that users always receive up-to-date content but at the cost of slightly slower page loads compared to static pages.

The content of the page is created dynamically for each user request and not only for each deployment. It's slower than SSG and puts more load on the server, but you'll always have up-to-date content. This is ideal for highly dynamic content or pages that needs real-time data.

### How SSR Works:

1. **Request Made**:
   - When a user requests a page, Next.js calls the page’s getServerSideProps() function on the server.
2. **Data Fetching**:
   - The server fetches necessary data (e.g., from a database, API, etc.) within getServerSideProps().
3. **Page Generation**:
   - The server dynamically generates the HTML for the page using the fetched data.
4. **Response Sent**:
   - The server sends the fully rendered HTML page to the user's browser.

### Key Characteristics:
1. **Runs on Each Request**:
    - `getServerSideProps()` is called on the server every time a request is made for the page.
2. **Data Fetching**:
    - You can fetch data directly from a database, an external API, or other sources.
3. **SEO-Friendly**:
    - The page is fully rendered on the server, making it easy for search engines to index.

### Advantages:
1. **Fresh Data**:
    - Ensures users always see the latest content since it is generated per request.
2. **Dynamic Content**:
    - Ideal for pages with data that changes frequently or is user-specific (e.g., dashboards).
3. **SEO Benefits**:
    - Fully rendered pages improve search engine visibility.

### Disadvantages:
1. **Performance**:
    - Slower than static rendering because the server generates the page on demand.
2. **Server Load**:
    - Increases server processing demands, especially under high traffic.
3. **Caching**:
    - Requires additional strategies like CDN caching to optimize performance.

---

# Partial Prerendering (PPR)
Is a rendering strategy that combines static and dynamic rendering methods to improve performance and handle dynamic content efficiently. It allows you to statically generate a part of your page at build time while keeping other parts dynamic, rendered at runtime. 

### How PPR Works:
1. **Static Part**:
    - the static portion of the page is rendered during the build process, using data available at that time. 
    - This ensures faster load times for the static parts. 
2. **Dynamic Part**:
    - The dynamic content is fetched and rendered on the client or server at runtime, ensuring the most up-to-date information. 

### Use Cases:
1. **Use Cases**:
    - Pages with headers, footers, or other parts that don't change often (static) and sections like user-specific data, comments, or feeds (dynamic).
2. **SEO-Friendly Dynamic Pages**
    - Ensures that search engines can crawl the static parts, while dynamic parts are fetched when necessary.

### Implementing PPR:
1. use **SSG** (`getStaticProps`) to prerender static parts. 
2. Fetch dynamic data on the **client-size** (CSR) or use **SSR** (`getServerSideProps`) for server-rendered dynamic content. 


## Example Implementation:
### Static and Dynamic Content:
```js
export async function getStaticProps() {
  // Fetch static data during build time
  const staticData = await fetch('https://api.example.com/static');
  const staticResult = await staticData.json();

  return {
    props: {
      staticResult,
    },
  };
}

export default function Page({ staticResult }) {
  const [dynamicData, setDynamicData] = React.useState(null);

  React.useEffect(() => {
    // Fetch dynamic data on the client
    async function fetchDynamicData() {
      const response = await fetch('https://api.example.com/dynamic');
      const result = await response.json();
      setDynamicData(result);
    }

    fetchDynamicData();
  }, []);

  return (
    <div>
      <h1>Partial Prerendering Example</h1>
      <h2>Static Content:</h2>
      <p>{JSON.stringify(staticResult)}</p>

      <h2>Dynamic Content:</h2>
      {dynamicData ? <p>{JSON.stringify(dynamicData)}</p> : <p>Loading...</p>}
    </div>
  );
}
```

### Advantages:

1. **Improved Performance**:
    - Static content load quickly while dynamic content is fetched asynchronously.
2. **SEO Benefits**:
    - Search engines can crawl static parts effectively.
3. **Flexibility**L
    - Combines the best of SSG and SSR/CSR.

### When to Use PPR:
- Pages with sections that rarely change and others that are dynamic. 
- E-commerce pages with static product descriptions but dynamic pricing or stock availability. 
- Blogs with static articles but dynamic comments or related post sections. 