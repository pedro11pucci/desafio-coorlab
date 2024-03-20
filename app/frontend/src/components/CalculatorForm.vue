<script setup>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref, defineProps, defineEmits } from 'vue';

const date = ref(new Date());
const props = defineProps(['format']);
const format = (date) => {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
}

const emits = defineEmits(['search'])
const onCalculate = () => {
    emits('search');
}
</script>

<template>
    <div class="calculator-form">
        <form @submit.prevent="calculateTrip">
            <h2>Calcule o Valor da Viagem</h2>
            <div class="input-wrapper">
            <span>Destino</span><br>
            <select class="destiny-select" placeholder="Selecione o destino">
                <option value="" disabled selected hidden>Selecione o destino</option>
                <option value="campinas">Campinas</option>
                <option value="sao-paulo">São Paulo</option>
                <option value="santo-andre">Santo André</option>
            </select><br>
            </div>
            <div class="input-wrapper">
                <span>Data</span><br>
                <VueDatePicker class="date-picker" v-model="date"
                :enable-time-picker="false"
                :format="format" 
                locale="br" 
                select-text="Selecionar"
                cancel-text="Fechar"
                placeholder="Selecione uma data" /><br>
            </div>
            <input class="btn-submit" type="submit" value="Buscar" @click="onCalculate" />
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