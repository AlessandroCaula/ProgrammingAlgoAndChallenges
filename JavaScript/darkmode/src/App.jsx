// Using styled-components (https://styled-components.com/), 
// Material UI Switch Component (https://mui.com/material-ui/react-switch/#switch), and a little bit of JSX to create this example application
import Switch from '@mui/material/Switch';
import { createGlobalStyle, ThemeProvider } from "styled-components";

import { useDarkMode } from "./utils/useDarkMode"

// GlobalStyle component is used to apply CSS to html tag based on the selected theme.
const GlobalStyles = createGlobalStyle`
  html {
    background: ${({ theme }) => theme.background};
    color: ${({ theme }) => theme.text};
    font-family: Arial, Helvetica, sans-serif;
    transition: all 0.3s;
    text-align: center;
  }
`;

function App() {
  // We use the useDarkMode hook to get all 3 previously mentioned properties.
  const { theme, toggleTheme, isDarkMode } = useDarkMode();

  return (
    <div className="App">
      {/* Supply the currently selected theme to the ThemeProvider, thanks to that the theme can be used in the GlobalStyles component */}
      <ThemeProvider theme={theme}>
        <GlobalStyles />
        <h1>Switch themes</h1>
        <h2>With useDarkMode hook</h2>
        <h2>and styled-components!</h2>
        <p>
          <strong>{isDarkMode ? "Dark Mode" : "Light Mode"}</strong>
        </p>
        {/* Toggle us created using Switch component and we assign checked={isDarkMode} and onChange={toggleTheme} to it */}
        <Switch
          checked={isDarkMode}
          onChange={toggleTheme}
          name="darkModeSwitch"
          color="primary"
        />
      </ThemeProvider>
    </div>
  )
}

export default App
