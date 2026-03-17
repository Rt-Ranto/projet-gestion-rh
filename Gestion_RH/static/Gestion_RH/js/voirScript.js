
console.log("prprprpr");
window.addEventListener('load', ()=>{
    console.log("load");
});


async function downloadPdf(button) {
    const pdfUrl = button.getAttribute('data-url');
    const redirectUrl = button.getAttribute('data-redirect');
    const loader = document.getElementById('loader');
    const loaderText = loader.querySelector('p');
    const spinner = document.querySelector('.spinner');
    
    console.log("changed");
    // AFFICHER le loader
    loader.style.display = 'flex';
    loaderText.textContent = 'Preparation du PDF';
    button.disabled = true;

    const theIntervalle = setInterval(() => {
        if (loaderText.textContent.length < 24 ){
            loaderText.textContent += " .";
        }else{
            loaderText.textContent = 'Preparation du PDF';
        }
        
    }, 500);

    const blockedEvent = (e)=>{
        e.preventDefault();
    }
    document.querySelector(".ret").querySelectorAll('a').forEach(link => {
        link.style.pointerEvents = 'none';
        link.style.opacity = '0.5';
        link.style.cursor = 'not-allowed';
       
        link.addEventListener('click', blockedEvent);        
    });
    
    try {
        const response = await fetch(pdfUrl);
        
        if (!response.ok) {
            throw new Error('Erreur de téléchargement');
        }
        
        // Changer le message
        loaderText.textContent = 'Préparation du fichier...';
        
        const blob = await response.blob();
        
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        
        const contentDisposition = response.headers.get('Content-Disposition');
        let filename = 'employe.pdf';
        if (contentDisposition) {
            const match = contentDisposition.match(/filename="?([^"]+)"?/);
            if (match) filename = match[1];
        }
        
        a.download = filename;
        document.body.appendChild(a);
        a.click();
        
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
        clearInterval(theIntervalle);
        // Message de succès
        spinner.style.display = 'none';
        loaderText.textContent = '✓ Téléchargement réussi !'; 
        setTimeout(() => {
            loader.style.display = "none";
        }, 4000);
        
        button.disabled = false;
        document.querySelector(".ret").querySelectorAll('a').forEach(link => {
            link.style.pointerEvents = 'auto';
            link.style.opacity = '1';
            link.style.cursor = 'pointer';
            link.removeEventListener('click', blockedEvent);
            
        });
        // Attendre un peu avant de cacher
        // setTimeout(() => {
        //     loader.style.display = 'none';
        //     window.location.href = redirectUrl;
        // }, 800);
        
    } catch (error) {
        console.error('Erreur:', error);
        loader.style.display = 'none';
        button.disabled = false;
        alert('Erreur lors du téléchargement du PDF');
    }
}