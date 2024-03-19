import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Home from './Home.vue'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoCalculator } from "oh-vue-icons/icons";

import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'


const app = createApp(Home)

app.component('VueDatePicker', VueDatePicker);

addIcons(CoCalculator)
app.component("v-icon", OhVueIcon)

app.mount("#home")
