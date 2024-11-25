/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  /** Include the dark class. darkMode: "class" => means that based on a simple class we'll be able to change the theme*/
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        chestnut: '#973F29',
      },
    },
  },
  plugins: [],
}
