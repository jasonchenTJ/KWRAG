import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
//import { apply } from 'core-js/library/fn/reflect'

const app = createApp(App)
app.use(router)
app.mount('#app')
