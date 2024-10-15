import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import Main from "./components/Main"
// Main Functional component. The highest hierarchical compoenent. The one that is rendered from the index.html.
// The index.html renders the "root" in the Main.jsx which set the root as this App.jsx component. 
// All the others components (i.e. Footer, Main, SideBar, etc.) are rendered here, in the App.jsx component. 
function App() {

  return (  
    <>
      <Main />
      <SideBar>Text from the SideBar</SideBar>
      <Footer />
    </>
  )
}

export default App
