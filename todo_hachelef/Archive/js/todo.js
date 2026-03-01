//quand on fait fetch pour chercher api on met option dans fetch ou 
//CORS  --> pip install flask-cors
//https://www.youtube.com/watch?v=2sQ9xiEAXNo     
//https://www.reddit.com/r/learnjavascript/comments/1m1b448/async_await_vs_fetch_then_catch/ 
//differe, document.onload(), ==> attendre dom chargé et apres on met le listener


async function recupTache(){
    const url = `http://localhost:5000/todo/api/v1.0/tasks`;

    let response = await fetch(url);

    if (!response.ok) {
        alert("HTTP-Error: " + response.status);
        return;
    }else {
        // let users = await response.json();

        let data = await response.json();
        console.log(data);

        affiche_liste(data.tasks)

    }
}

let current_task = null;

function affiche_liste(liste){

    let elem = document.querySelector('#taches');
    let ul = document.createElement("ul");
    elem.innerHTML = "";
    ul.addEventListener('mouseover', function(event){event.target.style.color = "orange";
        setTimeout(function(){event.target.style.color = "";}, 100);
     });

    for (const tache of liste){
        let li = document.createElement('li');
        li.textContent = tache.title;

        li.addEventListener('click', function() {
            affiche_tache(tache);});
        ul.appendChild(li);

    }
    elem.appendChild(ul);
}

document.addEventListener('DOMContentLoaded', function() {
    let bouton = document.querySelector('#button');
    bouton.addEventListener('click', recupTache);
    document.querySelector("#del").addEventListener("click", supprimer_tache);
    document.querySelector("#add").addEventListener("click", ajouter_tache);
});
function affiche_tache(tache){
    current_task = tache;
    let zone = document.querySelector("#currenttask")

    zone.innerHTML = `
    <label> titre </label><br>
    <input type = "text" id ="title" value = "${tache.title}"><br><br>

    <label> description </label><br>
    <textarea id="description">${tache.description}</textarea><br><br>

    <label> Tache terminée ? </label><br>
    <input type="checkbox" id="done" ${tache.done ? "checked" : ""}><br><br>

    <button id="save">Sauvegarder</button>`;

    document.querySelector("#save").addEventListener('click', sauvegarder_tache);

}


async function sauvegarder_tache(){
    let title = document.querySelector("#title").value;
    let description = document.querySelector("#description").value;
    let done = document.querySelector("#done").checked;

    let response = await fetch (current_task.uri,{
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            title: title,
            description: description,
            done: done
        })
    });

    console.log(response.status)
    if (response.ok) {
    recupTache(); // Recharger la liste des tâches
    }
}

async function supprimer_tache(){

    if(!current_task){
        alert ("Sélectionne une tâche");
        return;
    }
    
    await fetch(current_task.uri,
        {method : "DELETE"}
    );
    current_task = null;
    document.querySelector("#currenttask").innerHTML = "";
    recupTache();
}

function ajouter_tache(){
    let zone = document.querySelector("#currenttask")

    zone.innerHTML = `
    <label> titre </label><br>
    <input id ="title"><br><br>

    <label> description </label><br>
    <textarea id="description"></textarea><br><br>

    <label> Tache terminée ? </label><br>
    <input type="checkbox" id="done"><br><br>

    <button id="create">Créer tâche</button>`;
    
    document.querySelector("#create").addEventListener("click", creer_tache);
}

async function creer_tache(){
    let title = document.querySelector("#title").value;
    let description = document.querySelector("#description").value;
    let done = document.querySelector("#done").checked;

    if(title === ""){
        alert("Vous n'avez pas mis de titre");
        return;
    }

    await fetch ("http://localhost:5000/todo/api/v1.0/tasks",{
        method : "POST",
        headers : {"Content-Type" : "application/json"},
        body : JSON.stringify({
            title : title,
            description : description,
            done : done
        })
    }
);  
    document.querySelector("#currenttask").innerHTML = "";
    recupTache();
}