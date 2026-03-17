const inp = document.getElementById("inp");
const inp1 = document.querySelector(".inp1");
const lb = document.getElementById("lb");
const p1 = document.getElementById("lb1");


inp.addEventListener('focus',() => {
    lb.innerText = "Admin";
})
inp.addEventListener('blur', ()=>{
    if (inp.value.trim() === ""){
        lb.innerText = "Nom de l'Admin ...";
    }
    
})
inp1.addEventListener('focus',() => {
    lb1.innerText = "Mot de passe";
})
inp1.addEventListener('blur', ()=>{
    if(inp1.value.trim() === ""){
        lb1.innerText = "Mot de passe ..."; 
    }
    
})
function togglePassword() {
  const input = document.getElementById("password");
  const icon = document.querySelector(".toggle-password");

  if (input.type === "password") {
    input.type = "text";
    icon.classList.replace("fa-eye", "fa-eye-slash");
  } else {
    input.type = "password";
    icon.classList.replace("fa-eye-slash", "fa-eye");
  }
}