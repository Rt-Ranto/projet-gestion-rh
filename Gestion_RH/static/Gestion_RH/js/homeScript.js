let _$class = (elts)=>{return document.querySelector(elts);}
const btn_menu = _$class(".bars_menu");
const menu = _$class(".menu");
const mediaQuery = window.matchMedia("(max-width: 600px)");
const account_profil = _$class(".account_profil");

// valeurs fixes
const smallWidth = "67px";
const smallCollapsed = "0px";
const largeWidth = "180px";
const largeCollapsed = "66px";

let width_actuel;
let account_btn = _$class(".account_btn");
let retrecie = false;
// toggle menu
btn_menu.addEventListener("click", () => {

    if (width_actuel === smallCollapsed) {
        // petit écran
        menu.style.width = smallWidth;
        width_actuel = smallWidth;
    }
    else if (width_actuel === smallWidth){
        menu.style.width = smallCollapsed;
        width_actuel = smallCollapsed;
    } 
    else if (width_actuel === largeCollapsed){
        menu.style.width = largeWidth;
        width_actuel = largeWidth;
    }
    else {
        // grand écran
        menu.style.width = largeCollapsed;
        width_actuel = largeCollapsed;
    }
});

// ajuste le menu quand la taille de l'écran change
function handleWidth(e) {
    if (e.matches) {
        menu.style.width = smallCollapsed;
        width_actuel = smallCollapsed
    } else {
        menu.style.width = largeWidth;
        width_actuel = largeWidth
    }
}

account_btn.addEventListener('click', function(){
    account_profil.style.transition = "transform .7s ease";
    account_profil.style.transform = "translateY(100px)";
   
});

let remove_account_profil = ()=>{
    account_profil.style.transition = "transform .7s ease";
    account_profil.style.transform = "translateY(-300px)";
}
function retreciDash(){
    const dashboard = _$class(".dashboard");
    const icon = _$class(".fleche");
    if (!retrecie){
        dashboard.style.height = "155px";
        icon.classList.replace("fa-arrow-down","fa-arrow-up");
        retrecie = true;
    }else{
        dashboard.style.height = "0px";
        icon.classList.replace("fa-arrow-up","fa-arrow-down");
        retrecie = false;
    }
}
// function hoverItem(){
//     const ll = _$class('.empl');
//     ll.classList.add("msentr");
// }
// function notHoverItem(){
//     const ll = _$class('.empl');
//     ll.classList.remove('msentr');
// }
// initialisation
handleWidth(mediaQuery);
mediaQuery.addEventListener("change", handleWidth);

