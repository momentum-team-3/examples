// Global constants
const DBURL = "http://localhost:3000/notes"
const createNoteSection = document.querySelector("#create-note-section")
const viewNotesSection = document.querySelector("#view-notes-section")


// Miscellaneous helper functions
const makeVisible = element => element.classList.remove("hidden")
const makeHidden = element => element.classList.add("hidden")
const select = selector => document.querySelector(selector)
const selectAll = selector => document.querySelectAll(selector)
const noteURL = id => DBURL + `/${id}`
const statusOK = status => status > 199 && status < 300


// Helpers for piecing together the notes
function makeInputField(label, field, value, id) {
    let elementId = field + "-" + id
    let labelElement = `<label for=${elementId}>${label}</label>`
    let inputArea = `<textarea id=${elementId} disabled>${value}</textarea>`
    return labelElement + inputArea
}

function makeEditButton(id) {
    return `<button class="edit-button" onclick="editNote(${id})">edit</button>`
}

function makeEditSubmitButton(id) {
    return `<button class="submit-edits-button" onclick="commitNoteChanges(${id})">save</button>`
}

function makeCancelButton(id) {
    return `<button class="cancel-edits-button" onclick="displayNote(${id})">cancel</button>`
}

function makeDeleteButton(id) {
    return `<button class="delete-button" onclick="deleteNote(${id})">delete</button>`
}

// Event handlers for edit, commit edit, and delete
function editNote(id) {
    let note = select(`#note-${id}`)
    note.classList.remove("display-mode")
    note.classList.add("edit-mode")
    select(`#title-${id}`).removeAttribute("disabled")
    select(`#body-${id}`).removeAttribute("disabled") 
}

function displayNote(id) {
   let note = select(`#note-${id}`)
    note.classList.remove("edit-mode")
    note.classList.add("display-mode")
    select(`#title-${id}`).setAttribute("disabled", true)
    select(`#body-${id}`).setAttribute("disabled", true)
}

function commitNoteChanges(id) {
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

// Produce a new section containing a note
function makeNote(title, body, id) {
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

function getShowNotes() {
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
	        let newNode = makeNote(title, body, id)
            contentHook.appendChild(newNode)
        }})
}

function addNote () {
    let noteTitle = select("#create-note-title")
    let noteBody = select("#create-note-body")
    let request = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ "title": noteTitle.value, "body": noteBody.value })
    }

    fetch(DBURL, request)
    .then(response => {
        if (statusOK(response.status)) {
	        alert("Note added to database.")
	        noteTitle.value = ""
	        noteBody.value = ""
        } else { 
            alert("A calamitous problem occured.")
        }})
    }

// Setup the application
function addAllEventListeners() {
    select("#create-note-nav-button").addEventListener("click", showCreateNote)
    select("#view-notes-nav-button").addEventListener("click", showViewNotes)
}

addAllEventListeners()
getShowNotes()
