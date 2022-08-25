const QUOTES = [
    {
        quote: 'Where words fail music feels.',
        author: 'Hans C Andersen'
    },
    {
        quote: 'Music, a magic beyond all we do here!',
        author: 'Albus Dumbledore'
    },
    {
        quote: 'Symphony starts when you walk together, feel the heart beats and understand the unspoken words.',
        author: 'Amit Ray'
    },
    {
        quote: 'The world is an orchestra, the universe is a symphony.',
        author: 'Matshona Dhliwayo'
    }
]

const SOUNDS = {
    'rain': 'https://assets.mixkit.co/sfx/download/mixkit-downpour-loop-1245.wav',
    'guitar': 'https://assets.mixkit.co/sfx/download/mixkit-cool-guitar-riff-2321.wav',
    'wind': 'https://assets.mixkit.co/sfx/download/mixkit-campfire-night-wind-1736.wav'
}

const HOWLS = {
    'rain': new Howl({
        src: SOUNDS.rain,
        volume: 0.5,
        loop: true,
        onpause: () => {removePLayingIndicator('rain')}
    }),
    'guitar': new Howl({
        src: SOUNDS.guitar,
        onend: () => {removePLayingIndicator('guitar')}
    }),
    'wind': new Howl({
        src: SOUNDS.wind,
        loop: true,
        onpause: () => {removePLayingIndicator('rain')}
    })
}

const INSTRUMENTBUTTONS = document.querySelectorAll('.instrument');

function scatterInstruments() {
    for (let instrumentbutton of INSTRUMENTBUTTONS) {
        instrumentbutton.style.top = `${Math.floor(Math.random() * 100)}%`
        instrumentbutton.style.left = `${Math.floor(Math.random() * 100)}%`
    }
}

function addPlayFunctionality() {
    for (let instrumentbutton of INSTRUMENTBUTTONS) {
        instrumentbutton.addEventListener('click', (e) => {
            const instrument = e.target.getAttribute('sound');
            if (!HOWLS[instrument].playing()) {
                HOWLS[instrument].play()
                console.log(HOWLS[instrument])
                e.target.classList.add('playing')
            } else {
                HOWLS[instrument].pause()
                e.target.classList.remove('playing')
            }
        })
    }
}

function removePLayingIndicator(sound) {
    document.querySelector(`i[sound=${sound}]`).classList.remove('playing')
}

function randomchoice(arr) {
    const ci = Math.floor(Math.random() * arr.length);
    return arr[ci];
}

window.addEventListener('load', () => {
    scatterInstruments();
    addPlayFunctionality();
    const quoteTextElement = document.querySelector('#quote-text');
    const quoteAuthorElement = document.querySelector('#quote-author');
    const {quote, author} = randomchoice(QUOTES);
    quoteTextElement.innerText = quote;
    quoteAuthorElement.innerText = `- ${author}`
})