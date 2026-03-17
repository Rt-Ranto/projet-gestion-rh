let _$id = (elts)=>{return document.getElementById(elts)}; 
let _$class = (elts)=>{return document.querySelector(elts)};

const le_form = _$class(".le_form");
const info_sup = _$class(".info_sup");
const i1 = _$id("inp1");
const l1 = _$id("lb1");
const i2 = _$id("inp2");
const l2 = _$id("lb2");
const i3 = _$id("inp3");
const l3 = _$id("lb3");
const i4 = _$id("inp4");
const l4 = _$id("lb4");
const i5 = _$id("inp5");
const l5 = _$id("lb5");
const i6 = _$id("inp6");
const l6 = _$id("lb6");
const i7 = _$id("inp7");
const l7 = _$id("lb7");
const i8 = _$id("inp8");
const l8 = _$id("lb8");
const i9 = _$id("inp9");
const l9 = _$id("lb9");
const i10 = _$id("inp10");
const l10 = _$id("lb10");
const i11 = _$id("inp11");
const l11 = _$id("lb11");
const date_naissance = _$id("date_naissance");
const gender = _$id("gender");
const s_m = _$id("s_m");
const d_e = _$id("d_e");


let csv_btn = _$class(".csv_btn");
let csv_frame = _$class(".le_csv");
let pdf_btn = _$class(".pdf_btn");
let pdf_frame = _$class(".le_pdf");


let svt = _$class(".suivant");
let svt1 = _$class(".suivant1");
let svt2 = _$class(".svt1");
let prec = _$class(".precedent");
let prec1 = _$class(".precedent1");
let prec2 = _$class(".precedent2");

svt.addEventListener('click', ()=>{
    if (i1.value.trim() !== "" && i2.value.trim() !== ""
        && date_naissance.value.trim() !== "" && gender.value.trim() !== ""){
        le_form.style.transition = "transform .7s ease";
        le_form.style.transform = "translateX(-350px)";
    }
    else
    {
        alert(" Veuiller completer \n les Informations Personnels.");
    }
   
});
svt1.addEventListener('click', ()=>{
    if (s_m.value.trim() !== "" && d_e.value.trim() !== ""
    ){
        le_form.style.transition = "transform .7s ease";
        le_form.style.transform = "translateX(-700px)";
    }else{
        alert("Veuiller entrer les informations \n suplementaires necéssaire.")
    }
   
});
svt2.addEventListener('click', ()=>{
    if (i5.value.trim() !== "" && i7.value.trim() !== ""
    ){
        le_form.style.transition = "transform .7s ease";
        le_form.style.transform = "translateX(-1050px)";
    }else{
        alert("Remplisser tous les champs pour passer\n au Validation .")
    }
});

prec.addEventListener('click', ()=>{
    le_form.style.transition = "transform .7s ease";
    le_form.style.transform = "translateX(0px)";
 });
prec1.addEventListener('click', ()=>{
   le_form.style.transition = "transform .7s ease";
   le_form.style.transform = "translateX(-350px)";
})
prec2.addEventListener('click', ()=>{
   le_form.style.transition = "transform .7s ease";
   le_form.style.transform = "translateX(-700px)";
})

i1.addEventListener('focus',() => {
    l1.innerText = "Nom";
})
i1.addEventListener('blur', ()=>{
    if (i1.value.trim() === ""){
        l1.innerText = "Nom ...";
    }    
})

function grrr(inp,lb,a,b) {
    inp.addEventListener('change',() => {
        lb.innerText = a;
    })
    inp.addEventListener('blur', ()=>{
        if(inp.value.trim() === ""){
            lb.innerText = b; 
        }
    })
}

csv_btn.addEventListener('click', function(){
    // csv_frame.style.transition = "transform .7s ease";
    csv_frame.style.transform = "translateY(50%)";
    pdf_btn.disabled = true;
    // alert('btn clicked');
   
});
pdf_btn.addEventListener('click', function(){
    // csv_frame.style.transition = "transform .7s ease";
    pdf_frame.style.transform = "translateY(50%)";
    csv_btn.disabled = true;
    console.log("pdf_btn");
   
});

let remove_csv_frame = ()=>{
    // account_profil.style.transition = "transform .7s ease";
    csv_frame.style.transform = "translateY(-300%)";
    pdf_btn.disabled = false;

}
let remove_pdf_frame = ()=>{
    // account_profil.style.transition = "transform .7s ease";
    pdf_frame.style.transform = "translateY(-300%)";
    csv_btn.disabled = false;
}


_$id('form1').addEventListener('submit', ()=>{
    _$id('loader').style.display = "flex";
    this.querySelector("button[type='submit']").disabled = true;
})
_$id('form2').addEventListener('submit', ()=>{
    _$id('loader').style.display = "flex";
    this.querySelector("button[type='submit']").disabled = true;
})


grrr(i1,l1,"Nom","Nom...");
grrr(i2,l2,"Prenom","Prenom...");
grrr(i3,l3,"Père","Père...");
grrr(i4,l4,"Mère","Mère...");
grrr(i5,l5,"Adresse","Adresse...");
grrr(i6,l6,"Email","Email...");
grrr(i7,l7,"Telephone","Telephone...");
grrr(i8,l8,"Grade","Grade...");
grrr(i9,l9,"Unite actuel","Unite actuel...");
grrr(i10,l10,"Matricule","Matricule...");
grrr(i11,l11,"Unite ancien","Unite ancien...");
