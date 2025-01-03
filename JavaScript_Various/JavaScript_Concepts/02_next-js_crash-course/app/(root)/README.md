# Route Groups (root) or (dashboard)

Are a feature introduced in the App router (app/directory) to organize routes and structure your application without affecting the URL structure. They allow you to group related components or pages together logically without impacting the actual routes or navigation paths. 

## Key Features of Route Groups:
1. **Logical Grouping**:
    - Group files and components together for better project structure and readability.
    - Does not appear in the final URL path. 
2. **Seamless Routing**:
    - Keeps the URL consistent even if your files are nested inside a group folder. 
3. **Better Code Organization**:
    - Useful for organizing layout files, loading states, error handling, etc. Specific to a part of the application. 

---

## How Route Groups Work

- You can create a **route group** by prefixing a folder name with parentheses `(` `)` in the `app/` directory. 
- Any files inside the group folder will not include the folder's name in the route. 

### Example
Given the following folder structure:
```
app/
  (admin)/
    dashboard/
      page.js
    settings/
      page.js
  profile/
    page.js
```
- **Route Outputs**:
    - `/dashboard` &rarr; Maps to `app/(admin)/dashboard/page.js`
    - `/settings` &rarr; Maps to `app/(admin)/settings/page.js`
    `/profile` &rarr; Maps to `app/(admin)/profile/page.js`

Notice that the `admin` folder (route group) does not appear in the URLs.

---

## When to Use Route Groups

- **Separate Concerns**: Group related pages or components logically (e.g. admin, routes, user routes).
- **Shared Layouts**: Apply a specific layout or middleware to certain groups od routes. 
- **Improve File Organization**: For large apps, route groups make it easier to manage complex file structures. 

---

## Practical Benefits

1. **Apply different Layouts**:
    - Each route group can have its own layout that wraps its child pages.
    - Example:
    ```
    app/
        (marketing)/
        layout.js  // A layout specific to marketing routes
        home/
            page.js
        about/
            page.js
    ```

2. **Error and Loading States**
    - Group routes for specific error or loading handlers. 
    - Example:
    ```
    app/
      (user)/
        layout.js
        error.js
        loading.js
    ```

3. **Code Splitting**
    - Route groups enable better bundling and lazy loading for large apps.