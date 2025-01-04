# Error handling

In Next.js, an `error.tsx` file is used to define custom error handling for specific routes or layouts. It allows you to gracefully handle unexpected errors that occur during the rendering of pages, components, or layout within a specific part of your application. 

## Key Features of `error.tsx`

1. **Localize Error Handling:**
    - Each route or layout can have its own `error.tsx`, allowing tailored error messages or recovery options. 
2. **Automatic Fallback:**
    - When an error occurs in a route or component, Next.js automatically renders the closest `error.tsx` in the hierarchy.
3. **Error Boundary:**
    - Acts as an error boundary for that specific part of the application. 

## How to Use `error.tsx`

**1. Create `error.tsx`**   

Place the `error.tsx` file within a specific layout or route directory.  

**File structure Example:**
```go
app/
  dashboard/
    layout.tsx
    error.tsx  <--
    page.tsx 
  profile/
    layout.tsx
    error.tsx <--
    page.tsx
```

**2. Define the Error Component**

The `error.tsx` file must export a default component that receives an `error` and `reset` function as props.

```tsx
// app/dashboard/error.tsx

'use client';

import { useEffect } from 'react';

export default function Error({ error, reset }: { error: Error; reset: () => void }) {
  // Log the error (optional)
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div>
      <h2>Something went wrong in the Dashboard.</h2>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

## Parameters Passed to the Component

- `error`:
    - The error object that caused the rendering of the `error.tsx`.
    - Contains details about the error (e.g. message, stack trace).
- `reset`:
    - A function to retry rendering. When invoked, it attempts to re-render the component that caused the error.

## How It Works

1. When an error occurs in any child component of the layout or page where `error.tsx` is defined, Next.js:
    - Stops rendering the broken components.
    - Falls back to the `error.tsx` for that route. 
2. If no `error.tsx` exists for a specific route, the error propagates to the nearest parent layout's `error.tsx` or the global error handling if defined. 

## Global Error Handling

You can also define an `error.tsx` in the root `app/` directory to handle errors that aren't caught by specific routes or layouts.

**Example:**

```go
app/
    error.tsx
```

## Common Use Cases

1. **Custom Error Messages:**
    - Display meaningful messages for different sections of your app.  
2. **Retry Logic:**
    - Provide users with a way to retry rendering after a failure.   
3. **Logging:**
    - Send error details to an external service for debugging. 

## Caveats

1. **Client-Side Only:**
    - The `error.tsx` file must be `'use client'` because error boundaries are client-side features. 
2. **Does Not Handle Server Errors:**
    - It handles runtime errors during rendering, not API or server-side errors.