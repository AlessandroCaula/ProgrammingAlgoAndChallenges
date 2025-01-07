# Metadata

In **Next.js**, metadata refers to the information used to define properties of a page, such as its title, description, and other meta tags. Metadata plays a crucial role in improving **SEO** (Search Engine Optimization), enhancing user experience, and providing information to social media platforms when sharing links. 

### Types of Metadata in Next.js
1. **Basic Metadata**:
    - Includes common HTML meta tags like `title`, `description`, `keywords`, etc. 
    - Improve SEO and helps search engines understand the content of your page. 
2. **Open Graph Metadata**:
    - Used for rich link previews on social media platforms. 
    - Example: `og:title`, `og:description`, `og:image`.
3. **Twitter Metadata**:
    - Similar to Open Graph but specifically for Twitter.
    - Example: `twitter:title`, `twitter:card`, `twitter:image`
4. **Custom Metadata**:
    - Any additional meta tags you want to include.

### Setting Metadata in Next.js

#### 1. **Using the `head` Component**:
the `Head` component allows you to define metadata directly in a React component.

```js
import Head from "next/head";

export default function Page() {
  return (
    <>
      <Head>
        <title>My Awesome Page</title>
        <meta name="description" content="This is an awesome page built with Next.js." />
        <meta property="og:title" content="My Awesome Page" />
        <meta property="og:description" content="Check out this awesome page built with Next.js!" />
        <meta property="og:image" content="/images/awesome.png" />
        <meta name="twitter:card" content="summary_large_image" />
      </Head>
      <div>
        <h1>Welcome to My Awesome Page</h1>
      </div>
    </>
  );
}
```

#### 2. **Using App Router Metadata API**:
With the Next.js 13+ and the **App Router**, metadata is specified at the layout or page level using the `metadata` object or `generateMetadata` function. 

- **Static Metadata**: Define metadata directly as a static object. 

```js
export const metadata = {
  title: 'My Awesome Page',
  description: 'This is an awesome page built with Next.js.',
  openGraph: {
    title: 'My Awesome Page',
    description: 'Check out this awesome page built with Next.js!',
    images: ['/images/awesome.png'],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'My Awesome Page',
    images: ['/images/awesome.png'],
  },
};
```

- **Dynamic Metadata**: Use the `generateMetadata` function to create metadata dynamically based on data or parameters. 

```js
export async function generateMetadata({ params }) {
  const post = await fetchPost(params.slug);

  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      images: [post.image],
    },
    twitter: {
      card: 'summary_large_image',
      title: post.title,
      images: [post.image],
    },
  };
}
```

### Advantages of Metadata in Next.js
1. **SEO Optimization**:
    - Enhances visibility in search engines. 
    - Improves click-through rates with meaningful titles and descriptions. 
2. **Social Media Integration**:
    - Creates rich link preview with Open Graph and Twitter metadata.
3. **Custom Experience**:
    - Tailors the page's metadata based on user data or dynamic content.
4. **Performance**:
    - Metadata handling is optimized by Next.js for server-side rendering.

### Where Metadata is Used
1. **Static Pages**:
    - Predefined metadata is set in metadata or Head.
2. **Dynamic Pages**:
    - Dynamic metadata is generated using generateMetadata or server-side logic.
3. **Layouts**: 
    - Shared metadata across multiple pages can be defined in layout files.