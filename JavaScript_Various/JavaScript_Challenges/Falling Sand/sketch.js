// Initialize the grid, that will be the 2D matrix.
let grid;
// Initialize the velocity grid. It is parallele to the grid matrix, each cell stores the velocity of the corresponding particle.
// Tracks how fast the particle in each cell is moving downward.
let velocityGrid;
// The gravity represents the rate of acceleration due to gravity applied to each particle. 
// It is added to the velocity of each particle in every frame, simulating the continuous downward pull.
let gravity = 0.1;
// Establis the width/height of each cells in the matrix.
let cellDimension = 3;
let cols, rows;
// Defining the "color type", represented as a degree on a color wheel. Value range: 0-360 (corresponding to red, orange, yellow, green, blue and back to red)
let hueValue = 200;

// Creating an empty 2D matrix.
function make2DArray(rows, cols) {
  let arr = new Array(rows);
  for (let r = 0; r < rows; r++) {
    arr[r] = new Array(cols);
    // Initialize the matrix with 0s.
    for (let c = 0; c < cols; c++) {
      arr[r][c] = 0;
    }
  }
  return arr;
}

// Setup function.
function setup() {
  // Create the canvas. 
  // The Canvas in Web Development refers to the <canvas> HTML element, which provides a drawing surface for rendering graphics, shapes, animations, and even game visuals directly on a webpage. 
  // To autosize to the dimension of the current browser width use createCanvas(windowWidth, windowHeight).
  createCanvas(600, 400);

  // Setting the frameRate. By default is set to 60 fps.
  frameRate(60);

  // The colorMode() function in p5.js sets the color mode for the project, defining how colors are interpreted. 
  // When using colorMode(HSB, 360, 255, 255), you are changing the color interpretation to HSB (Hue, Saturation, Brightness).
  // - H (Hue): The "color type", represented as a degree on a color wheel. Value range from 0 to 360 corresponding to red, orange, yellow, green, blue, and back to red. 
  colorMode(HSB, 360, 255, 255);

  // The number of rows and cols is equal to the total canvas width divided by the dimension of a cell.
  cols = floor(width / cellDimension);
  rows = floor(height / cellDimension);

  // Initialize the dimensions of the grid, by calling the make2DArray function. 
  grid = make2DArray(rows, cols);
  // Initialize the velocity Grid with the same dimension of the original grid. In here I will put the value of the velocity
  velocityGrid = make2DArray(rows, cols);
}

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

  // Check if the mouse is press, this is checked every frame. If it is, then set the cell with 1. 
  if (mouseIsPressed) {
    drawSand();
  }

  // Check every cell. Change the color of the cell based on its value.
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      //// Sets the color used to draw lines and borders around shapes.
      // stroke(255);
      // Disables drawing the stroke (outline)
      noStroke();
      // If the value is 0, by multiplying it by 255 it will still be 0 (black). Otherwise, if it is 1, the value will be 255 (white)
      // If the value is not black (is not 0), fill the sand square. 
      if (grid[r][c] > 0) {
        fill(grid[r][c], 255, 255);
        // The x position will be the column time the width of that square.
        let x = c * cellDimension;
        let y = r * cellDimension;
        // Paint the rectangular square.
        square(x, y, cellDimension);
      }
    }
  }

  // The next grid and velocity grid, the next frame of this falling sand simulation. 
  let nextGrid = make2DArray(rows, cols);
  let nextVelocityGrid = make2DArray(rows, cols);
  // Fill the nextGrid of the frame rate. With the falling sand. 
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      // Get the state of the current cell we are looking at.
      let state = grid[r][c];
      // Retrieve the velocity of the current cell from the velocityGrid. 
      let velocity = velocityGrid[r][c];
      let moved = false;  // Tracks if the particle has moved. 
      // If the state is 1, I need to look the cell below and check what there is. If it is empty, we let the white cell to "fell" down.
      // If there is a particle of sand, then the value of the cell is higher than 0. We check if there is space available on the bottom-left or bottom-righ space.
      if (state > 0) { // Only process cells containing a particle. 

        let newPos = min(int(r + velocity), rows - 1); // Calculate the particle's potential new position, by adding it's velocity value, which increase the more the particle is falling. Preventing to exceeds the last row.

        // Iterate from the potential new position back to the current position. 
        // The newPos represents the lowest position the particle might reach in the current frame based on its velocity. 
        // 1 reason: Instead of moving the particle directly to newPos (which might skip over intermediate positions), the loop check each row from newPos to r (in reverse).
        // 2 reason: Granular behaviour. Sand particles fall "cell by cell" (row by row). This allows the simulation to behave like sand, rather than releporting particles to theri final position.
        // 3 reason: HAndling multiple particles. This ensures no particles overlap or "pass through" others. 
        for (let y = newPos; y > r; y--) {
          let below = grid[y][c]; // Check the cell directly below. 

          // If the cell below is empty. Then let the particle move to it.
          if (below == 0) {
            nextGrid[y][c] = state;
            nextVelocityGrid[y][c] = velocity + gravity; // Increase velocity due to gravity. 
            moved = true;
            break; // Exit the loop once the particle has moved. 
          }
          // Check left left and/or rigth cells are available.
          else {
            let isLeftAvailable = (isWithinCols(c - 1) && grid[y][c - 1] === 0); // Check if the cell to the left is within the columns boundaries and if there are no other particles in that cell.
            let isRightAvailable = (isWithinCols(c + 1) && grid[y][c + 1] === 0);
            // If they are both available then randomly choose where the particle should go, if to the left or to the rigth. 
            if (isLeftAvailable && isRightAvailable) {
              let rd = random(1); // Randomize a number between 0 and 1. 
              isLeftAvailable = rd < 0.5 ? true : false; // If it is lower than 0.5, then let the particle go to the left. 
              isRightAvailable = rd > 0.5 ? true : false; // If the random number is higher than 0.5, then let the particle go to the right. 
            }

            // Move the particle diagonlly if there are empty cells. 
            if (isLeftAvailable) {
              nextGrid[y][c - 1] = state;
              nextVelocityGrid[y][c - 1] = velocity + gravity;
              moved = true;
              break;
            } else if (isRightAvailable) {
              nextGrid[y][c + 1] = state;
              nextVelocityGrid[y][c + 1] = velocity + gravity;
              moved = true;
              break;
            }
          }
        }
        
        // If the particle didn't move and it is a the bottom row, stop velocity.
        if (r === rows - 1) {
          nextGrid[r][c] = state;
          nextVelocityGrid[r][c] = 0; // Stop movement. 
        } else if (!moved) {
          // Otherwise, keep it in the same position and continue applying gravity. 
          nextGrid[r][c] = grid[r][c];
          nextVelocityGrid[r][c] = velocityGrid[r][c] + gravity;
        }
      }
    }
  }
  // Update the grid and velocity grid for the next frames. 
  grid = nextGrid;
  velocityGrid = nextVelocityGrid;
}

