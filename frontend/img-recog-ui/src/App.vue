<template>
  <div id="app">
    <header>
      <h1>Image Recognition App</h1>
      <p>Upload an image to identify objects within it</p>
    </header>
    
    <main class="main-container">
      <div class="upload-section">
        <UploadImage 
          @recognize="handleRecognize" 
          ref="uploadComponent" 
        />
        <RecognitionResult 
          v-if="currentPredictions.length"
          :predictions="currentPredictions"
          class="current-result"
        />
      </div>

      <div class="history-section">
        <div v-if="recognitionHistory.length > 0" class="history-header">
          <h2>Recent Records</h2>
          <button @click="clearHistory" class="clear-button">
            Clear History
          </button>
        </div>
        <div class="recognition-history">
          <div
            v-for="(result, index) in recognitionHistory"
            :key="index"
            class="history-item"
          >
            <div class="history-item-content">
              <div class="history-thumbnail">
                <img :src="result.imageUrl" alt="Uploaded image" />
              </div>
              <div class="history-details">
                <div class="history-timestamp">{{ result.timestamp }}</div>
                <div class="top-prediction" v-if="result.predictions[0]">
                  <span class="prediction-label">{{ result.predictions[0].label }}</span>
                  <span class="prediction-confidence">
                    {{ (result.predictions[0].confidence * 100).toFixed(1) }}%
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import UploadImage from "./components/UploadImage.vue";
import RecognitionResult from "./components/RecognitionResult.vue";
// import axios from 'axios'

export default {
  name: "App",
  components: {
    UploadImage,
    RecognitionResult,
  },
  data() {
    return {
      currentPredictions: [],
      recognitionHistory: [],
    };
  },
  methods: {
    async handleRecognize(file) {
      try {
        // For now, we'll simulate the recognition with mock data
        // This will be replaced with actual API call later
        await new Promise((resolve) => setTimeout(resolve, 1500));

        const newPredictions = [
          { label: "Sample Object 1", confidence: 0.95 },
          { label: "Sample Object 2", confidence: 0.85 },
          { label: "Sample Object 3", confidence: 0.7 },
        ];

        // Create thumbnail URL from the uploaded file
        const thumbnailUrl = await this.createThumbnail(file);

        // Set current predictions
        this.currentPredictions = newPredictions;

        // Add new predictions to history
        this.recognitionHistory.unshift({
          timestamp: new Date().toLocaleString(),
          predictions: newPredictions,
          imageUrl: thumbnailUrl,
        });

        // Keep only the last 5 results
        if (this.recognitionHistory.length > 5) {
          this.recognitionHistory = this.recognitionHistory.slice(0, 5);
        }

        // Reset the processing state
        this.$refs.uploadComponent.isProcessing = false;

        /* When backend is ready, uncomment this code:
        const formData = new FormData()
        formData.append('file', file)
        
        const response = await axios.post('/recognize', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        
        this.predictions = response.data.predictions
        */
      } catch (error) {
        console.error("Recognition failed:", error);
        alert("Failed to process the image. Please try again.");
        this.$refs.uploadComponent.isProcessing = false;
      }
    },
    clearHistory() {
      this.recognitionHistory = [];
      this.currentPredictions = [];
    },
    async createThumbnail(file) {
      return new Promise((resolve) => {
        const reader = new FileReader();
        reader.onload = (e) => {
          const img = new Image();
          img.onload = () => {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');
            
            // Set thumbnail size
            const maxSize = 100;
            let width = img.width;
            let height = img.height;
            
            if (width > height) {
              if (width > maxSize) {
                height *= maxSize / width;
                width = maxSize;
              }
            } else {
              if (height > maxSize) {
                width *= maxSize / height;
                height = maxSize;
              }
            }
            
            canvas.width = width;
            canvas.height = height;
            
            ctx.drawImage(img, 0, 0, width, height);
            resolve(canvas.toDataURL('image/jpeg', 0.7));
          };
          img.src = e.target.result;
        };
        reader.readAsDataURL(file);
      });
    }
  },
};
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: 0;
  padding: 20px;
  min-height: 100vh;
  background: #f8f9fa;
}

header {
  text-align: center;
  margin-bottom: 40px;
}

h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

header p {
  color: #666;
  margin: 0;
}

.main-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 30px;
}

.upload-section {
  flex: 1;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.history-section {
  width: 300px;
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.current-result {
  margin-top: 20px;
}

.history-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.history-header h2 {
  margin: 0;
  font-size: 1.2em;
  color: #2c3e50;
}

.clear-button {
  padding: 6px 12px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 12px;
  transition: background-color 0.3s;
}

.clear-button:hover {
  background-color: #c82333;
}

.recognition-history {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.history-item {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
}

.history-item-content {
  display: flex;
  gap: 12px;
  padding: 10px;
}

.history-thumbnail {
  width: 60px;
  height: 60px;
  border-radius: 4px;
  overflow: hidden;
  flex-shrink: 0;
}

.history-thumbnail img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.history-details {
  flex: 1;
  min-width: 0;
}

.history-timestamp {
  font-size: 0.8em;
  color: #666;
  margin-bottom: 4px;
}

.top-prediction {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.9em;
}

.prediction-label {
  font-weight: 600;
  color: #2c3e50;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.prediction-confidence {
  color: #4CAF50;
  font-weight: 600;
  margin-left: 8px;
}

@media (max-width: 768px) {
  .main-container {
    flex-direction: column;
  }
  
  .history-section {
    width: auto;
  }
}
</style>