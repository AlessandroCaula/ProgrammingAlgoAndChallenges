// Tic Tac Toe Board
let board = [
  ["", "", ""],
  ["", "", ""],
  ["", "", ""],
]

// Define the number of rows and columns
let w   // = width / 3
let h   // = height / 3

// Players
let ai = 'X' // the computer
let human = 'O' // The human
let currentPlayer = human;

let available = []

// --- SETUP
// 
function setup() {
  createCanvas(400, 400);
  // Change the frame rate
  frameRate(5);

  // // Randomize the initial player 
  currentPlayer = human
}

// Define the function that will be used to check diagonal equality
function equals3(a, b, c) {
  // Return true if they are all equal
  return (a === b && b === c && a != '')
}

// Check of we have a winner
function checkWinner() {
  let winner = null

  // Check if there are 3 of the same symbols horizontally 
  for (let i = 0; i < 3; i++) {
    if (equals3(board[i][0], board[i][1], board[i][2])) {
      winner = board[i][0]
    }
  }

  // Check if there are 3 of the same symbols vertically
  for (let j = 0; j < 3; j++) {
    if (equals3(board[0][j], board[1][j], board[2][j])) {
      winner = board[0][j]
    }
  }

  // Check diagonals
  if (equals3(board[0][0], board[1][1], board[2][2])) {
    winner = board[0][0]
  }
  if (equals3(board[0][2], board[1][1], board[2][0])) {
    winner = board[0][2]
  }

  let openSpots = 0
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      if (board[r][c] === '') {
        openSpots++
      }
    }
  }

  // If there is no winner and there are no available cells
  if (winner === null && openSpots === 0) {
    return 'tie'
  } else {
    return winner
  }
}

// Mouse click for the interaction with the user
function mousePressed() {
  if (currentPlayer == human) {
    // Human make the turn. Find the cell coordinate based on where the human clicked with the mouse 
    const c = floor(mouseX / w)
    const r = floor(mouseY / h)
    // Check if there is nothing yet in the selected cell
    if (board[r][c] == '') {
      board[r][c] = human
      // Change the player back to the machine
      currentPlayer = ai
      // nextTurn()
      bestMove()
    }
  }
}

// --- DRAW
// 
function draw() {
  background(255);

  // Increase the width of the line
  strokeWeight(4)
  // Define the width and height of each single cell
  w = width / 3
  h = height / 3
  // Draw the lines dividing the cells
  line(w, 0, w, height)
  line(w*2, 0, w*2, height)
  line(0, h, width, h)
  line(0, h*2, width, h*2)

  // Draw the board
  for (let r = 0; r < 3; r++) {
    for (let c = 0; c < 3; c++) {
      // x coordinate centered in the cell
      const x = w * c + w/2
      // y coordinate centered in the cell
      const y = h * r + h/2
      // Retrieve what's the symbol in the current cell
      const spot = board[r][c]
      // If in the cell there is a "O"
      if (spot === human) {
        // Draw a circle
        noFill()
        ellipse(x, y, w/2)
      } else if (spot === ai) {
        // Otherwise draw the X symbol
        const xr = w/4    // Length of half the line
        line(x - xr, y - xr, x + xr, y + xr)
        line(x - xr, y + xr, x + xr, y - xr)
      }
    }
  }

  // Check for the winner
  const result = checkWinner()
  // If there is a winner
  if (result !== null) {
    // Stop the loop 
    noLoop()
    // Text to print
    let resultP = createP('')
    resultP.style('font-size', '32pt')
    if (result === 'tie') {
      resultP.html("Tie!")
    } else {
      resultP.html(`${result} wins!`)
    }
  }
}
