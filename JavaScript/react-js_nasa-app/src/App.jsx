import Footer from "./components/Footer"
import SideBar from "./components/SideBar"
import Main from "./components/Main"
import { useEffect, useState } from "react"

// Main Functional component. The highest hierarchical compoenent. The one that is rendered from the index.html.
// The index.html renders the "root" in the Main.jsx which set the root as this App.jsx component. 
// All the others components (i.e. Footer, Main, SideBar, etc.) are rendered here, in the App.jsx component. 
function App() {

  // Define a new Stae variable used to store the fetched data coming from the NASA API. useState variable with a default value of null.
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  // Using a state variable in order to make the page reactive. In this case the default value will be false.
  const [showModel, setShowModel] = useState(false);

  // Create a function for dealing with the click on the (i) button, in th footer page, which click should show the SideBar with the description of the image.
  // This function will be then taken and passed to the footer as a prop.
  // We want then to pass the same function to the sideBar, so that when the button of the sideBar is clicked, the SideBar hides.
  function handleToggleModel() {
    // Call the setter function to set the new state of the showModel, by inverting its previous value.
    setShowModel(!showModel);
  }

  // !! Fetching data from an API. To do so in React we use the State useEffect hook. The useEffect, takes as input an arrow function and a dependecy array. 
  // The array is knwo as the dependency array, and the arrow function is the logic to be executed whenever the requirements of the dependecy array are satisfied. 
  // If we have a blanck dependency array that says to run the useEffect arrow function whenever the web page loads. 
  // If we instead have a variable in the dependecy array, the code inside the useEffect arrow function is executed when that variable changes. 
  // In this case we want to fecth the information when our page loads. So we will leave the dependecy array empty.
  useEffect(() => {

    // Using an async function. The async function allows the use of the await keyword within its body. This makes it easier to work with promises and handle asynchronous operations, such as fetching data from an API or performing I/O operations, without blocking the main thread.
    // Fetching Data: When you need to retrieve data from APIs or databases asynchronously, using async functions makes it easier to handle the result.
    async function fetchAPIData() {

      // Accessing the value of the API key.
      const NASA_KEY = import.meta.env.VITE_NASA_API_KEY;
      // The url of the APOD API. https://api.nasa.gov/ Access it with the API key.
      const url = 'https://api.nasa.gov/planetary/apod' + `?api_key=${NASA_KEY}`;
      
      // !!! Chache the informations. So that we avoid burning through our local storage call. (There are a maximum number of API call for the NASA API, something like 1000).
      const today = (new Date()).toDateString();
      // Define our local Key
      const localKey = `NASA-${today}`;
      // Now check if in   our localStorage exist a localKet. If it exist we can fecth the data from localStorage.
      if (localStorage.getItem(localKey)) {
        // Accessing the data which is already stored in the localStorage as out localKey.
        // Parsing the JSON file to access the stored Data in the localStorage.
        const apiData = JSON.parse(localStorage.getItem(localKey));
        setData(apiData);
        console.log('Fetched from cache today');
        return;
      }
      // If there is no data saved as localKey in the localStorage. We are gonna clear everything in the local storage, and then after having retrieved and fetch the data in the try block, we are gonna store it in the localStorage.
      localStorage.clear();

      // Define a try and catch block to handle Errors.
      try {
        // Fetching the data.
        const response = await fetch(url);
        // Retrieve some JSON text from the response.
        const apiData = await response.json();
        // Chache the retrieved data in the localStorage. So that if I enter the site more time in the same day, I don't have to fetch the data every time but I can use the one already stored in the localStorage.
        localStorage.setItem(localKey, JSON.stringify(apiData));
        console.log('Fetched from API today');
        // Setting the loaded api data to the data State.
        setData(apiData);
        console.log('DATA\n', apiData);
      } catch (err) {
        // When we get an error, give a message.
        console.log(err.message);
      }
    }
    // Call the method to fecth the data that we have just defined.
    fetchAPIData();
  }, [])

  return (
    <>
      {/*When we have fetched the data from the API, that's actually when we want to show the main. Only when we have the data we will show the main.*/}
      {data ? (<Main data={data}/>) : (
        /*If the Data has not been fetched, we visuailze a gear icon. You can see it by commenting the fetchAPIData() call in the useEffect State*/
        <div className="loadingState">
          <i className="fa-solid fa-gear"></i>
        </div>
      )}
      {/*Now we can conditionally render the SideBar by using the showModel state. If it is true, we will render the SideBar, by using the &&.*/}
      {/*!!!! You cannot use regular if statements directly inside the curly braces {} like that. The reason is that JSX expects expressions, not statements, and an if statement is a statement.*/}
      {/*Passing the fetched data as a prop to the SideBar to visualize the title and explanation of the images*/}
      {showModel && (
        <SideBar data={data} handleToggleModel={handleToggleModel} />
      )}
      {/*Pass the handleToggleModal function as a prop to the footer component*/}
      {/*Also the footer component needs to be conditioned to the data. When there is no data, the footer it is not rendered.*/}
      {/*Passing the fetched data as prop to the Footer as well to display the title of the images*/}
      {data && (
        <Footer data={data} handleToggleModel={handleToggleModel} />
      )}
    </>
  )
}

export default App
