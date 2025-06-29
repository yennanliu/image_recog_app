<template>
  <div class="results-container" v-if="predictions.length">
    <h3>Recognition Results</h3>
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
  max-width: 500px;
  margin: 20px auto;
  padding: 20px;
  background: #f5f5f5;
  border-radius: 8px;
}

h3 {
  margin-top: 0;
  color: #333;
  text-align: center;
}

.results-list {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.result-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.label {
  min-width: 100px;
  font-weight: bold;
  color: #333;
}

.confidence-bar {
  flex-grow: 1;
  height: 24px;
  background: #e0e0e0;
  border-radius: 12px;
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
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: #333;
  font-size: 14px;
  font-weight: bold;
}
</style> 