<script setup>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import Modal from './Modal.vue'
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

const modalRef = ref()
const emits = defineEmits(['search'])
const handleSubmit = () => {
    if (!formData.value.destiny || !formData.value.date) {
        modalRef.value.openCloseFun()
        return
    }
    console.log(formData.value.destiny);
    emits('search', formData.value);
}

</script>

<script>
import axios from 'axios';
import Modal from './Modal.vue'
import HandCoinIcon from 'vue-material-design-icons/HandCoinOutline.vue';
import 'vue-material-design-icons/styles.css';

export default {
    data () {
        return {
            options: [],
            placeholder: "Insira"
        };
    },
    created () {
        axios.get('http://localhost:3000/fetch')
            .then(response => {
                this.options = response.data;
            })
            .catch(error => {
                console.error('Erro ao buscar dados:', error);
            });
    },
    components: {
        Modal,
        HandCoinIcon
    }
};
</script>

<template>
    <div class="calculator-form">
        <form @submit.prevent="handleSubmit">
            <h2><hand-coin-icon style="font-size: 30px;" /> Calcule o Valor da Viagem</h2>
            <div class="input-wrapper">
                <span>Destino</span><br>
                <v-select class="destiny-select" label="city" placeholder="Selecione o destino" :options="options"
                    v-model="formData.destiny"></v-select>
            </div>
            <div class="input-wrapper">
                <span>Data</span><br>
                <VueDatePicker class="date-picker" v-model="formData.date" :enable-time-picker="false" :format="format"
                    locale="br" select-text="Selecionar" cancel-text="Fechar" placeholder="Selecione uma data" /><br>
            </div>
            <input class="btn-submit" type="submit" value="Buscar" />
        </form>
    </div>
    <Modal ref="modalRef" :visible="false">Insira os valores para realizar<br> a cotação.</Modal>
</template>

<style scoped>
.calculator-form {
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
            font-size: 20px;
            font-weight: bold;
            margin-left: 6%;
        }

        .input-wrapper {
            margin-top: 6%;

            .destiny-select {
                width: 90%;
                font-size: 16px;
                height: 4vh;
                border-radius: 5px;
                background-color: #fff;
                color: #212121;
            }

            span {
                font-size: 14px;
            }

            .date-picker {
                width: 90%;
                margin-top: 2%;
            }
        }
    }

    .btn-submit {
        background-color: #00a8b3;
        width: 17vh;
        height: 1.7vw;
        margin-top: 6%;
        margin-left: 23%;
        border-radius: 6px;
        border-color: #75d6dd;
    }

    .btn-submit:hover {
        background-color: #09dae9;
        transition: 0.3s;
    }
}
</style>