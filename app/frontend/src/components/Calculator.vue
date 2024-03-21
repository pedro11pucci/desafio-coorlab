<script setup>
import CalculatorForm from './CalculatorForm.vue'
import TripOption from './TripOption.vue'
import { ref } from 'vue';

const showTripResult = ref(false);

const calculateTrip = () => {
    showTripResult.value = true;
};
</script>

<template>
    <div class="calculator-wrapper">
        <div class="calculator-header">
            <h1>Calculadora de Viagem</h1>
        </div>
        <div class="calculator-main">
            <div class="calculator-form">
                <CalculatorForm :format="format" @search="calculateTrip"/>
            </div>
            <div class="calculator-results">
                <h2 class="no-result" v-if="!showTripResult">Nenhum dado selecionado.</h2>
                <div class="results" v-if="showTripResult">
                    <h2 class="result">Estas são as melhores alternativas de viagem <br> para a data selecionada</h2>
                    <TripOption />
                    <TripOption />
                    
                </div>
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
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        
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
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;

        .calculator-results{
            width: 39vw;
            margin-left: 4%;

            .no-result{
                margin-top: 37%;
                margin-left: 31%;
            }

            .result{
                margin-top: 15%;
            }
        }
    }
}
</style>