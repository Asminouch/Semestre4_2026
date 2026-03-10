<template>
  <div class="progress-container">
    <div class="progress-bar-background">
      <div 
        class="progress-bar-fill" 
        :style="{ width: progressPercentage + '%' }"
      ></div>
    </div>
    <p class="progress-text">{{ valeurActuelle }} / {{ objectif }} verres</p>
  </div>
</template>

<script>
export default {
  name: 'ProgressBar',
  props: {
    valeurActuelle: {
      type: Number,
      required: true
    },
    objectif: {
      type: Number,
      required: true
    }
  },
  computed: {
    // Calcule le pourcentage, plafonné à 100%
    progressPercentage() {
      if (this.objectif === 0) return 0;
      const percentage = (this.valeurActuelle / this.objectif) * 100;
      return Math.min(percentage, 100);
    }
  }
}
</script>

<style scoped>
.progress-container {
  width: 100%;
  max-width: 300px;
  margin: 20px 0;
  text-align: center;
}

.progress-bar-background {
  width: 100%;
  height: 20px;
  background-color: #e0e0e0;
  border-radius: 10px;
  overflow: hidden; /* Pour que le remplissage reste dans les bords arrondis */
  box-shadow: inset 0 1px 3px rgba(0,0,0,0.2);
}

.progress-bar-fill {
  height: 100%;
  background-color: #2196f3; /* Bleu */
  transition: width 0.3s ease-in-out; /* Animation douce */
}

.progress-text {
  margin-top: 5px;
  font-size: 0.9rem;
  color: #555;
}
</style>