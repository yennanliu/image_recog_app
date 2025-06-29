<template>
  <div class="results-container" v-if="predictions.length">
    <div class="results-list">
      <div v-for="(prediction, index) in predictions" :key="index" class="result-item">
        <span class="label">{{ prediction.label }}</span>
        <div class="confidence-bar">
          <div 
            class="confidence-fill" 
            :style="{ width: prediction.confidence * 100 + '%' }"
          ></div>
          <span class="confidence-text">{{ (prediction.confidence * 100).toFixed(1) }}%</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecognitionResult',
  props: {
    predictions: {
      type: Array,
      default: () => []
    }
  }
}
</script>

<style scoped>
.results-container {
  width: 100%;
  margin: 0 auto;
}

.results-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.result-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.label {
  min-width: 100px;
  font-weight: 600;
  color: #333;
  font-size: 0.9em;
}

.confidence-bar {
  flex-grow: 1;
  height: 20px;
  background: #e0e0e0;
  border-radius: 10px;
  position: relative;
  overflow: hidden;
}

.confidence-fill {
  height: 100%;
  background: #4CAF50;
  transition: width 0.3s ease;
}

.confidence-text {
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translateY(-50%);
  color: #333;
  font-size: 0.8em;
  font-weight: 600;
}
</style> 