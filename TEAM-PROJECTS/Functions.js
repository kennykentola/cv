var Id = (e) => {
return document.getElementById(e);
};

var querySelector = (e) => {
return document.querySelector(e);
}

var addClass = function(e,classes){
querySelector(e).classList.add(classes);
}

var removeClass = function(e,classes){
querySelector(e).classList.remove(classes);
}

var toggleClass = function(e,classes){
querySelector(e).classList.toggle(classes);
}

function addEvent(dom,evt,funct,bool=false){
document.querySelector(dom).addEventListener(evt,funct,bool);
}

function LoadStyles(styles){
window.addEventListener("DOMContentLoaded",function(){
styles.map(function(style){
document.head.insertAdjacentHTML('beforeend', `<link rel="stylesheet" type="text/css" href="${style}.css">`);
});
})
}

function __JsonRender(pos,dom,json,func){
if(Array.isArray(json)){
Id(dom).insertAdjacentHTML(`${pos}`,`${json.map(func).join("")}`);
}
}

function __miniRender(json,func){
if(Array.isArray(json)){
return(`${json.map(func).join("")}`);
}
}

function html(dom,funct){
document.querySelector(dom).innerHTML  = funct();
}
