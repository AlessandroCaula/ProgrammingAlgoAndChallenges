// Creating an empty 2D matrix.
function make2DArray(rows, cols) {
  let arr = new Array(rows);
  for (let r = 0; r < arr.length; r++) {
    arr[r] = new Array(cols);
    // Initialize the matrix with 0s.
    for (let c = 0; c < arr[r].length; c++) {
      arr[r][c] = 0;
    }
  }
  return arr;
}

let grid;
// Establis the width/height of each cells in the matrix.
let cell_dimension = 10;
let cols, rows;

// Setup function.
function setup() {
  // Create the canvas. 
  // The Canvas in Web Development refers to the <canvas> HTML element, which provides a drawing surface for rendering graphics, shapes, animations, and even game visuals directly on a webpage. 
  createCanvas(400, 400); // To autosize to the dimension of the current browser width use createCanvas(windowWidth, windowHeight).

  // Setting the frameRate. By default is set to 60 fps.
  frameRate(20);

  // The number of rows and cols is equal to the total canvas width divided by the dimension of a cell.
  cols = width / cell_dimension;
  rows = height / cell_dimension;

  // !! In graphics or game grids (i.e. p5.js) coordinates are often specified as (x, y) which corresponds to column (x) and row (y).

  // Initialize the dimensions of the grid, by calling the make2DArray function. 
  grid = make2DArray(rows, cols);
  // // Initialize the grid matrix with 0s. Loop 
  // for (let r = 0; r < grid.length; r++) {
  //   for (let c = 0; c < grid[r].length; c++) {
  //     grid[r][c] = 0;
  //   }
  // }
  // TEST coloring one cell. Column 20, row 10
  grid[10][20] = 1;
  grid[25][20] = 1;
}


// Add some mouse interaction. When I click with the mouse, I add a grain of sand. 
// // !! The mousePressed() funciton in p5.js is an event handling function that gets called whenever a mouse button is pressed.
// function mousePressed() {
//   // Retrieve the row and col index, where tha mouse has clicked. 
//   let row = floor(mouseY / cell_dimension);
//   let col = floor(mouseX / cell_dimension);
//   grid[row][col] = 1;
// }
// // mouseDragegd() function is a built-in function that gets called continuously while the mouse is pressed and moved. 
// function mouseDragged() {
//   // Retrieve the row and col index, where tha mouse has clicked. 
//   let row = floor(mouseY / cell_dimension);
//   let col = floor(mouseX / cell_dimension);
//   grid[row][col] = 1;
// }


// !! Draw function. It serves as the main rendering loop. It continuously executes the code inside it, allowing you to create animations, update visuals, or interact dynamically with the canvas. 
// - The draw() function runs repeatedly after the setup() function is called. 
//- By default, it executes 60 times per seconds (60 frames per seconds), but this can be adjusted using the frameRate() function. Define the frameRate in the setup() function. 
// - Whatever is drawn or modified inside the draw() function gets updaed on the canves every frame. 
// KEY FEATURES of draw()
// - The function runs in a loop after setup().
// - Use noLoop() to stop the draw() loop if you don't need continuous updates. Call loop() to restart it. 
function draw() {
  // Black background. Clearing the Canva at the start of each frame. Omitting background() will cause shapes to overlap, creating a "trailing" effect. 
  background(0);

  // // Check if the mouse is press, this is checked every frame. If it is, then set the cell with 1. 
  // if (mouseIsPressed) {
  //   // Retrieve the row and col index, where tha mouse has clicked. 
  //   let row = floor(mouseY / cell_dimension);
  //   let col = floor(mouseX / cell_dimension);
  //   grid[row][col] = 1;
  // }

  // Change the color of the cell based on its value.
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      // Sets the color used to draw lines and borders around shapes.
      stroke(255);
      // If the value is 0, by multiplying it by 255 it will still be 0 (black). Otherwise, if it is 1, the value will be 255 (white)
      fill(grid[r][c] * 255);
      // The x position will be the column time the width of that square.
      let x = c * cell_dimension;
      let y = r * cell_dimension;
      // Paint the rectangular square.
      square(x, y, cell_dimension);
    }
  }

  // The next grid, the next frame of this falling sand simulation. 
  let nextGrid = make2DArray(rows, cols);
  // Fill the nextGrid of the frame rate. With the falling sand. 
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      // Get the state of the current cell we are looking at.
      let state = grid[r][c];
      // If the state is 1, I need to look the cell below and check what there is. If it is empty, we let the white cell to "fell" down.
      // If there is already a 1. We let the current cell to stay there.
      if (state === 1) {
        // If the cell is at the last row OR the cell below this current one has a 1. Then the current cell will be in the same position also in the nextGrid.
        if (r === rows - 1 || grid[r + 1][c] === 1) {
          nextGrid[r][c] = 1;
        } else {
          // Let the cell drop down one cell in the other cases. (free fall)
          nextGrid[r + 1][c] = 1;
        }
      }
    }
  }
  // Now the grid is the nextGrid.
  grid = nextGrid;
}
