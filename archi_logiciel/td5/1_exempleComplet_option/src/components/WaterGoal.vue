<template>
  <div class="goal-container">
    <button @click="handleAdd" class="btn-add">
      + Ajouter un verre
    </button>
    <button @click="handleReset" class="btn-reset">
      Réinitialiser
    </button>
  </div>
</template>

<script>
export default {
  name: 'WaterGoal',
  // Déclaration explicite des événements 
  emits: ['add-glass', 'reset'],
  methods: {
    handleAdd() {
      this.$emit('add-glass');
    },
    handleReset() {
      this.$emit('reset');
    }
  }
}
</script>

<style scoped>
.goal-container {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}
.btn-add {
  background: #4caf50;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
}
.btn-reset {
  background: #ef5350;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  cursor: pointer;
}
</style>