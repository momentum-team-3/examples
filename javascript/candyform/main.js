const DBURL = "http://localhost:3000/candies/"


function makeAddCandyVisible () {
    let addCandySection = document.querySelector("#add-candy-section")
    let candySearchSection = document.querySelector("#candy-search-section")
    let browseCandySection = document.querySelector("#browse-candy-section")
    addCandySection.classList.remove("hidden")
    browseCandySection.classList.add("hidden")
    candySearchSection.classList.add("hidden") 
}

function makeCandySearchVisible () {
    let addCandySection = document.querySelector("#add-candy-section")
    let candySearchSection = document.querySelector("#candy-search-section")
    let browseCandySection = document.querySelector("#browse-candy-section")
    addCandySection.classList.add("hidden")
    browseCandySection.classList.add("hidden")
    candySearchSection.classList.remove("hidden")
}

function makeBrowseCandyVisible() {
    let addCandySection = document.querySelector("#add-candy-section")
    let candySearchSection = document.querySelector("#candy-search-section")
    let browseCandySection = document.querySelector("#browse-candy-section")
    addCandySection.classList.add("hidden")
    browseCandySection.classList.remove("hidden")
    candySearchSection.classList.add("hidden")
    makeShowCandies()

}

function makeShowCandies() {
    let browseCandySection = document.querySelector("#browse-candy-section")
    // clear away old content
    browseCandySection.innerHTML = ""
    fetch(DBURL)
    .then(response => response.json())
    .then(candies => {
        for (let candy of candies) {
            let name = candy.name
            let type = candy.type
            let calories = candy.calories
            let newCandyEntry = document.createElement("dl")
            newCandyEntry.classList.add("candy-info")
            newCandyEntry.innerHTML = `<dt>name</dt><dd>${name}</dd><dt>type</dt><dd>${type}</dd><dt>calories</dt><dd>${calories}</dd>`
            browseCandySection.appendChild(newCandyEntry)
        }
    })
}


// Produce a new object representing a candy

/*

    an m&m would look like:
    ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ
    {
        name: "m&ms",
        type: "chocolate",
        calories: 120,
    }

*/


function searchByName(candies, candyName) {
    for (let candy of candies) {
        if (candy.name === candyName) {
            // Add a paragraph element to the dom with
            // information about my candy
            alert("That candy exists!")
            return
        }
    }

    // No match was found
    alert("No match found.")
}

function validateResponse(candies, name, type, calories) {
    console.log(candies)
    for (let candy of candies) {
        if (candy.name === name) {
            alert("A candy with that name already exists in the database.")
            // Exit the handler without doing anything
            return
        }
    }

    // Create the new object to put in the database
    let addCandyRequest = {
       method: "POST",
       headers: {
           "Content-Type": "application/json"
       },
       body: JSON.stringify({                     // our new candy object
           "name": name,
           "type": type,
           "calories": calories,
       })
   }

   fetch(DBURL, addCandyRequest)
   .then(response => {
       let status = response.status
       if (status > 199 && status < 300) {
           alert("Candy added to database.")
       } else {
           alert("Something went wrong D:")
       }
   })
}

// Event handler for forms
function addCandy (event) {
    // Prevent request of new url
    event.preventDefault()

    /*

        What does a dom object actually look like?

               ¯\_(⊙_ʖ⊙)_/¯
        {
            tag: "form",
            id: "candy-form",
            parent: "main",
            children: [<zero or more javaScript Objects>],
            ...
        }

    */

    // Get the fields the user submitted
    let candyName = document.querySelector("#candy-name")
    let candyType = document.querySelector("#candy-type")
    let candyCalories = document.querySelector("#candy-calories")
    // Get their values (convert to appropriate type if necessary)
    let candyNameValue = candyName.value
    let candyTypeValue = candyType.value
    let candyCaloriesValue = Number(candyCalories.value)

    // Use fetch to get an array of all values in the database and pass that array,
    // as well as the processed form values, to the validateResponse handler
    fetch(DBURL)
    .then(response => response.json())
    .then(data => validateResponse(data, candyNameValue, candyTypeValue, candyCaloriesValue))
}

let theForm = document.querySelector("#candy-form")
if (theForm !== null) {
    theForm.addEventListener("submit", addCandy)
}

let searchForm = document.querySelector("#candy-search-form")
if (searchForm !== null) {
searchForm.addEventListener("submit", searchSubmit)
}

function searchSubmit (event) {
    event.preventDefault();

    let candySearched = document.querySelector("#search-candy-name")
    let candySearchedValue = candySearched.value
    let request = {
        method: "GET"
    }

    fetch(DBURL, request)
    .then(response => response.json())
    .then(data => searchByName(data, candySearchedValue))

}

let addCandyNav = document.querySelector("#add-candy-nav-button")
addCandyNav.addEventListener("click", makeAddCandyVisible)

let searchCandyNav = document.querySelector("#search-candy-nav-button")
searchCandyNav.addEventListener("click", makeCandySearchVisible)

let browseCandyNav = document.querySelector("#browse-candy-nav-button")
browseCandyNav.addEventListener("click", makeBrowseCandyVisible)