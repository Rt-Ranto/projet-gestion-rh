let _$class = (elts)=>{return document.querySelector(elts);}
const mediaQuery = window.matchMedia("(max-width: 600px)");
const menu = _$class(".menuconge");
const rech = _$class(".floating-search");
const rech_btn = _$class(".rech_btn");

retrecie = false;
function retreciMenu(){
    const icon = _$class(".fleche");
    if (!retrecie){
        menu.style.width = "170px";
        rech.style.left = "185px";
        icon.classList.replace("fa-arrow-right","fa-arrow-left");
        retrecie = true;
    }else{
        menu.style.width = "60px";
        rech.style.left = "75px";
        icon.classList.replace("fa-arrow-left","fa-arrow-right");
        retrecie = false;
    }
}

// ajuste le menu quand la taille de l'écran change
function handleWidth(e) {
    if (e.matches) {
        menu.style.width = "60px";
        rech.style.left = "75px";
        _$class(".liste_g").style.display = "none";
        retrecie=false
    } else {
        menu.style.width = "170px";
        rech.style.left = "185px";
        _$class(".liste_g").style.display = "flex";
        retreciMenu();
    }
}

rech_btn.addEventListener('click', ()=>{
    rech.style.transform = "translateX(0)";
})
rech.addEventListener('mouseleave',()=>{
    rech.style.transform = "translateX(-200%)";
})

handleWidth(mediaQuery);
mediaQuery.addEventListener("change", handleWidth);