// Function that checks whether the current cell is within the boundaries of the rows in the grid. 
function isWithinRows(row) {
  return row >= 0 && row <= rows - 1;
}
// Function that checks whether the current cell is within the boundaries of the cols in the grid
function isWithinCols(col) {
  return col >= 0 && col <= cols - 1;
}

function drawSand() {
  // Retrieve the row and col index, where tha mouse has clicked. 
  let clicked_row = floor(mouseY / cellDimension);
  let clicked_col = floor(mouseX / cellDimension);

  // Randomly add an area of sand paricles.
  // A 5 by 5 matrix around the center clicked cell. 
  let matrix = 6;
  let extend = floor(matrix / 2);
  // Loop through the cells aroud the central one and randomly set it to 0 or 1. 
  for (let r = -extend; r < extend; r++) {
    for (let c = -extend; c < extend; c++) {
      // Randomize a number, if it is lower than 0.75 set it to white (75% change of having a white cell)
      if (random(1) < 0.75) {
        let row_in_grid = clicked_row + r;
        let col_in_grid = clicked_col + c;
        // Check if the current cell (row, col) is within the boundaries of the grid. 
        if (isWithinRows(row_in_grid) && isWithinCols(col_in_grid)) {
          // If it is, then assign it the hue color. 
          grid[row_in_grid][col_in_grid] = hueValue;
          // When a particle is created (on mouse move), its initial value is set to 1.
          velocityGrid[row_in_grid][col_in_grid] = 1;
        }
      }
    }
  }
  // Change the hueColor of the sand cells. 
  hueValue += 1;
  if (hueValue > 360) {
    hueValue = 1;
  }
}



