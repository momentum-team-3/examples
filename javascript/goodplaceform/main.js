/* eslint-disable prefer-const */
let form = document.querySelector('#registration-form')
let formIsValid

form.addEventListener('submit', validate)

function validate (event) {
  event.preventDefault()

  // Think of these two initial steps as clearing everything
  // to give us a "clean slate" to start from
  removeErrorMessage()
  removeValidMessage()

  formIsValid = true

  // here are all the inputs we need to validate
  validateName()
  validateEmail()
  validatePhoneNumber()
  confirmPasswordMatch()
  // TODO: more validation functions here

  // if everything is valid, we want to show a message at the bottom
  showValidMessage()
}

function markFormAsInvalid () {
  formIsValid = false
}

function removeErrorMessage () {
  let errorDiv = document.querySelector('#error-msg')
  if (errorDiv) {
    errorDiv.innerHTML = ''
  }
}

function removeValidMessage () {
  let validMsg = document.querySelector('#valid-message')
  if (validMsg) {
    validMsg.remove()
  }
}

function validateName () {
  // validate presence of name input data
  // need to check if there is a value
  // check if the value has any text
  const nameInput = document.querySelector('#name-input')
  const name = nameInput.value
  const parentEl = nameInput.parentElement

  if (name) {
    // mark this as valid
    // add a class to the div that wraps the form controls
    console.log('Name input is valid') // this console log is not necessary, but using it could be helpful as you work
    parentEl.classList.remove('input-invalid')
    parentEl.classList.add('input-valid')
  } else {
    console.log('Name input is invalid')
    parentEl.classList.remove('input-valid')
    parentEl.classList.add('input-invalid')
    markFormAsInvalid()
  }
}

function validatePhoneNumber() {
  const numberInput = document.querySelector("#phone-input")
  const number = numberInput.value
  const parentEl = numberInput.parentElement
  let numTest = true

  if (numPat.test(number)) {
    parentEl.classList.remove("input-invalid")
    parentEl.classList.add("input-valid")
  } else {
    parentEl.classList.remove("input-valid")
    parentEl.classList.add("input-invalid")
    markFormAsInvalid()
  }
}



function validateEmail () {
  // this is almost identical to the validateName function!
  // we could probably do this same operation with one function, but for now this is fine
  const emailInput = document.querySelector('#email-input')
  const email = emailInput.value
  const parentEl = emailInput.parentElement

  if (email) {
    parentEl.classList.remove('input-invalid')
    parentEl.classList.add('input-valid')
  } else {
    parentEl.classList.remove('input-valid')
    parentEl.classList.add('input-invalid')
    markFormAsInvalid()
  }
}

function confirmPasswordMatch () {
  // grab the password input
  let password = document.querySelector('#password-input')
  // grab the confirm password input
  let confirmPwd = document.querySelector('#confirm-password')

  // compare their values to see if they match
  if (password.value !== confirmPwd.value) {
    // show an error message on the page
    let errorDiv = document.querySelector('#error-msg')
    errorDiv.innerHTML = 'Your passwords must match'
    confirmPwd.parentElement.classList.add('input-invalid')
    markFormAsInvalid()
  } else {
    confirmPwd.parentElement.classList.remove('input-invalid')
    confirmPwd.parentElement.classList.add('input-valid')
  }
}

function showValidMessage () {
  if (formIsValid) {
    const validMsgEl = document.createElement('h2')
    validMsgEl.id = 'valid-message'
    const validMsgText = document.createTextNode('This form is valid!')
    validMsgEl.appendChild(validMsgText)
    document.querySelector('main').appendChild(validMsgEl)
  }
}
