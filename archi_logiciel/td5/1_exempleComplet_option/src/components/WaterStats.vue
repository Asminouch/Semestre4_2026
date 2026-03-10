<template>
  <div class="stats-card">
    <h3>Consommation actuelle</h3>
    <p class="amount">{{ totalLiters }} Litres</p>
    <p>{{ glassCount }} verres de 250ml</p>
  </div>
</template>

<script>
export default {
  name: 'WaterStats',
  props: {
    glassCount: {
      type: Number,
      required: true // Oblige d'avoir une valeur
    }
  },
//  props: ['glassCount'], // Syntaxe tableau simple, sans vérification de type
  computed: {
    // propriété calculée pour le nombre de litre
    totalLiters() {
      return (this.glassCount * 0.25).toFixed(2);
    }
  }
}
</script>

<style scoped>
.stats-card {
  padding: 20px;
  background: #e3f2fd;
  border-radius: 12px;
  text-align: center;
}
.amount {
  font-size: 2rem;
  font-weight: bold;
  color: #0277bd;
}
</style>