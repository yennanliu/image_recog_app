<template>
  <div id="app">
    <header>
      <h1>Image Recognition App</h1>
      <p>Upload an image to identify objects within it</p>
    </header>
    
    <main>
      <UploadImage 
        @recognize="handleRecognize"
        ref="uploadComponent"
      />
      <RecognitionResult 
        :predictions="predictions"
      />
    </main>
  </div>
</template>

<script>
import UploadImage from './components/UploadImage.vue'
import RecognitionResult from './components/RecognitionResult.vue'
// import axios from 'axios'

export default {
  name: 'App',
  components: {
    UploadImage,
    RecognitionResult
  },
  data() {
    return {
      predictions: []
    }
  },
  methods: {
    async handleRecognize() {
      try {
        // For now, we'll simulate the recognition with mock data
        // This will be replaced with actual API call later
        await new Promise(resolve => setTimeout(resolve, 1500))
        
        this.predictions = [
          { label: 'Sample Object 1', confidence: 0.95 },
          { label: 'Sample Object 2', confidence: 0.85 },
          { label: 'Sample Object 3', confidence: 0.70 }
        ]
        
        // Reset the processing state
        this.$refs.uploadComponent.isProcessing = false
        
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
        console.error('Recognition failed:', error)
        alert('Failed to process the image. Please try again.')
        this.$refs.uploadComponent.isProcessing = false
      }
    }
  }
}
</script>

<style>
#app {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
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

main {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
