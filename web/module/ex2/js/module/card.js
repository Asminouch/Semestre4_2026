class Card{
    constructor(user){
        this.user = user;
    }
    draw(){
        let ul = document.createElement("ul");
        for (const key in this.user){
            
            const element = this.user[key];
            ul.append(this.#line(key, element))
        }
        return ul
    }

    #line(label, value){
        let li = document.createElement("li");
        li.innerHTML = `<strong> ${label} : </strong> ${value}`;
        return li;
    }
}

export {Card};