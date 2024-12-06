// Select the input (color picker) and the p value which will display the RGB values of it.
const colorPicker = document.getElementById("color-picker");
const colorPickerOpposite = document.getElementById("color-picker-opposite");
const colorDisplay = document.getElementById("color-display");
const colorDisplayOpposite = document.getElementById("color-display-opposite");

// Function used to convert from Hex to RGB.
function hexToRgb(hex) {
  // This line of code is used to convert a hexadecimal color value (e.g. #ff0000) into its corresponding numeric value in base 10 (decimal).
  // - hex.slice(1) => the slice(1) method removes the # character from the start of the hex string, leaving only the hex digits.
  // parseInt(string, radix) => Converts a string into an integer based on the specific radix (or base) (16 => hexadecimal)
  // i.e For "ff0000", the result is 16711680.
  const bigint = parseInt(hex.slice(1), 16);
  // Extract the red (R) component from the decimal representation of a hexadecimal or value. Here's a breakdown of how it works.
  // The >> operator performs a bitwise right shift. Shifting 16 bits to the right moves the red component (the first eight digits) into the last 8-bit position.
  // The & operator masks all bits except the last 8 bits. This ensures that we only keep the red component and discard anything else (if present)
  const r = (bigint >> 16) & 255;
  const g = (bigint >> 8) & 255;
  const b = bigint & 255;

  const return_color = {
    rVal: r,
    gVal: g,
    bVal: b,
    colorStr: `RGB: (${r}, ${g}, ${b})`,
  };
  return return_color;
}

// Define a function called when onClick of the converted button.
function oppositeColor() {
  // Convert first the hexadecimal colo of the color picker to the r,g and b value.
  console.log("Here you are");

  const originalColor = hexToRgb(colorPicker.value);
  const rNew = Math.abs(originalColor.rVal - 255);
  const gNew = Math.abs(originalColor.gVal - 255);
  const bNew = Math.abs(originalColor.bVal - 255);
  const oppositeColor = `rgb(${rNew}, ${gNew}, ${bNew})`;
  // Assign the rgb color to the colorPickerOpposite <div>.
  colorPickerOpposite.style.backgroundColor = oppositeColor;
  colorDisplayOpposite.textContent = `RGB: (${rNew}, ${gNew}, ${bNew})`;
}

// Add the event listener to update the <p> tag
// Add an event listener to the colorPicker element.
// - Event type "input": This event fires whenever the value of the color picker changes, either by user interaction or programmatically.
// Handler function: The code inside the arrow function () => {...} will execute whenever the "input" event is triggered.
colorPicker.addEventListener("input", () => {
  // Retrieves the current value of the color picker element. This value is in hexadecimal format. And call the function for converting it to r,g and b values.
  const rgbValue = hexToRgb(colorPicker.value);
  oppositeColor();
  // Updates the textContent of the colorDisplay element to show the RGB value.
  colorDisplay.textContent = rgbValue.colorStr;
});
