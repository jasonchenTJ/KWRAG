<template>
  <div class="login-page">
    <!-- 星空背景 -->
    <div class="background"></div>

    <!-- 登录框 -->
    <div class="login-box">
      <h2>登录</h2>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="username">用户名</label>
          <input type="text" id="username" v-model="username" required> 
        </div>
        <div class="form-group">
          <label for="password">密码</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <button type="submit">登录</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import {useRouter} from 'vue-router'
import { ref } from 'vue';


const router = useRouter();

// 定义响应式数据
const username = ref('');
const password = ref('');

// 登录处理函数
//function login() {
//  console.log('Username:', username.value);
//  console.log('Password:', password.value);
  // 实际项目中，可以使用axios或者fetch API发送POST请求
  // 示例：axios.post('/login', { username: username.value, password: password.value });
   
//}
const login = async () => {
if(username.value.trim() != '' &&  password.value.trim() != ''){
await fetch('http://127.0.0.1:8866/userLogon/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body:JSON.stringify({
                            username:username.value,
                            password:password.value
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
        const result =  json.result;
        if(result == 0){
          router.push('/chat')
        }else{
         console.log("failed!")
        }
    });

}

}
</script>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #000;
  background-image: url('.././image/bg_star_night.jpg');
  background-size: cover;
  background-position: center;
}

.login-box {
  background-color: rgba(255, 255, 255, 0.8);
  padding: 40px;
  width: 300px;
  border-radius: 10px;
  text-align: center;
}

.form-group {
  display: grid;
  grid-template-columns: 60px 1fr; /* 标签列宽固定，输入框列宽自适应 */
  align-items: center; /* 垂直居中对齐 */
  margin-bottom: 15px;
}

label {
  display: block;
  margin-bottom: 5px;
  text-align: left;
}

input[type="text"],
input[type="password"] {
  width: 80%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  font-size: 18px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #45a049;
}
</style>
