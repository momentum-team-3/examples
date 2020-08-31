// Global constants
const DBURL = "http://localhost:3000/notes"
const contentHook = document.querySelector("#content-hook")

// Miscellaneous helper functions
const select = (selector) => document.querySelector(selector)
const selectAll = (selector) => document.querySelectAll(selector)
const noteURL = (id) => DBURL + `/${id}`
const statusOK = (status) => status > 199 && status < 300


// Helpers for piecing together a note from the database
function makeInputField (label, field, value, id) {
    let elementId = field + "-" + id
    let labelElement = `<label for=${elementId}>${label}</label>`
    let inputArea = `<textarea id=${elementId} disabled>${value}</textarea>`
    return labelElement + inputArea
}

function makeEditButton (id) {
    return `<button class="edit-button" onclick="editNote(${id})">edit</button>`
}

function makeEditSubmitButton (id) {
    return `<button class="submit-edits-button" onclick="commitNoteChanges(${id})">save</button>`
}

function makeCancelButton (_) {
    return `<button class="cancel-edits-button" onclick="getShowNotes()">cancel</button>`
}

function makeDeleteButton (id) {
    return `<button class="delete-button" onclick="deleteNote(${id})">delete</button>`
}


// Produce a new section containing a note with content loaded from the database
function makeNote (title, body, id) {
    let output = document.createElement("div")
    output.id = `note-${id}`
    output.classList.add("display-mode")
    output.classList.add("note")
    let noteTitle = makeInputField("note title", "title", title, id)
    let noteBody = makeInputField("note body", "body", body, id)
    let noteEditButton = makeEditButton(id)
    let noteSubmitButton = makeEditSubmitButton(id)
    let noteCancelButton = makeCancelButton(id)
    let noteDeleteButton = makeDeleteButton(id)
    let buttons = noteEditButton  + noteDeleteButton + noteSubmitButton + noteCancelButton    
    output.innerHTML = noteTitle + noteBody + buttons

    return output
}

function makeAddNoteDiv () {
    let output = document.createElement("div")
    output.id = "note-nil"
    output.classList.add("display-mode")
    output.classList.add("note")
    output.innerHTML = "<button onclick='assembleMakeNote(this.parentNode)'></button>"
    return output
}

function assembleMakeNote(node) {
    node.innerHTML = ""
    node.id = "note-0"
    let noteTitle = makeInputField("note title", "title", "", 0)
    let noteBody = makeInputField("note body", "body", "", 0)
    let noteEditButton = makeEditButton(0)
    let noteSubmitButton = makeEditSubmitButton(0)
    let noteCancelButton = makeCancelButton(0)
    let noteDeleteButton = makeDeleteButton(0)
    let buttons = noteEditButton  + noteDeleteButton + noteSubmitButton + noteCancelButton    
    node.innerHTML = noteTitle + noteBody + buttons
    editNote(0)
}


// Event handlers for edit, commit edit, and delete
function editNote (id) {
    let note = select(`#note-${id}`)
    note.classList.remove("display-mode")
    note.classList.add("edit-mode")
    select(`#title-${id}`).removeAttribute("disabled")
    select(`#body-${id}`).removeAttribute("disabled")
}

// Make the displayNotes section visible
function displayNote (id) {
   let note = select(`#note-${id}`)
    note.classList.remove("edit-mode")
    note.classList.add("display-mode")
    select(`#title-${id}`).setAttribute("disabled", true)
    select(`#body-${id}`).setAttribute("disabled", true)
}

// Update the database with whatever changes the user has made to the note
function commitNoteChanges (id) {
    if (id === 0) {
        return addNote()
    }
    let noteTitle = select(`#title-${id}`).value
    let noteBody = select(`#body-${id}`).value
    let request = {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "title": noteTitle, "body": noteBody })
    }

    fetch(noteURL(id), request)
    .then(response => {
    if (statusOK(response.status)) {
        displayNote(id)
        alert("Note changes saved.")
    } else {
        alert("A calamitous problem occured.")
    }})
}

// Remove a note from the database
function deleteNote(id) {

    let check = confirm("Delete this note?")
    if (!check) {
        return
    }

    let request = {
        method: "DELETE"
    }

    fetch(noteURL(id), request)
    .then(response => {
    if (statusOK(response.status)) {
        alert("Note successfully deleted.")
        // refresh the notes view
        getShowNotes()
    } else {
        alert("A calamitous problem occured.")
    }})
}

// Nav menu event handlers
function showCreateNote(event) {
    event.preventDefault()

    createNoteSection.classList.remove("hidden")
    createNoteSection.classList.add("visible")
    viewNotesSection.classList.add("hidden")
    viewNotesSection.classList.remove("visible")
}

function showViewNotes(event) {
    event.preventDefault()

    createNoteSection.classList.add("hidden")
    createNoteSection.classList.remove("visible")
    viewNotesSection.classList.remove("hidden")
    viewNotesSection.classList.add("visible")
    getShowNotes()
}

// Get all of the notes from the database and add them to the document, anchoring them to the content-hook node
function getShowNotes () {
    let contentHook = select("#content-hook")
    contentHook.innerHTML = ""
    fetch(DBURL)
    .then(response => response.json())
    .then( notes => {
        // Iterate through the database entries and render a new note, adding it to the content-hook div
        for (let note of notes) {
            let id = note.id
            let title = note.title
            let body = note.body
            /*
            With string interpolation:

            let newNode = `<div><h3 id="note-${id}">${title}</h3><p>${body}</p></div>`
            contentHook.innerHTML += newNode
            */
            let newNode = makeNote(title, body, id)
            contentHook.appendChild(newNode)
        }
        contentHook.appendChild(makeAddNoteDiv())
    })
}

function addNote () {
    let noteTitle = select("#title-0").value
    let noteBody = select("#body-0").value
    let request = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "title": noteTitle, "body": noteBody })
    }

    fetch(DBURL, request)
    .then(response => {
        if (statusOK(response.status)) {
            alert("Note added to database.")
            getShowNotes()
        } else { 
            alert("A calamitous problem occured.")
        }})
    }
