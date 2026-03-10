<script>
export default{
    props: {
        todo : Object
    },
    methods:{
        suppr : function() {
        this.$emit('remove',{id:this.todo.id});
        }
    },
    emits : ['remove']
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
        </label>
    </div>




</template>