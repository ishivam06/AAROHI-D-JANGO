const tabs = {
    about: {
        header: document.querySelector('#tab-title-about'),
        content: document.querySelector('#content-about')
    },
    faq: {
        header: document.querySelector('#tab-title-faq'),
        content: document.querySelector('#content-faq')
    },
    reachout: {
        header: document.querySelector('#tab-title-reachout'),
        content: document.querySelector('#content-reachout')
    },
    register: {
        header: document.querySelector('#tab-title-register'),
        content: document.querySelector('#content-register')
    }
}

let currentTab = 'about'

function switchToTab(tabName) {
    console.log(`swtiching to ${tabName}`);
    switch (tabName) {
        case 'about':
            tabs.about.content.classList.add('active-content')
            break;
        case 'faq':
            tabs.faq.content.classList.add('active-content')
            break;
        case 'reachout':
            tabs.reachout.content.classList.add('active-content')
            break;
        case 'register':
            tabs.register.content.classList.add('active-content')
            break;
        default:
            console.log(`inavlid tab ${tabName}`)
    }
}

for (tab in tabs) {
    tabs[tab].header.addEventListener('click', (e) => {
        const switchTo = e.target.getAttribute('name');
        if (switchTo != currentTab) {
            for (alltab in tabs) {
                tabs[alltab].header.classList.remove('active-tab');
                tabs[alltab].content.classList.remove('active-content');
            }
            e.target.classList.add('active-tab');
            switchToTab(e.target.getAttribute('name'))
        }
        currentTab = switchTo
    })
}