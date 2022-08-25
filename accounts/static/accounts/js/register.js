const ids = [
  "first_name",
  "last_name",
  "email",
  "password1",
  "password2",
  "college",
  "contact",
];

//show hide password
function toggleInputType(elementId) {
  // Select element to toggle input type for
  let inputElement = document.getElementById(elementId)
  console.log({elementId, element: inputElement})
  // Checks if element exists
  if (inputElement == null || inputElement == undefined) {
    alert('something went wrong, contact webmaster');
  }
  // Check if input is either of text/password type
  ['password', 'text'].includes(inputElement.type.toString());
  // Toggle logic
  inputElement.type = inputElement.type === 'password' ? 'text' : 'password';
}



function placePlaceholders() {
  ids.forEach((id) => {
    const element = document.querySelector(`#id_${id}`);
    let placeholder = id.split("_").join(" ").trim()
    if (id === 'password1') {
        placeholder = "password";
    } else if (id === "password2") {
        placeholder = "confirm password";
    }
    element.setAttribute("placeholder", placeholder);
  });
}

window.addEventListener("load", (_) => {
  placePlaceholders();
});
