<script>

import TodoItem from './components/TodoItem.vue';

let data = {
  todos: [{id:1,  text: 'Faire les courses', checked: true }, { id:2, text: 'Apprendre REST', checked: false }],
  title: 'Mes tâches',
  newItem: ''
};

export default {

  data() {
    return data;
  },
  methods: {
      addItem: function () {
        let text = this.newItem.trim();
        if (text) {
          this.todos.push({
            id: this.todos.length +1,
            text: text,
            checked: false
          });
          this.newItem = '';
        }

      },

      supprItem : function(todo) {
      this.todos = this.todos.filter(item=> item.id !== todo.id);
      },


      modifItem : function($event) {
        let index = this.todos.indexOf($event.todo);
        this.todos.at(index).text = $event.change

      },
      checkItem : function($event) {
        let index = this.todos.indexOf($event.todo);
        this.todos.at(index).text = $event.change
        
      },
    

    },
    components: {TodoItem}

}
</script>


<template>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
 <div  class="container">
<h2>{{ title }}</h2>
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

