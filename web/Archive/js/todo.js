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
        let users = await response.json();

        if (users.length === 0) {
            alert("aucun utilisateur trouvé");
        }
        console.log(users);
        let p = document.querySelector('#button');
        p.onclick = function() {
            this.style.color='blue';
  }
    }
}


// function render(){
//     let list=[]
//     let ul= document.createElement('ul');
//     for (const title of #list){
//         let li = document.createElement('li');
//         li.textContent = title;
//         ul.append(li);
//     }

//     let container = document.querySelector(#nav1);
//     container.append(ul);
// }


// let list = new listRender('#nav1');
// events.forEach ((values) =>{
//     let e = new EventFactory(values.type, values);
//     list.add = e.title;
// });
// list.render(list, "#nav1")

function affiche_liste(liste){
    let elem = document.querySelector('#nav1');
    let ul = document.createElement("ul");

    for (const title of liste){
        let li = document.createElement('li');
        li.textContent = title;
        ul.append(li);

    elem.appendChild(ul);
    }
}
affiche_liste(["saliut", "hello", "hola"])

