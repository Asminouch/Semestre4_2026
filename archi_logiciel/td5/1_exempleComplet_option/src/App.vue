<template>
  <main class="app-container">
    <h1>💧 Mon Hydratation</h1>
    
    <WaterStats :glassCount="glasses" />

    <ProgressBar 
      :valeurActuelle="glasses" 
      :objectif="dailyGoal" 
    />

    <WaterGoal 
      @add-glass="incrementGlasses" 
      @reset="resetGlasses" 
    />

    <p v-if="glasses >= dailyGoal" class="congrats">
      🎉 Objectif atteint ! Bravo !
    </p>
  </main>
</template>

<script>
// Imports des trois composants
import WaterStats from './components/WaterStats.vue';
import WaterGoal from './components/WaterGoal.vue';
import ProgressBar from './components/ProgressBar.vue';

export default {
  name: 'App',
  components: {
    WaterStats,
    WaterGoal,
    ProgressBar 
  },
  data() {
    return {
      glasses: 0,
      dailyGoal: 8 // Nous fixons l'objectif à 8 verres
    };
  },
  methods: {
    incrementGlasses() {
      this.glasses++;
    },
    resetGlasses() {
      this.glasses = 0;
    }
  }
}
</script>

<style>
.app-container {
  font-family: sans-serif;
  max-width: 400px;
  margin: 40px auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 16px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.congrats {
  margin-top: 15px;
  color: #4caf50;
  font-weight: bold;
}
</style>