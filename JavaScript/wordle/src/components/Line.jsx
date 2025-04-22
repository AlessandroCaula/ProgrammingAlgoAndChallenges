export const Line = ({ guess }) => {
  // Create a tile, one for each character of the guess. The guess words are of 5 letters. 
  console.log(guess)
  
  const tiles = guess ?  guess.split() : Array(5).fill(' ')
  return (
    <div className="line">
      {/* For each of the index in the tiles array, return a tile box */}
      {
        tiles.map((c, i) => (
          <div key={i} className="tile">
            
          </div>
        ))
      }
    </div>
  )
}