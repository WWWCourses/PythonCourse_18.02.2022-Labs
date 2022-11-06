const pass = document.querySelector('[type="password"]')
const btn = document.querySelector('button')

btn.addEventListener('click', function(e) {
	е.preventDefault();
	password = pass.value;
	console.log(password);
})


const images = [
	'./images/2022/femaile/HTTP_ClientServerSystem.png',
	'./images/2022/femaile/HTTP_ClientServerSystem.png',
]

images.forEach(imgsrc=>{
	const img = document.createElement('IMG')
	img.src = imgsrc
	document.body.appendChild(img)
})


