const IMAGE_URLS = [
    'https://upload.wikimedia.org/wikipedia/en/f/ff/SuccessKid.jpg',
    'https://i.pinimg.com/originals/7b/4d/a9/7b4da9ca53fd8f43d340d5f19b8d6944.jpg'
]

const CAPTIONS = [
    'Account Made, Great Success! check your mail for your Aarohi ID',
    'Registration Done! check your mail for your Aarohi ID'
]

const image_choice = Math.floor(Math.random() * IMAGE_URLS.length);
const image_src = IMAGE_URLS[image_choice]

const caption_choice = Math.floor(Math.random() * CAPTIONS.length);
const caption = CAPTIONS[caption_choice]

const image = document.querySelector('#success-image');
image.src = image_src;

const caption_container = document.querySelector('#caption');
caption_container.innerText = caption;