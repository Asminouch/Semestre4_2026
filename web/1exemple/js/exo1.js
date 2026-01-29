let button = document.querySelector('#action');
        button.addEventListener('click', function(e){
            console.log("click sur action");
            let paragraphe = document.querySelector('p');
            paragraphe.classList.remove('design');});

        let buttonAdd = document.querySelector('#add');
        buttonAdd.addEventListener('click', function(e){
            console.log("click sur add");
            let paragraphe = document.querySelector('p');
            paragraphe.classList.add('design');});


