<template>
  <div class="upload-container">
    <div class="upload-box" @click="triggerFileInput" @dragover.prevent @drop.prevent="handleDrop">
      <input 
        type="file" 
        ref="fileInput" 
        @change="handleFileSelect" 
        accept="image/*" 
        style="display: none"
      >
      <div v-if="!imagePreview" class="upload-placeholder">
        <i class="upload-icon">📸</i>
        <p>Click or drag an image here to upload</p>
      </div>
      <div v-else class="preview-container">
        <img :src="imagePreview" alt="Preview" class="image-preview">
      </div>
    </div>
    <button 
      v-if="imagePreview" 
      @click="handleRecognize" 
      :disabled="isProcessing" 
      class="recognize-button"
    >
      {{ isProcessing ? 'Processing...' : 'Recognize Image' }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'UploadImage',
  data() {
    return {
      imageFile: null,
      imagePreview: null,
      isProcessing: false
    }
  },
  methods: {
    triggerFileInput() {
      this.$refs.fileInput.click()
    },
    handleFileSelect(event) {
      const file = event.target.files[0]
      if (file) {
        this.processSelectedFile(file)
      }
    },
    handleDrop(event) {
      const file = event.dataTransfer.files[0]
      if (file && file.type.startsWith('image/')) {
        this.processSelectedFile(file)
      }
    },
    processSelectedFile(file) {
      this.imageFile = file
      const reader = new FileReader()
      reader.onload = (e) => {
        this.imagePreview = e.target.result
      }
      reader.readAsDataURL(file)
    },
    handleRecognize() {
      if (!this.imageFile) return
      
      this.isProcessing = true
      // Emit event to parent component
      this.$emit('recognize', this.imageFile)
    },
    reset() {
      this.imageFile = null
      this.imagePreview = null
      this.isProcessing = false
    }
  }
}
</script>

<style scoped>
.upload-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  max-width: 500px;
  margin: 0 auto;
}

.upload-box {
  width: 100%;
  height: 300px;
  border: 2px dashed #ccc;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: border-color 0.3s;
}

.upload-box:hover {
  border-color: #666;
}

.upload-placeholder {
  text-align: center;
  color: #666;
}

.upload-icon {
  font-size: 48px;
  margin-bottom: 10px;
}

.preview-container {
  width: 100%;
  height: 100%;
  padding: 10px;
}

.image-preview {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.recognize-button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.recognize-button:hover:not(:disabled) {
  background-color: #45a049;
}

.recognize-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style> 