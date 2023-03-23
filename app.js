const title = document.getElementById('title');
const root = document.getElementById('root');

title.textContent = 'This is a react class';

const h1 = document.createElement('h1');
// const text = document.createTextNode('Welcome to react js');
h1.textContent = 'Welcome to react js';
root.appendChild(h1);

const link = document.createElement('a');
// link.setAttribute(attr);
link.textContent = 'For more info, click on this link!';
root.appendChild(h1);
