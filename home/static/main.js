function deviceWidth(){
    document.getElementById("width").innerHTML=window.innerWidth + "px";
}
window.onresize = deviceWidth;  
window.onload = deviceWidth;

/*defining variables*/
var btt = document.querySelector(".back-to-top");
var body = document.body;
var docElem = document.documentElement;
offset = 650;
var isFireFox= navigator.userAgent.toLowerCase().indexOf("firefox") > -1;

/*adding scroll event*/
window.addEventListener("scroll", function () {
    var btt = document.querySelector(".back-to-top");
    btt.classList.toggle("active", window.scrollY > offset);
});

/*adding click event*/
window.addEventListener("click", function(){
    if (isFireFox){
        btt.docElem.scrollTop = 0;
    }
    else{
        btt.body.scrollTop = 0;
    } 
}); 

/*click event for hamburger menu*/
var menu = document.getElementById("bars");
var nav = document.querySelector(".dropdown");
var lists = document.getElementById("interests");
var lists_items = document.querySelector(".sub-dropdown1");

menu.addEventListener("click", function (){
    nav.classList.toggle("active");
});

lists.addEventListener("click", ()=>{
    lists_items.classList.toggle("active");
});