/////////////////////
// WITHOUT GRAVITY //
/////////////////////

// // Initialize the grid, that will be the 2D matrix.
// let grid;
// // Establis the width/height of each cells in the matrix.
// let cellDimension = 3;
// let cols, rows;
// // Defining the "color type", represented as a degree on a color wheel. Value range: 0-360 (corresponding to red, orange, yellow, green, blue and back to red)
// let hueValue = 200;

// // Creating an empty 2D matrix.
// function make2DArray(rows, cols) {
//   let arr = new Array(rows);
//   for (let r = 0; r < rows; r++) {
//     arr[r] = new Array(cols);
//     // Initialize the matrix with 0s.
//     for (let c = 0; c < cols; c++) {
//       arr[r][c] = 0;
//     }
//   }
//   return arr;
// }

// // Setup function.
// function setup() {
//   // Create the canvas.
//   // The Canvas in Web Development refers to the <canvas> HTML element, which provides a drawing surface for rendering graphics, shapes, animations, and even game visuals directly on a webpage.
//   // To autosize to the dimension of the current browser width use createCanvas(windowWidth, windowHeight).
//   createCanvas(600, 400);

//   // Setting the frameRate. By default is set to 60 fps.
//   frameRate(60);

//   // The colorMode() function in p5.js sets the color mode for the project, defining how colors are interpreted.
//   // When using colorMode(HSB, 360, 255, 255), you are changing the color interpretation to HSB (Hue, Saturation, Brightness).
//   // - H (Hue): The "color type", represented as a degree on a color wheel. Value range from 0 to 360 corresponding to red, orange, yellow, green, blue, and back to red.
//   colorMode(HSB, 360, 255, 255);

//   // The number of rows and cols is equal to the total canvas width divided by the dimension of a cell.
//   cols = floor(width / cellDimension);
//   rows = floor(height / cellDimension);

//   // Initialize the dimensions of the grid, by calling the make2DArray function.
//   grid = make2DArray(rows, cols);
// }

// // !! Draw function. It serves as the main rendering loop. It continuously executes the code inside it, allowing you to create animations, update visuals, or interact dynamically with the canvas.
// // - The draw() function runs repeatedly after the setup() function is called.
// //- By default, it executes 60 times per seconds (60 frames per seconds), but this can be adjusted using the frameRate() function. Define the frameRate in the setup() function.
// // - Whatever is drawn or modified inside the draw() function gets updaed on the canves every frame.
// // KEY FEATURES of draw()
// // - The function runs in a loop after setup().
// // - Use noLoop() to stop the draw() loop if you don't need continuous updates. Call loop() to restart it.
// function draw() {
//   // Black background. Clearing the Canva at the start of each frame. Omitting background() will cause shapes to overlap, creating a "trailing" effect.
//   background(0);

//   // Check if the mouse is press, this is checked every frame. If it is, then set the cell with 1.
//   if (mouseIsPressed) {
//     drawSand();
//   }

//   // Change the color of the cell based on its value.
//   for (let r = 0; r < rows; r++) {
//     for (let c = 0; c < cols; c++) {
//       //// Sets the color used to draw lines and borders around shapes.
//       // stroke(255);
//       // Disables drawing the stroke (outline)
//       noStroke();
//       // If the value is 0, by multiplying it by 255 it will still be 0 (black). Otherwise, if it is 1, the value will be 255 (white)
//       // If the value is not black (is not 0), fill the sand square.
//       if (grid[r][c] > 0) {
//         fill(grid[r][c], 255, 255);
//         // The x position will be the column time the width of that square.
//         let x = c * cellDimension;
//         let y = r * cellDimension;
//         // Paint the rectangular square.
//         square(x, y, cellDimension);
//       }
//     }
//   }

