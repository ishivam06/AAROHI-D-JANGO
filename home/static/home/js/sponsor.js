/*
const bgm = new Howl({
  src: bgmPath,
  loop: true,
});

window.addEventListener("load", (e) => {
  document.querySelector("#music-message").style.display = "flex";
  document.querySelector("#navbar").style.display = "none";
  document.querySelector("#music-button").style.display = "none";
  document.querySelector("#music-message").addEventListener("click", (e) => {
    document.querySelector("#music-message").style.display = "none";
    document.querySelector("#music-button").style.display = "block";
    document.querySelector("#navbar").style.display = "flex";
    if (!bgm.playing()) {
      bgm.play();
    }
  });
  document.querySelector("#music-button").addEventListener("click", (e) => {
    document.querySelector("#music-button").classList.toggle("fa-volume-xmark");
    document.querySelector("#music-button").classList.toggle("fa-music");
    if (bgm.playing()) {
      bgm.pause();
    } else {
      bgm.play();
    }
  });
});
*/

const bgm = new Howl({
    src: bgmPath,
    loop: true,
});

const easterEgg = () => {
    if (!bgm.playing()) {
        bgm.play()
    } else {
        bgm.pause();
    }
}

const spons = [
  "avi-electrical",
  "canara-bank",
  "chilli",
  "coca",
  "cozmoderm",
  "da-bakery",
  "denver-hamilton",
  "dinshaws",
  "dp-jain",
  "elaichi",
  "levels",
  "fastrack",
  "frankie",
  "global-power",
  "health-potli",
  "hotel-embassy",
  "hr-mentors",
  "ies-master",
  "integrity",
  "js-events",
  "kingsway",
  "ktm",
  "lush-house",
  "maac",
  "trendz",
];

//get path according to host name
const host = window.location.hostname;
const path =
  host === "127.0.0.1"
    ? "/static/home/images/previous_sponsors/"
    : "https://dszmbw7j07tnz.cloudfront.net/static/home/images/previous_sponsors/";

const prevSponsList = document.querySelector(".previous-sponsors > .card-list");

const titlespons = document.querySelector(".title-sponsors");
titlespons.style.display = "none";
//const majorspons = document.querySelector(".major-sponsors");
//majorspons.style.display = "none";
const otherspons = document.querySelector(".other-sponsors");
otherspons.style.display = "none";

function createPrevSponsorImage(url) {
  const card = document.createElement("div");
  card.classList.add("sponsor-card", "sponsor-card-previous");
  const container = document.createElement("div");
  container.classList.add("sponsor-logo-container");
  const image = document.createElement("img");
  image.src = url;
  container.appendChild(image);
  card.appendChild(container);
  return card;
}

spons.forEach((sponsor) => {
  const sponsCard = createPrevSponsorImage(`${path}${sponsor}.jpg`);
  prevSponsList.appendChild(sponsCard);
});

console.log('Looking for easter eggs 🐰🥚');
console.log('Try being a bit literal in your hunt!');
