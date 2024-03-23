<script setup>
import CalculatorForm from './CalculatorForm.vue'
import TripOption from './TripOption.vue'
import axios from 'axios';
import { ref } from 'vue';

const tripResult = ref(null);

const calculateTrip = (data) => {
    axios.get(`http://localhost:3000/${data.destiny}`).then((response) => {
        data = response.data
        tripResult.value = null
        tripResult.value = data
    })
};
</script>
<script>
import TruckDeliveryIcon from 'vue-material-design-icons/TruckDeliveryOutline.vue';
import HandCoinIcon from 'vue-material-design-icons/HandCoinOutline.vue';
import ClockCheckOutlineIcon from 'vue-material-design-icons/ClockCheckOutline.vue';
import 'vue-material-design-icons/styles.css';

components: {
  TruckDeliveryIcon;
  HandCoinIcon;
  ClockCheckOutlineIcon
}
</script>

<template>
    <div class="calculator-wrapper">
        <div class="calculator-header">
            <h1><truck-delivery-icon style="font-size: 28px;"/> Calculadora de Viagem</h1>
        </div>
        <div class="calculator-main">
            <div class="calculator-form">
                <CalculatorForm :format="format" @search="calculateTrip" />
            </div>
            <div class="calculator-results">
                <h2 class="no-result" v-if="!tripResult">Nenhum dado selecionado.</h2>
                <div class="results" v-if="tripResult">
                    <h2 class="result">Estas são as melhores alternativas de viagem <br> para a data selecionada</h2>
                    <TripOption>
                        <template #icon><hand-coin-icon/></template>
                        <template #company-label>{{tripResult.comfort.name}}</template>
                        <template #duration>{{tripResult.comfort.duration}}</template>
                        <template #seat>Leito: {{tripResult.comfort.seat}} (Completo)</template>
                        <template #price>{{tripResult.comfort.price_confort}}</template>
                    </TripOption>
                    <TripOption>
                        <template #icon><clock-check-outline-icon/></template>
                        <template #company-label>{{tripResult.econ.name}}</template>
                        <template #duration>{{tripResult.econ.duration}}</template>
                        <template #seat>Assento: {{tripResult.econ.seat}} (convencional)</template>
                        <template #price>{{tripResult.econ.price_econ}}</template>
                    </TripOption>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
.calculator-wrapper {
    width: 70%;
    margin-top: 6%;
    margin-left: 11.4%;

    .calculator-header {
        background-color: #292f3f;
        color: #f3f6fb;
        height: 6.4vh;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;

        h1 {
            margin-left: 3.5%;
            padding-top: .8%;
            font-size: 23px;
            color: #f7faff;
        }
    }

    .calculator-main {
        display: flex;
        background-color: #fefefe;
        padding-bottom: 2%;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;

        .calculator-results {
            width: 39vw;
            margin-left: 4%;

            .no-result {
                margin-top: 37%;
                margin-left: 31%;
            }

            .result {
                margin-top: 15%;
            }
        }
    }
}
</style>