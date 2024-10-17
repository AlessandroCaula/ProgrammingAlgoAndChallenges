import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import Main from "./components/Main"
import { useState } from "react"
// Main Functional component. The highest hierarchical compoenent. The one that is rendered from the index.html.
// The index.html renders the "root" in the Main.jsx which set the root as this App.jsx component. 
// All the others components (i.e. Footer, Main, SideBar, etc.) are rendered here, in the App.jsx component. 
function App() {
  // Using a state variable in order to make the page reactive. In this case the default value will be false.
  const [showModel, setShowModel] = useState(false);

  // Create a function for dealing with the click on the (i) button, in th footer page, which click should show the SideBar with the description of the image.
  // This function will be then taken and passed to the footer as a prop.
  // We want then to pass the same function to the sideBar, so that when the button of the sideBar is clicked, the SideBar hides.
  function handleToggleModel() {
    // Call the setter function to set the new state of the showModel, by inverting its previous value.
    setShowModel(!showModel);
  }

  return (
    <>
      <Main />
      {/*Now we can conditionally render the SideBar by using the showModel state. If it is true, we will render the SideBar, by using the &&.*/}
      {/*!!!! You cannot use regular if statements directly inside the curly braces {} like that. The reason is that JSX expects expressions, not statements, and an if statement is a statement.*/}
      {showModel && (
        <SideBar handleToggleModel={handleToggleModel} />
      )}
      {/*Pass the handleToggleModal function as a prop to the footer component*/}
      <Footer handleToggleModel={handleToggleModel} />
    </>
  )
}

export default App
