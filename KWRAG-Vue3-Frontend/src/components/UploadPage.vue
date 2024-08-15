<template>
  <div class="upload-container">
    <h2>知识库上传文件</h2>
    <form @submit.prevent="handleSubmit" class="upload-form">
      <input
        type="file"
        ref="fileInput"
        @change="handleFileChange"
        accept=".doc,.docx,.xls,.xlsx,.txt,.html"
        class="file-input"
      />
      <button type="submit" class="upload-button">上传文件</button>
      <p v-if="fileName" class="file-info">选择的文件: {{ fileName }}</p>
    </form>
      <h5>文件内容预览:</h5>
   <pre>{{ fileContent }}</pre>
  </div>

 
</template>

<script>
import { ref } from 'vue';
import {useRouter} from 'vue-router';

export default {
  name: 'FileUploadPage',
  setup() {
    const fileInput = ref(null);
    const fileName = ref('');
    const fileContent = ref('');
    const router = useRouter();
  

    const handleFileChange = (event) => {
      if (event.target.files.length > 0) {
        const file = event.target.files[0];
        fileName.value = event.target.files[0].name;
        const reader = new FileReader();
        reader.onload = (e) => {
      // 将文件内容赋值给 fileContent
          fileContent.value = e.target.result;
    };
    
         reader.readAsText(file);
      } else {
        fileName.value = '';
      }
    };

    const handleSubmit = async () => {
      const file = fileInput.value.files[0];
      if (file) {
         const formData = new FormData();
         formData.append('file', file);
         await fetch('http://127.0.0.1:8866/uploadfile/', {
          method: 'POST',
         // headers: {
         //   'Content-Type': 'application/json'
         // },
          body: formData
        }).then(response => {
      // a non-200 response code
      if (!response.ok) {
        // create error instance with HTTP status text
        const error = new Error(response.statusText);
        error.json = response.json();
        throw error;
      }
      return response.json()
    }).then(json=>{
        if(json.comment == 0){
          fileContent.value = '文件上传成功！'
          router.push('/upload');
        }else{
          fileContent.value = '上传失败！'
        }   
    });
      } else {
        alert('请先选择一个文件');
      }
    };

    return {
      fileInput,
      fileName,
      handleFileChange,
      handleSubmit,
      fileContent,
    };
  }
};
</script>

<style scoped>
.upload-container {
  max-width: 800px;
  height: 800px;
  margin: auto;
  overflow-y: auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.upload-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.file-input {
  margin-bottom: 20px;
  align: left;
}

.upload-button {
  align:center;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #6a0dad; /* 紫色按钮 */
  color: white;
  font-size: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.upload-button:hover {
  background-color: #4b0082; /* 按钮悬停时的颜色变化 */
}

.file-info {
  margin-top: 10px;
  color: #333;
}
.preview-file {
  max-height: 600px;
  max-width: 900px;
  overflow-y: auto;
  margin: auto;
  padding: 4px;
  background-color: #C0C0C0;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}
</style>
