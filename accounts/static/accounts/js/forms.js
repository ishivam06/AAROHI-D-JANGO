// Setting proper placeholder
function setPlaceholders() {
  document.getElementById('id_username').setAttribute('placeholder', 'username');
  document.getElementById('id_password').setAttribute('placeholder', 'password');
}

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

// Set placeholders when content has loaded
window.addEventListener('load', () => {
  setPlaceholders()
  document.getElementById('id_username').value = ''
  document.getElementById('id_password').value = ''
})

function passToggle3() {
  let ip = document.getElementById("id_old_password");

  if (ip.type === "password") {
    ip.type = "text";
  } else {
    ip.type = "password";
  }
}

function passToggle4() {
  let ip = document.getElementById("id_new_password1");

  if (ip.type === "password") {
    ip.type = "text";
  } else {
    ip.type = "password";
  }
}

function passToggle5() {
  let ip = document.getElementById("id_new_password2");

  if (ip.type === "password") {
    ip.type = "text";
  } else {
    ip.type = "password";
  }
}

$(document).ready(function () {
  $("#id_password1").on("input", function () {
    inputtxt = $("#id_password1").val();
    //$('#pass-strength').html("strong");

    var decimal =
      /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,50}$/;
    if (inputtxt.match(decimal)) {
      $("#pass-strength").css("color", "green");
      $("#pass-strength").html("Strong Password");
    } else {
      $("#pass-strength").css("color", "red");
      $("#pass-strength").html("Weak Password");
    }
  });

  $("#id_new_password1").on("input", function () {
    inputtxt = $("#id_new_password1").val();
    //$('#pass-strength').html("strong");

    var decimal =
      /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,50}$/;
    if (inputtxt.match(decimal)) {
      $("#pass-strength").css("color", "green");
      $("#pass-strength").html("Strong Password");
    } else {
      $("#pass-strength").css("color", "red");
      $("#pass-strength").html("Weak Password");
    }
  });
});