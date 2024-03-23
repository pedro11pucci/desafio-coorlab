<script setup>
import SidebarItem from './SidebarItem.vue'
</script>
<script>
import CalculatorIcon from 'vue-material-design-icons/CalculatorVariantOutline.vue';
import 'vue-material-design-icons/styles.css';

components: {
  CalculatorIcon;
}
</script>

<template>
    <div class="sidebar">
        <img alt="CB logo" class="logo" src="../assets/logo.png" />
        <div class="items">
            <SidebarItem url="calculadora">
                <template #heading><calculator-icon/> Calculadora de Viagem</template>
            </SidebarItem>
        </div>

    </div>
</template>

<style scoped>
.sidebar{
    background-color: #292f3f;
    height: 100vh;
    width: 22%;
    position: static;

    a{
        text-decoration: none
    }

    .items{
        margin-top: 13%;
        margin-right: 10%;
    }

    img{
        width: 58%;
        margin-top: 9%;
        margin-left: 7%;
    }

}

</style>