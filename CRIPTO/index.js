const sideMenu = document.querySelector("aside");
const menuBtn = document.querySelector("#menu-btn");
const closeBtn = document.querySelector("#close-btn");
const themeToggle = document.querySelector(".theme-toggle")

menuBtn.addEventListener('click',() =>{
sideMenu.style.display ='block';
})

closeBtn.addEventListener('click',()=>{
  sideMenu.style.display ='none';
})

//change color
themeToggle.addEventListener('click',()=>{
  document.body.classList.toggle('dar-theme-variable');

  themeToggle.querySelector('img:nth-child(1)').classList.toggle('active');
  // themeToggle.querySelector('img:nth-child(2)').classList.toggle('active');
})
