// script.js

document.getElementById('menuToggle').addEventListener('click', function() {
    var dropdownMenu = document.getElementById('dropdownMenu');
    if (dropdownMenu.style.display === 'block') {
        dropdownMenu.style.display = 'none';
    } else {
        dropdownMenu.style.display = 'block';
    }
});



// script.js

document.getElementById('readMoreBtn').addEventListener('click', function() {
    var content = document.querySelector('.content');
    content.classList.toggle('expanded');
    var btn = document.getElementById('readMoreBtn');
    if (content.classList.contains('expanded')) {
        btn.textContent = 'Read Less';
    } else {
        btn.textContent = 'Read More';
    }
});


document.getElementById('readMoreBtn').addEventListener('click', function() {
    var content = document.querySelector('.talk');
    content.classList.toggle('expanded');
    var btn = document.getElementById('readMoreBtn');
    if (content.classList.contains('expanded')) {
        btn.textContent = 'Read Less';
    } else {
        btn.textContent = 'Read More';
    }
});