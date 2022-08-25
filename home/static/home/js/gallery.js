const gallery = document.querySelector('#gallery');
const nav = document.querySelector('nav');
const main = document.querySelector('#main');

const image_api_url = 'https://aarohiworld.org/home/api/allimages';
const TOTAL_IMAGES = 2;

let data;
let last_image = 0;
const resp = fetch(image_api_url)
    .then(resp => resp.json())
    .then(json => {
        main.addEventListener('scroll', () => {
            let offset = main.scrollTop + window.innerHeight;
            let height = main.scrollHeight;
            const diff = height - offset;
            if (diff < 2) {
                addRandomImages(10) 
            }
        })

        function addRandomImages(count) {
            let lastDescChoice = 0;
            for (let j = 0; j < count && last_image + j < json.length; j++) {
                let {image, description} = json[(last_image + j) % json.length];
                if (description == undefined) {
                    let choice = Math.floor(Math.random() * DESCS.length);
                    while (choice == lastDescChoice) {
                        choice = Math.floor(Math.random() * DESCS.length);
                    }
                    description = DESCS[choice]
                    lastDescChoice = choice;
                }
                let node = createRandomImage(image, description);
                gallery.appendChild(node);
            }
            last_image += count;
        }

        /*
        main.addEventListener('scroll', () => {
            let offset = main.scrollTop + window.innerHeight;
            let height = main.scrollHeight;
            const diff = height - offset;
            if (diff < 2) {
                addRandomImages(10) 
            }
        })
        */
        addRandomImages(10);
    })


const DESCS = [
    'A Photograph',
    'Moments captured in time',
    'Snapped and Etched',
    'Some moments are worth a thousand words and a million pixels',
    'An enigma, frozen in time',
]


function createRandomImage(url, description) {
    // Create an image container
    // This acts as a photo frame
    const container = document.createElement('div');
    container.classList.add('photo');
    // Create the actual img tag to fetch the image
    const imageNode = document.createElement('img');
    const height = 300 + Math.floor(Math.random() * 5) * 100;
    const width = 300 + Math.floor(Math.random() * 5) * 100;
    imageNode.src = url;
    if (window.innerWidth > 720 && window.innerWidth > window.innerHeight) {
        imageNode.style.width = `${width}px`;
        imageNode.style.objectFit = "contain";
    } else {
        imageNode.style.objectFit = "contain";
    }
    // Add img to container
    container.appendChild(imageNode);
    // Create an overlay with text we might want to show
    const overlay = document.createElement('div');
    overlay.classList.add('image-overlay');
    container.appendChild(overlay);
    // Create a text-container so that text doesn't fill the overlay
    const overlayText = document.createElement('div');
    overlayText.classList.add('overlay-text');
    // TODO: fetch descriptions from API
    overlayText.innerText = description;
    overlay.appendChild(overlayText);
    // Return the container
    // NOTE: user has to manually add it to DOM
    return container;
}

let i = 0;
function addRandomImages(count) {
    for (let j = 0; j < count; j++) {
        let {image, description} = data[(i + j) % data.length];
        if (description == undefined) {
            const choice = Math.floor(Math.random() * DESCS.length);
            description = DESCS[choice]
        }
        let node = createRandomImage(image, description);
        gallery.appendChild(node);
    }
    i += count;
}

