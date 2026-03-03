import users from './module/data.js';
import {Card} from './module/card.js';

//console.log(users)

let ul = document.querySelector("#menu");
let info = document.querySelector("#info");

let myuser = await users;
console.log(myuser);

for (const user of myuser){
    let li = document.createElement("li");
    let a  = document.createElement("a");
    a.textContent = user.username;
    a.setAttribute('user_id', user.id);
    a.addEventListener('click',  (e) =>{
        let user_card = new Card(user);
        info.innerHTML = null;
        info.append(user_card.draw());
    })
    li.append(a);
    //li.innerHTML = user.username;
    ul.append(li);

}