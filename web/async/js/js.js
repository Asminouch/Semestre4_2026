
//todo1 
// function mathRandom() {
//     return new Promise((resolve, reject) => {
//         console.log("la promsesse")
//         setTimeout(() => {
//             // réussir une fois sur deux
//         if (Math.random()> 0.5) {
//             resolve("result");
//         } else {
//             reject("error");
//         }
//         }, 3000)
        
//     });
// }

// const promsesse = mathRandom();
// console.log(promsesse);
// promsesse.then(
//     function(result) {
//     console.log(result);
//     },
//     function(error) {
//     console.log(error);
//     }
// );

// // Ou avec des arrows function
// promsesse.then(
//     result => console.log(result),
//     error => console.log(error)
// );


//2eme todo

function loadScript(src) {
    return new Promise((resolve, reject) => {
        let script = document.createElement('script');
        script.src = src;
        setTimeout(() => {
            document.head.append(script);
        }, 3000);
        script.onload=() =>resolve('fichier'+ src +'charge');
        script.onerror=()=>  reject(new Error('echec du chargement'+ src));
    });
}

async function loadAllScript() {
    const script1 = await loadScript('js/1.js')
    console.log(script1)
    const script2 = await loadScript('js/2.js')
    console.log(script2)
    const script3 = await loadScript('js/3.js')
    console.log(script3)
    
}

loadAllScript() 
//loadallScript a la place de ca en bas 
// loadScript('js/1.js')
//     .then(result => loadScript('js/2.js'))
//     .then(result => loadScript('js/3.js'))
//     .catch(error => console.log(error));

//todo 3

async function rechercheUsername() {
    const username = prompt("Entrez un nom d'utilisateur:");
    const url = `https://jsonplaceholder.typicode.com/users?username=${username}`;

    let response = await fetch(url);
    if (!response.ok) {
        alert("HTTP-Error: " + response.status);
        return;
    }else {
        let users = await response.json();

        if (users.length === 0) {
            alert("aucun utilisateur trouvé");
        }
        console.log(users);

    }
}

rechercheUsername();
//Bret, Antonette