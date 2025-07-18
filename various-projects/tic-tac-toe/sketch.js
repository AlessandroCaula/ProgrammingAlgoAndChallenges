// Tic Tac Toe Board
let board = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
]

// Players
const player1 = 'X'
const player2 = 'O'

// Play the game
let currentPlayer;


function setup() {
  createCanvas(400, 400);

  // Let's randomly pick a starting player, 1 or 2
  if (random(1) < 0.5) {
    currentPlayer = player1
  } else {
    currentPlayer = player2
  }
}

function draw() {
  background(255);

  // Define the width and height of each single cell
  const w = width / 3
  const h = height / 3
  // Draw the lines dividing the cells
  line(w, 0, w, height)
  line(w*2, 0, w*2, height)
  line(0, h, width, h)
  line(0, h*2, width, h*2)

  // Draw the board
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      // x coordinate centered in the cell
      const x = w * i + w/2
      // y coordinate centered in the cell
      const y = h * j + h/2
      // Retrieve what's the symbol in the current cell
      const spot = board[i][j]
      // Increase the width of the line
      strokeWeight(4)
      // If in the cell there is a "O"
      if (spot === player2) {
        // Draw a circle
        noFill()
        ellipse(x, y, w/2)
      } else if (spot === player1) {
        // Otherwise draw the X symbol
        const xr = w/4    // Length of half the line
        line(x - xr, y - xr, x + xr, y + xr)
        line(x - xr, y + xr, x + xr, y - xr)
      }
    }
  }
}
