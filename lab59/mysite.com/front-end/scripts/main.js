const body = document.body;
const h1 = document.createElement('h1');
const btn = document.querySelector('button');
const ul = document.querySelector('ul');

h1.innerHTML = 'Welcome to my site';
body.appendChild(h1);

btn.addEventListener('click', function (e) {
	ul.remove()
})

