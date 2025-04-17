import Switch from '@mui/material/Switch';
import { createGlobalStyle, ThemeProvider } from "styled-components";

import { useDarkMode } from "./utils/useDarkMode"

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
  const { theme, toggleTheme, isDarkMode } = useDarkMode();

  return (
    <div className="App">
      <ThemeProvider theme={theme}>
        <GlobalStyles />
        <h1>Switch themes</h1>
        <h2>With useDarkMode hook</h2>
        <h2>and styled-components!</h2>
        <p>
          <strong>{isDarkMode ? "Dark Mode" : "Light Mode"}</strong>
        </p>
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
