// Tic Tac Toe Board
let board = [
  ["X", "O", "O"],
  ["O", "X", "X"],
  ["O", "X", "O"],
]

// Players
const player1 = 'X'
const player2 = 'O'

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);

  let w = width / 3
  let h = height / 3

  // Draw the board
  for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      // x coordinate centered in the cell
      let x = w * i
      // y coordinate centered in the cell
      let y = h * j
      let spot = board[i][j]
      // Just use the text to draw the board cell ("X" or "O")
      textSize(11)
      text(spot, x, y)
    }
  }
}
