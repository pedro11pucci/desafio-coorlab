<script setup>
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'
import { ref } from 'vue';

const date = ref(new Date());
const format = (date) => {
  const day = date.getDate();
  const month = date.getMonth() + 1;
  const year = date.getFullYear();

  return `${day}/${month}/${year}`;
}
</script>

<template>
    <div class="calculator-wrapper">
        <div class="calculator-header">
            <h1>Calculadora de Viagem</h1>
        </div>
        <div class="calculator-main">
            <div class="calculator-form">
                <form>
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
                    <input class="btn-submit" type="submit" value="Buscar" />
                </form>
            </div>
            <div class="calculator-results">
                
            </div>
        </div>
    </div>
</template>

<style scoped>
.calculator-wrapper{
    width: 70%;
    margin-top: 6%;
    margin-left: 11.4%;
    
    .calculator-header{
        background-color: #292f3f;
        color: #f3f6fb;
        height: 6.4vh;
        
        h1{
            margin-left: 5%;
            padding-top: 0.8%;
            font-size: 25px;
            color: #f7faff;
        }
    }

    .calculator-main{
        display: flex;
        background-color: #fefefe;
        padding-bottom: 2%;

        .calculator-form{
            margin-left: 2%;
            margin-top: 2.5%;
            padding-top: 8%;
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
                width: 15vh;
                height: 1.7vw;
                margin-top: 6%;
                margin-left: 24%;
                border-radius: 6px;
                border-color: #75d6dd;
            }
        }
    }
}
</style>