<template>
  <div class="chat-container">
    <div class="chat-header">
      <h2>DBA knowledge Base</h2>
    </div>
    <div ref="scrollContainer" class="chat-messages">
      <div v-for="(message, index) in messages" :key="index" class="message" :class="{ 'user-message': message.type === 'user', 'bot-message': message.type === 'bot' }">
        <div class="message-content" v-html="message.content"></div>
      </div>
    </div>
    <div class="chat-input-container">
      <input v-model="userInput" @keydown.enter="sendMessage" placeholder="Type your message..." class="chat-input" />
      <button @click="sendMessage" class="send-button" type="button">Send</button>
    </div>
    <div class="upload-file">
      <a href="#" @click.prevent="upload">upload file</a>
    </div>  
  </div>

</template>

<script>
import { ref } from 'vue';
import {useRouter} from 'vue-router'

export default {
  name: 'ChatPage',
  setup() {
    const messages = ref([
      { type: 'bot', content: '【机器人】专业DBA小助手，有什么要咨询的吗?' }
    ]);
    const userInput = ref('');
    const router = useRouter();

  


    const sendMessage = async () => {
      if (userInput.value.trim() !== '') {
        messages.value.push({ type: 'user', content: userInput.value });
        // Simulate bot response (replace with actual logic in real app)
        await fetch('http://127.0.0.1:8866/RAGTalk/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body:JSON.stringify({
                            content:userInput.value
                        })    
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

        const comment =  json.comment;
     messages.value.push({ type: 'bot', content:comment });
 
    });
           
        userInput.value = '';
      }
    };

    const upload = () => {
         router.push('/upload');
    };

    return {
      messages,
      userInput,
      sendMessage,
      upload
    };
  }
};
</script>

<style scoped>
.chat-container {
  max-width: 800px;
  margin: auto;
  background-color: #f0f0f0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

.chat-header {
  background-color: #550088;
  color: white;
  padding: 30px;
  text-align: center;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
}

.chat-messages {
  max-height: 400px;
  overflow-y: auto;
  text-align:left;
}

.message {
  max-width: 80%;
  margin-bottom: 50px;
  padding: 10px;
  border-radius: 8px;
  word-wrap: break-word;
  transition: background-color 0.3s ease;
}

.user-message {
  background-color: #550088;
  color: white;
  align-self: flex-end;
}

.bot-message {
  background-color: #FFD700;
  color: #333;
  font-size:12px;
}


.message-content {
 word-wrap: break-word;
}

.chat-input-container {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #fff;
}

.chat-input {
  flex: 1;
  padding: 10px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  outline: none;
}

.send-button {
  padding: 10px 20px;
  background-color: #C63300;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.send-button:hover {
  background-color: #0056b3;
}

.upload-file {
text-align:right;
}

</style>
