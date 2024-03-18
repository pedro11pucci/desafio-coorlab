import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import Home from './Home.vue'

import { OhVueIcon, addIcons } from "oh-vue-icons";
import { CoCalculator } from "oh-vue-icons/icons";

addIcons(CoCalculator)

const app = createApp(Home)
app.component("v-icon", OhVueIcon)
app.mount("#home")
