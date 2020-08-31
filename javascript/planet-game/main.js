
// Global constants and variables
// The document's canvas element
const canv = document.querySelector("#canvas")
// small helper for getting a new context
const getctx = () => canv.getContext("2d")
const width = canv.width
const height = canv.height
var playerAlive = true
var baseSpawnChance = 0.0005
var baseSpawnChanceGrowthFactor = 1.005
var mainLoopID

// variables for initializing new planets
const playerVelocity = [3, 3]
const baseImageSize = 48
const planetImages = [new Image(), new Image(), new Image(), new Image(), new Image(), new Image()]
const planetNames = ["Baren", "Desert", "Forest", "Ice", "Lava", "Ocean"]
planetImages.forEach((p, i) => p.src = `assets/${planetNames[i]}.png`)
const earthImage = new Image() 
earthImage.src = "assets/Terran.png"
const lavaImage = planetImages[4]
// This object records which keys are currently being pressed
const keyPressedState = {
  37: false,
  38: false,
  39: false,
  40: false
}

// Records the change in x and coordinates mapped to each key
const keyDV = {
  37: [-1, 0],
  39: [1, 0],
  38: [0, -1],
  40: [0, 1]
}

// The global table of planets and planet spawning variables
const GameState = {
  planets: [],
  numPlanets: 0,
  maxPlanets: 20,
  spawnChance: baseSpawnChance,
}

function randomPlanetImage () {
  return randomElement(images)
}

// Functions for constructing new planets
function makePlanet (x, y, velocity, scale, image, type) {
  let Planet = {
    x: x,
    y: y,
    scale: scale,
    image: image,
    velocity: velocity,
    type: type,
    vx: () => Planet.velocity[0],
    vy: () => Planet.velocity[1],
    radius: () => Math.floor(Planet.scale / 2)
  }

  return Planet
}

// Create a player controlled planet
function makeEarth (x,y) {
  let Earth = makePlanet(
    x,
    y,
    playerVelocity,
    baseImageSize * 2,
    earthImage,
    "earth")
    Earth.numLives = 5

    return Earth
}

function randomAlienPlanet () {
  // Variables to hold the parameters for the new planet
  let x, y, velocity, scale, image

  // Generate position, scale, and image
  scale = random(1, 3) * baseImageSize
  x = random(0, width - scale)
  y = random(0, height - scale)
  image = randomElement(planetImages)

  // Randomly generate velocity vectors until a
  // a non-zero velocity vector is generated
  // (ensure the planet isn't stationary)
  // more often than not, this loop will run only once
  while (true) {
    velocity = randomVector(0, 3, 0, 3)

    // Break if at least one component is non-zero
    if (velocity[0] || velocity[1]) {
      velocity[0] *= randSign()
      velocity[1] *= randSign()
      break
    }
  }

  return makePlanet(x, y, velocity, scale, image, "alien")
}

// predicates for the planet type
function isEarth(p) {
  return p.type === "earth"
}

function isAlienPlanet(p) {
  return p.type === "alien"
}

function planetIndex(p) {
  return GameState.planets.indexOf(p)
}

function addPlanet(p) {
  GameState.planets.push(p)
  GameState.numPlanets++
}

function removePlanet(p) {
  GameState.planets.splice(planetIndex(p), 1)
  GameState.numPlanets--
  return
}

function replacePlanet(p1, p2) {
  GameState.planets[planetIndex(p1)] = p2
}

function resetPlanets() {
  GameState.planets.splice(0)
}

// Get the surface area of this planet (for calculating new entities on collision)
function areaOf (p) {
  return p.scale ** 2
}

// Get the side length of a planet with a given size
function edgeOf (area) {
  return Math.sqrt(area)
}

// Return the midpoint of the p1 and p2
function midpoint (p1, p2) {
  let mx = (p1.x + p2.x) / 2
  let my = (p1.y + p2.y) / 2

  return [mx, my]
}

// Get the coordinates of the center of the planet
function center(p) {
  let mx = p.x + p.radius()
  let my = p.y + p.radius()

  return [mx, my]
}

// Create a new planet by merging the two planet objects
function mergePlanets(p1, p2) {
  let [x, y]  = midpoint(p1, p2)
  let scale = edgeOf(areaOf(p1) + areaOf(p2))
  let velocity = [-(p1.vx()) - p2.vx(), -(p1.vy()) - p2.vy()]
  return makePlanet(x, y, velocity, scale, lavaImage, "alien")
}

function handleCollision (p1, p2) {
  if (isEarth(p1)) {
    playerAlive = --p1.numLives ? true : false
    removePlanet(p2)
  } else if (isEarth(p2)) {
    playerAlive = --p2.numLives ? true : false
    removePlanet(p1)
  } else {
    let combined = mergePlanets(p1, p2)
    replacePlanet(p1, combined)
    removePlanet(p2)
  }

  if (!playerAlive) {
    alert("Game over!")
    window.clearInterval(mainLoopID)
  }
}