//   // The next grid, the next frame of this falling sand simulation.
//   let nextGrid = make2DArray(rows, cols);
//   // Fill the nextGrid of the frame rate. With the falling sand.
//   for (let r = 0; r < rows; r++) {
//     for (let c = 0; c < cols; c++) {
//       // Get the state of the current cell we are looking at.
//       let state = grid[r][c];
//       // If the state is 1, I need to look the cell below and check what there is. If it is empty, we let the white cell to "fell" down.
//       // If there is already a 1. We check if there is space available on the bottom-left or bottom-righ space.
//       if (state > 0) {

//         // // If the cell is at the last row OR the cell below this current one has a 1. Then the current cell will be in the same position also in the nextGrid.
//         // if (r === rows - 1 || grid[r + 1][c] > 0) {
//         //   nextGrid[r][c] = state;
//         // } else {
//         //   // Let the cell drop down one cell in the other cases. (free fall)
//         //   nextGrid[r + 1][c] = state;
//         // }

//         // Check the grain of sand (cell) is at the bottom of the grid. In that case just let it stay there.
//         if (r === rows - 1) {
//           nextGrid[r][c] = state;

//         } else if (grid[r + 1][c] > 0) {
//           // If the grig below has another grain of sand, check if there is space on the left or rigth position.
//           isBelowLeftAvailable = (isWithinCols(grid[r + 1][c - 1]) && grid[r + 1][c - 1] === 0);
//           isBelowRightAvailable = (isWithinCols(grid[r + 1][c + 1]) && grid[r + 1][c + 1] === 0);

//           // If both (below-right and left) spaces are available, randomize where to let it drop.
//           if (isBelowLeftAvailable && isBelowRightAvailable) {
//             let randomLeftOrRight = random(1);
//             // if randomLeftOrRight is less than 0.5 then we will let it drop to the left. Otherwise to the rigth.
//             if (randomLeftOrRight < 0.5) {
//               // Set isBelowRightAvailable to false
//               isBelowRightAvailable = false;
//             } else {
//               // Set isBelowLeftAvailable to false
//               isBelowLeftAvailable = false;
//             }
//           }

//           // At this point, only one or none of the beolow right and left cells are available.
//           if (isBelowLeftAvailable) {               // If left is available, place it to the left.
//             nextGrid[r + 1][c -1] = state;
//           } else if (isBelowRightAvailable) {       // If right is available, place it to the left.
//             nextGrid[r + 1][c + 1] = state;
//           } else {                                  // If none of the bottom right or left cells are available, the grain of sand will stai still.
//             nextGrid[r][c] = state;
//           }

//         } else {
//           // It there simply is space in the cell just below, let the grain of sand, to go down.
//           nextGrid[r + 1][c] = state;
//         }
//       }
//     }
//   }
//   // Now the grid is the nextGrid.
//   grid = nextGrid;
// }

// // Function that checks whether the current cell is within the boundaries of the rows in the grid.
// function isWithinRows(row) {
//   return row >= 0 && row <= rows - 1;
// }
// // Function that checks whether the current cell is within the boundaries of the cols in the grid
// function isWithinCols(col) {
//   return col >= 0 && col <= cols - 1;
// }

// function drawSand() {
//   // Retrieve the row and col index, where tha mouse has clicked.
//   let clicked_row = floor(mouseY / cellDimension);
//   let clicked_col = floor(mouseX / cellDimension);

//   // Randomly add an area of sand paricles.
//   // A 5 by 5 matrix around the center clicked cell.
//   let matrix = 6;
//   let extend = floor(matrix / 2);
//   // Loop through the cells aroud the central one and randomly set it to 0 or 1.
//   for (let r = -extend; r < extend; r++) {
//     for (let c = -extend; c < extend; c++) {
//       // Randomize a number, if it is lower than 0.75 set it to white (75% change of having a white cell)
//       if (random(1) < 0.75) {
//         let row_in_grid = clicked_row + r;
//         let col_in_grid = clicked_col + c;
//         // Check if the current cell (row, col) is within the boundaries of the grid.
//         if (isWithinRows(row_in_grid) && isWithinCols(col_in_grid)) {
//           // If it is, then assign it the hue color.
//           grid[row_in_grid][col_in_grid] = hueValue;
//         }
//       }
//     }
//   }
//   // Change the hueColor of the sand cells.
//   hueValue += 1;
//   if (hueValue > 360) {
//     hueValue = 1;
//   }
// }