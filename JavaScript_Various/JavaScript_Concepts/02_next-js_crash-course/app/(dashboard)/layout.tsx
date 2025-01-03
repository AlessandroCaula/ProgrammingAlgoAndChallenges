// With next.js you can create additional layouts if necessary. Let's say you want to render a specific UI just for the dashboard routes, we can do that by adding another "layout.tsx" (like we did with this file) within dashboard. The name has to be "layout".
// So in this case all the dashboard routes (users and analytics) will share the common UI that are specified in this layout. In this case they will all have the DASHBOARD text.

import React from "react";

const layout = ({ children }: { children: React.ReactNode }) => {
  return (
    // Within this div we can then render children
    <div>
      {/* The children in this case will be all other pages that you are showing within this layout. But if you want to add some i.e. special navBar that is shared among all the children you can add it to the layout here */}
      <h1 className="text-3xl">DASHBOARD</h1>
      {children}
    </div>
  );
};

export default layout;