// Code for the shader-comet
// Copy pasted from: https://codepen.io/shubniggurath/pen/dKwegY
// All credits to original author
/*
Most of the stuff in here is just bootstrapping. Essentially it's just
setting ThreeJS up so that it renders a flat surface upon which to draw
the shader. The only thing to see here really is the uniforms sent to
the shader. Apart from that all of the magic happens in the HTML view
under the fragment shader.
*/
let container;
let camera, scene, renderer;
let uniforms;
let divisor = 1 / 10;
let capturing = false;
let newmouse = {
    x: 0,
    y: 0
};
let loader = new THREE.TextureLoader();
let texture, rtTexture, rtTexture2;
loader.setCrossOrigin("anonymous");
loader.load('https://s3-us-west-2.amazonaws.com/s.cdpn.io/982762/noise.png', function do_something_with_texture(tex) {
    texture = tex;
    texture.wrapS = THREE.RepeatWrapping;
    texture.wrapT = THREE.RepeatWrapping;
    texture.minFilter = THREE.LinearFilter;
    init();
    animate();
});
function init() {
    container = document.getElementById('bg-container');
    camera = new THREE.Camera();
    camera.position.z = 1;
    scene = new THREE.Scene();
    var geometry = new THREE.PlaneBufferGeometry(2, 2);
    rtTexture = new THREE.WebGLRenderTarget(window.innerWidth * .2, window.innerHeight * .2);
    rtTexture2 = new THREE.WebGLRenderTarget(window.innerWidth * .2, window.innerHeight * .2);
    uniforms = {
        u_time: { type: "f", value: 1.0 },
        u_resolution: { type: "v2", value: new THREE.Vector2() },
        u_noise: { type: "t", value: texture },
        u_buffer: { type: "t", value: rtTexture.texture },
        u_mouse: { type: "v2", value: new THREE.Vector2() },
        u_renderpass: { type: 'b', value: false }
    };
    var material = new THREE.ShaderMaterial({
        uniforms: uniforms,
        vertexShader: document.getElementById('vertexShader').textContent,
        fragmentShader: document.getElementById('fragmentShader').textContent
    });
    material.extensions.derivatives = true;
    var mesh = new THREE.Mesh(geometry, material);
    scene.add(mesh);
    renderer = new THREE.WebGLRenderer();
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);
    onWindowResize();
    window.addEventListener('resize', onWindowResize, false);
    document.addEventListener('pointermove', (e) => {
        let ratio = window.innerHeight / window.innerWidth;
        newmouse.x = (e.pageX - window.innerWidth / 2) / window.innerWidth / ratio;
        newmouse.y = (e.pageY - window.innerHeight / 2) / window.innerHeight * -1;
        e.preventDefault();
    });
}
function onWindowResize(event) {
    renderer.setSize(window.innerWidth, window.innerHeight);
    uniforms.u_resolution.value.x = renderer.domElement.width;
    uniforms.u_resolution.value.y = renderer.domElement.height;
    rtTexture = new THREE.WebGLRenderTarget(window.innerWidth * .2, window.innerHeight * .2);
    rtTexture2 = new THREE.WebGLRenderTarget(window.innerWidth * .2, window.innerHeight * .2);
}
function animate(delta) {
    requestAnimationFrame(animate);
    render(delta);
}
let capturer = new CCapture({
    verbose: true,
    framerate: 60,
    // motionBlurFrames: 4,
    quality: 90,
    format: 'webm',
    workersPath: 'js/'
});
isCapturing = function (val) {
    if (val === false && window.capturing === true) {
        capturer.stop();
        capturer.save();
    }
    else if (val === true && window.capturing === false) {
        capturer.start();
    }
    capturing = val;
};
toggleCapture = function () {
    isCapturing(!capturing);
};
window.addEventListener('keyup', function (e) { if (e.keyCode == 68)
    toggleCapture(); });
let then = 0;
function renderTexture(delta) {
    // let ov = uniforms.u_buff.value;
    let odims = uniforms.u_resolution.value.clone();
    uniforms.u_resolution.value.x = window.innerWidth * .2;
    uniforms.u_resolution.value.y = window.innerHeight * .2;
    uniforms.u_buffer.value = rtTexture2.texture;
    uniforms.u_renderpass.value = true;
    //   rtTexture = rtTexture2;
    //   rtTexture2 = buffer;
    window.rtTexture = rtTexture;
    renderer.setRenderTarget(rtTexture);
    renderer.render(scene, camera, rtTexture, true);
    let buffer = rtTexture;
    rtTexture = rtTexture2;
    rtTexture2 = buffer;
    // uniforms.u_buff.value = ov;
    uniforms.u_buffer.value = rtTexture.texture;
    uniforms.u_resolution.value = odims;
    uniforms.u_renderpass.value = false;
}
function render(delta) {
    uniforms.u_mouse.value.x += (newmouse.x - uniforms.u_mouse.value.x) * divisor;
    uniforms.u_mouse.value.y += (newmouse.y - uniforms.u_mouse.value.y) * divisor;
    uniforms.u_time.value = delta * 0.0005;
    renderer.render(scene, camera);
    renderTexture();
    if (capturing) {
        capturer.capture(renderer.domElement);
    }
}