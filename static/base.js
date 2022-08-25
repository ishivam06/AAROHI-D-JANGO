const navOpenButton = document.querySelector('#navopen-button');
const navbar = document.querySelector('#navbar');

navOpenButton.addEventListener('click', (e) => {
  openNav();
})


// Getting rid of the preloader once content has loaded
document.addEventListener('loadeddata', (_) => {
  document.querySelector('#preload').style.display = "none";
})

// Replace home sign in and links with icons when on mobile
// The function will handle resize event for the navbar
function navbarResizeHandler() {
  const homelink = document.querySelector('#home-link');
  const signinlink = document.querySelector('#signin-link');
  const signoutlink = document.querySelector('#signout-link');
  const navopenLink = document.querySelector('#nav-open-button');
  if (window.innerWidth < 720) {
    // Replace home text with icon
    homelink.innerHTML = '<i class="fa-solid fa-house"></i>'
    // Sign in and sign out links need to be handled one by one
    // Because these links are generated on the HTML by django
    // We have to check whether the element exists before attempting to style i
    if (signinlink) {
      signinlink.innerHTML = '<i class="fa-solid fa-arrow-right-to-bracket"></i>'
    }
    if (signoutlink) {
      signoutlink.innerHTML = '<i class="fa-solid fa-arrow-right-to-bracket"></i>'
    }
    // Replacing the navopen button inside with an icon
    navopenLink.innerHTML = '<i class="fa-solid fa-ellipsis"></i>';
  } else {
    homelink.innerHTML = 'Home';
    if (signinlink) {
      signinlink.innerHTML = 'Sign In';
    }
    if (signoutlink) {
      signoutlink.innerHTML = 'Sign Out';
    }
    navopenLink.innerHTML = 'Links'
  }
}

window.addEventListener('resize', (_) => {
  navbarResizeHandler();
})

navbarResizeHandler();


/* Open when someone clicks on the span element */
function openNav() {
  document.getElementById("myNav").style.width = "100%";
  $(".nav-overlay-link-left").addClass('slide-left');
  $(".nav-overlay-link-right").addClass('slide-right');

}

/* Close when someone clicks on the "x" symbol inside the overlay */
function closeNav() {
  document.getElementById("myNav").style.width = "0%";
  $(".nav-overlay-link-left").removeClass('slide-left');
  $(".nav-overlay-link-right").removeClass('slide-right');

}


/*
  //loader funcs
const preloader = document.querySelector('.preloader');
const fadeEffect = setInterval(() => {
  // if we don't set opacity 1 in CSS, then
  // it will be equaled to "" -- that's why
  // we check it, and if so, set opacity to 1
  if (!preloader.style.opacity) {
      preloader.style.opacity = 1;
  }
  if (preloader.style.opacity > 0) {
      preloader.style.opacity -= 0.1;
  } else {
      clearInterval(fadeEffect);
  }
}, 100);

window.addEventListener('load', fadeEffect);

*/

$(window).on('load', function () { // makes sure the whole site is loaded 
  $('#status').delay(300).fadeOut(); // will first fade out the loading animation 
  $('#preloader').delay(350).fadeOut('slow'); // will fade out the white DIV that covers the website. 
})


