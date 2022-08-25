const ids = [
  "first_name",
  "last_name",
  "email",
  "password1",
  "password2",
  "college",
  "contact",
];

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
