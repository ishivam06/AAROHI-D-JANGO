/*
interface EventData {
    name: string,
    description: string,
    longDescription: string,
    registrationLinks: {
        solo: string,
        duet?: string,
        group?: string
    }
}
*/
const testEvent = {
    name: 'Test',
    description: 'test test tes',
    longDescription: 'test test test test',
    registrationLinks: {
        solo: 'https://www.google.com/',
        duet: 'https://www.bing.com/'
    }
}

const events = {
    'Test': testEvent,

}

const app = document.querySelector('#app')
const eventModal = document.querySelector('#event-modal');
const modalCloseButton = document.querySelector('#modal-close-button');
const modalTitle = document.querySelector('#modal-title');

const modalTabs = document.querySelectorAll('.modal-tab-title');
const modalTabContent = document.querySelector('#modal-tab-content');

const clist = document.querySelector('#event-cards-list');
for (let i = 0; i < 10; i++) {
    clist?.appendChild(constructCard(testEvent))
}

// Modal click handler
modalCloseButton.addEventListener('click', () => {
    eventModal.classList.remove('modal-show')
})

const exploreButtons = document.querySelectorAll('.controls button')
let currentEvent = ''

// Set event listeners for every click button
exploreButtons.forEach(button => {
    button.addEventListener('click', (e) => {
        const targetEvent = (e.target).getAttribute('event')
        console.log(targetEvent)
        currentEvent = targetEvent;
        eventModal.classList.add('modal-show');
        modalTitle.innerText = targetEvent.toUpperCase();
    })
})

// Modal tab switching logic
modalTabs.forEach(tab => {
    tab.addEventListener('click', (e) => {
        // Get the tab to swicth to
        const switchTo = (e.target).getAttribute('tab');
        // Mark all tabs as inactive
        modalTabs.forEach(tab => (tab).classList.remove('active-tab'));
        // Mark tab to switch to as active
        (e.target).classList.add('active-tab')
        // Remove the earlier content
        while (modalTabContent.firstChild) {
            modalTabContent.firstChild.remove()
        }
        // Populate the tab with corresponding content
        switch (switchTo) {
            case 'about':
                modalTabContent.appendChild(constructAbout(events[currentEvent]))
                break;
            case 'register':
                modalTabContent.appendChild(constructRegister(events[currentEvent]))
                break;
        }
    })
})

// These functions only generate html and mark elements with relevant classes
function constructCard(ed) {
    // Main card
    const container = document.createElement('div')
    container.classList.add('event-card');
    // Event title
    const title = document.createElement('div')
    title.classList.add('event-title')
    title.innerText = ed.name
    container.appendChild(title)
    // Event body
    const eb = document.createElement('div');
    const descr = document.createElement('div');
    descr.innerText = ed.longDescription;
    const controls = document.createElement('div');
    controls.classList.add('controls')
    const exploreButton = document.createElement('button');
    exploreButton.setAttribute('event', ed.name);
    exploreButton.innerText = 'EXPLORE'
    controls.appendChild(exploreButton);
    eb.appendChild(descr)
    eb.appendChild(controls)
    container.appendChild(eb)
    return container;
}

function constructAbout(ed) {
    const container = document.createElement('div');
    container.classList.add('modal-about');
    const text = document.createElement('div');
    text.innerHTML = ed.longDescription;
    container.appendChild(text)
    return container;
}

function constructRegister(ed) {
    const container = document.createElement('div');
    container.classList.add('modal-register');
    const controls = document.createElement('div');
    controls.classList.add('modal-register-controls');
    if (ed.registrationLinks.solo) {
        const link = document.createElement('a');
        link.innerText = 'SOLO'
        link.href = ed.registrationLinks.solo;
        controls.appendChild(link)
    }
    if (ed.registrationLinks.duet) {
        const link = document.createElement('a');
        link.innerText = 'DUET'
        link.href = ed.registrationLinks.duet;
        controls.appendChild(link)
    }
    if (ed.registrationLinks.group) {
        const link = document.createElement('a');
        link.innerText = 'GROUP'
        link.href = ed.registrationLinks.group;
        controls.appendChild(link)
    }
    container.appendChild(controls);
    return container;
}
