import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

import vSelect from 'vue-select'

import 'vue-select/dist/vue-select.css';

const app = createApp(App)

app.component('VueDatePicker', VueDatePicker);
app.component('v-select', vSelect)

app.mount("#home")