// Draw a planet using information about its size, position, and color
function draw(p) {
  if (p) {
    let x, y, scale, image, rest
    ({x, y, scale, image, ...rest} = p)
    let ctx = getctx()
    ctx.drawImage(image, x, y, scale, scale)
  }
}

// Find maximum x/y for a particular planet
function xupper(p) {
  return canv.width - p.scale
}

function yupper(p) {
  return canv.height - p.scale
}

// Find minimum x/y coordinate for a particular planet
function ylower(_) {
  return 0
}

function xlower(_) {
  return 0
}


// Update the planet's position, staying inside the boundaries
// of the canvas. If the planet is a non-player planet and it reaches
// a vertical or horizontal canvas edge, invert its corresponding velocity
// component
function update(p) {
  let dx = 0, dy = 0
  if (isEarth(p)) {
    // If this plaent is a player planet, iterate through the keyState
    // and, for every key that's currently being pressed, get its x and
    // y velocity components
    for (var k in keyState) {
      if (keyState[k]) {
        [dx, dy] = [dx + keyDV[k][0], dy + keyDV[k][1]]
      }
    }

    let nx = p.x + p.vx() * dx
    let ny = p.y + p.vy() * dy

    if (nx < xlower(p)) {
      p.x = xlower(p)
    } else if (nx > xupper(p)) {
      p.x = xupper(p)
    } else {
      p.x = nx
    }

    if (ny < ylower(p)) {
      p.y = ylower(p)
    } else if (ny > yupper(p)) {
      p.y = yupper(p)
    } else {
      p.y = ny
    }

  } else if (isAlienPlanet(p)) {
    [dx, dy] = p.velocity

    let nx = p.x + dx, ny = p.y + dy

    if (nx < xlower(p)) {
      p.x = xlower(p)
      p.velocity[0] = -(p.velocity[0])
    } else if (nx > xupper(p)) {
      p.x = xupper(p)
      p.velocity[0] = -(p.velocity[0])
    } else {
      p.x = nx
    }

    if (ny < ylower(p)) {
      p.y = ylower(p)
      p.velocity[1] = -(p.velocity[1])
    } else if (ny > yupper(p)) {
      p.y = yupper(p)
      p.velocity[1] = -(p.velocity[1])
    } else {
      p.y = ny
    }
  } else {
    throw new Error("No procedure for rendering non-planet entity")
  }
}

// Check whether two planets are colliding, using the collision algorithm
// for circular screen elements. Although the planet images are squares, using the 
// algorithm for circular screen elements prevents distortion of the hitbox at larger
// scales
function checkCollision(p1, p2) { 
  if (p1 && p2) {
    // get the center coordinates of the planets
    let [m1x, m1y] = center(p1)
    let [m2x, m2y] = center(p2)
    let dx = m1x - m2x
    let dy = m1y - m2y
    let distance = Math.hypot(dx, dy)
    let minSafeDistance = p1.radius() + p2.radius()
    return distance <= minSafeDistance
  } else {
    return false
  }
}

/* 
 * Clear the screen, run the update loop, then run the drawing loop
 * 
 */
function refresh () {
  let ctx = getctx()
  ctx.clearRect(0, 0, width, height)
  
  // Begin entities updating loop
  let i = 0
  let GS = GameState

  while (i < GS.numPlanets) {
    if (GS.planets[i]) {
      update(GS.planets[i])
      let j = 0

      while (j < GS.numPlanets) {
        if (i !== j && checkCollision(GS.planets[i], GS.planets[j])) {
          handleCollision(GS.planets[i], GS.planets[j])
          if (!playerAlive) {
            break
          }
        }
        j++
      }
      if (!playerAlive) {
        break
      } else {
        draw(GS.planets[i])
      }
    }
    i++
  }

  if (GS.numPlanets < GS.maxPlanets && Math.random() < GS.spawnChance) {
    addPlanet(randomAlienPlanet())
    GS.spawnChance = baseSpawnChance
  } else {
    GS.spawnChance *= baseSpawnChanceGrowthFactor
  }
}

function runGame () {
  initializePlanets(2)
  mainLoopID = window.setInterval(refresh, 20)
}

// Add a player planet and some randomized non-player planets
function initializePlanets(n) {
  resetPlanets()
  addPlanet(makeEarth(452, 452))
  for (let i = 1; i < n; i++) {
    let p = randomAlienPlanet()
    GameState.planets.push(p)
    numPlanets++
  }
}

window.addEventListener("keydown", e => keyState[e.keyCode] = true)
window.addEventListener("keyup", e => keyState[e.keyCode] = false)