<script>
export default{
    data(){
        return{
            changment: "",
            check: ""
        }
    },
    props: {
        todo : Object
    },
    methods:{
        suppr : function() {
        this.$emit('remove',{id:this.todo.id});
        },
        modif : function() {
        this.$emit('modifier',{todo:this.todo, change: this.changment});
        this.changment= ""
        },

        fini : function() {
        this.$emit('tache_f',{todo:this.todo, change: this.changment});
        this.changment= ""
        }
    },
    emits : ['remove', 'modifier', "tache_f"]
}
</script>

<template>
    <!-- // Mettre le code pour afficher une tache définie par la prop todo -->

    <div class="checkbox" v-bind:class="{ 'alert alert-success': todo.checked }">
        <label>
          <input type="checkbox" v-model="todo.checked"> {{ todo.text }}

        <input type="button"
        class="btn btn-danger"
        value="Supprimer"
        @click="suppr">


    <input v-model="changment" @keyup.enter="" placeholder="Modif" type="text"
    class="form-control">
        <input type="button"
        class="btn btn-default"
        value="Modifier"
        @click="modif">
        </label>
    </div>




</template>