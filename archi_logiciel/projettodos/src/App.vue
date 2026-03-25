<script>

import TodoItem from './components/TodoItem.vue';

let data = {
  todos: [{id:1,  title: 'Faire les courses', done: true }, { id:2, title: 'Apprendre REST', done: false }],
  titre: 'Mes tâches',
  newItem: ''
};

export default {

  data() {
    return data;
  },
  methods: {
    afficherItem: function () {
      
        const resp= fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {
          headers: {
            'Content-Type': 'application/json'
          },
          method: 'GET',
          
        })
        .then(res => res.json())
        .then(data =>{
          console.log(data)
          this.todos= data.questionnaires;
          
        });
    },

      

      addItem: function () {
        
        let text = this.newItem.trim();
        if(text.length === 0) {
          return;
        }
        if (text) {
        fetch("http://localhost:5000/quiz/api/v1.0/questionnaires", {
          headers: {
            'Content-Type': 'application/json'
          },
          method: 'POST',
          body: JSON.stringify({nom: text, done: false})
        })
        .then(res => res.json())
        .then(data =>{

          const nouveau = data['questionnaire crée '];

          if (nouveau && nouveau.id) {
            this.todos.push(nouveau);
            this.newItem="";

          }
          else{
            this.afficherItem();
          }
        
        });
      
        }

      },


      supprItem : function(todo) {
        console.log("remove task "+ todo.nom);

        fetch("http://localhost:5000/quiz/api/v1.0/questionnaires/"+todo.id, {
          headers: {
            'Content-Type': 'application/json'
          },
          method: 'DELETE',
        }).then(res =>{
          if (res.ok) {
                this.todos = this.todos.filter(item => item.id !== todo.id);
            }
        })
      },


      modifItem : function($event) {
        console.log("MODIFIER task "+ $event.todo);
        console.log($event)
        console.log($event.todo.uri)

        const url = $event.todo.uri || `http://localhost:5000/quiz/api/v1.0/questionnaires/${$event.todo.id}`;

        fetch(url, {
          headers: {
            'Content-Type': 'application/json'
          },
          method: 'PUT',
          body: JSON.stringify({
          nom: $event.change})
        }).then(res =>{
          if (res.ok) {
                $event.todo.nom = $event.change; //nom?
            }
        })

      },

      checkItem : function($event) {
        let index = this.todos.indexOf($event.todo);
        this.todos.at(index).text = $event.change
        
      },
    

    },
    mounted() {
      fetch("http://localhost:5000/quiz/api/v1.0/questionnaires")
        .then(response => response.json())
        .then(json => {
          console.log("Mounted");
          console.log(json.questionnaires);
          this.todos = json.questionnaires;
        });
    },
    components: {TodoItem}

}

</script>


<template>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
 <div  class="container">
<h2>{{ titre }}</h2>
  <ol>
    <!-- <li v-for= "todo in todos" 
        v-bind:class="{ 'alert alert-success': todo.checked }">
      <div class="checkbox">
        <label>
          <input type="checkbox" v-model="todo.checked"> {{ todo.text }}
        </label>
      </div>
    </li> -->

    <TodoItem v-for="item of todos"
      :key="item.id"
      :todo="item"
      @remove="supprItem"
      @modifier="modifItem"  
      >
    
    </TodoItem>
  </ol>
  <div class="input-group">
    <input v-model="newItem" 
     @keyup.enter="addItem" 
     placeholder="Ajouter une tache à la liste" 
    type="text"
    class="form-control">
    <span class="input-group-btn">
      <button @click="addItem" 
      class="btn btn-default" 
      type="button">Ajouter</button>
    </span>
  </div>
</div>
</template>

