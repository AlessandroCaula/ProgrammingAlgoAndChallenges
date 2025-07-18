export const Line = ({ guess, solution }) => {
  // Create a tile, one for each character of the guess. The guess words are of 5 letters.   
  const tiles = guess ? guess.split('') : Array(5).fill(' ')

  return (
    <div className="line">
      {/* For each of the index in the tiles array, return a tile box */}
      {tiles.map((c, i) => {
        // Determine the color of the tile based on the presence or not of the letter
        const color = 
          solution[i] === c 
          ? "correct"
          : solution.includes(c) 
          ? "present"
          : ""
        return (
          <div key={i} className={`tile ${color}`}>
            {c}
          </div>
        )
      })}
    </div >
  )
}