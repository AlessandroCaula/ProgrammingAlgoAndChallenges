import { useState } from "react"

// Creating a THEME mapper to keep our string values
const THEME = {
  default: "default",
  dark: "dark"
}

// Adding defaultTheme objects with CSS properties
const defaultTheme = {
  background: "#FAFAFA",
  text: "#212121"
}

// Adding darkModeTheme objects with CSS properties
const darkModeTheme = {
  background: "#212121",
  text: "#FAFAFA"
}

// Mapping string values to a theme object.
// By wrapping it in square brackets, the value of THEME.default is used as the key in the THEME_MAPPER object
// By using [THEME.default], the key becomes "default", which is the value stored in THEME.default
const THEME_MAPPER = {
  [THEME.default]: defaultTheme,
  [THEME.dark]: darkModeTheme
}

// Hook that will keep track of the currently selected theme sting value.
export const useDarkMode = () => {
  const [theme, setTheme] = useState(THEME.default)

  // Switches currently selected theme string value
  const toggleTheme = () => {
    theme === THEME.default ? setTheme(THEME.dark) : setTheme(THEME.default)
  }

  // Returning the theme object based on the string value (using THEME_MAPPER), toggle function, and isDarkMode boolean which we'll use in our App.js
  return {
    theme: THEME_MAPPER[theme],
    toggleTheme,
    isDarkMode: theme === THEME.dark
  }
}