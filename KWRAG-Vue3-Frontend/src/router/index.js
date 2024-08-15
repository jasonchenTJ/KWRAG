// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import chat from '.././components/ChatPage.vue'
import logon from '.././components/logonPage.vue'
import upload from '.././components/UploadPage.vue'

const routes = [
  { path: '/chat', component: chat },
  { path: '/logon', component: logon },
  { path: '/upload', component: upload },
  { path: '/', component: logon }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
