<script setup>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref } from 'vue';

const date = ref(new Date());
const props = defineProps(['format']);
const format = (date) => {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
}

const formData = ref({
    destiny: '',
    date: ''
})

const emits = defineEmits(['search'])
const handleSubmit = () => {
    emits('search', formData.value);
}

</script>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      options: []
    };
  },
  created() {
    axios.get('http://localhost:3000/fetch')
      .then(response => {
        this.options = response.data;
      })
      .catch(error => {
        console.error('Erro ao buscar dados:', error);
      });
  }
};
</script>

<template>
    <div class="calculator-form">
        <form @submit.prevent="handleSubmit">
            <h2>Calcule o Valor da Viagem</h2>
            <div class="input-wrapper">
            <span>Destino</span><br>
            <select class="destiny-select" v-model="formData.destiny">
                <option v-for="option in options" :value="option">{{  option  }}</option>
            </select><br>
            </div>
            <div class="input-wrapper">
                <span>Data</span><br>
                <VueDatePicker class="date-picker" v-model="formData.date"
                :enable-time-picker="false"
                :format="format" 
                locale="br" 
                select-text="Selecionar"
                cancel-text="Fechar"
                placeholder="Selecione uma data" /><br>
            </div>
            <input class="btn-submit" type="submit" value="Buscar" />
        </form>
    </div>
</template>

<style scoped>
.calculator-form{
    margin-left: 5%;
    margin-top: 5%;
    padding-top: 22%;
    border-radius: 10px;
    width: 21vw;
    height: 27vw;
    background-color: #f2f2f2;

    form {
        margin-left: 8%;

        h2 {
            font-size: 18px;
            font-weight: bold;
            margin-left: 4%;
        }

        .input-wrapper{
            margin-top: 6%;

            select {
                width: 90%;
                font-size: 16px;
                height: 4vh;
                border-radius: 5px;
                border-color: #ddd;
                background-color: #fff;
                color: #212121;
            }

            span{
                font-size: 14px;
            }

            .date-picker{
                width: 90%;
                margin-top: 2%;
            }
        }
    }

    .btn-submit{
        background-color: #00a8b3;
        width: 17vh;
        height: 1.7vw;
        margin-top: 6%;
        margin-left: 23%;
        border-radius: 6px;
        border-color: #75d6dd;
    }

    .btn-submit:hover{
        background-color: #09dae9;
        transition: 0.3s;
    }
}
</style>