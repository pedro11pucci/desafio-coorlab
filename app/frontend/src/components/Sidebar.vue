<script setup>
import SidebarItem from './SidebarItem.vue'
</script>

<template>
    <div class="sidebar">
        <img alt="CB logo" class="logo" src="../assets/logo.png" />
        <div class="items">
            <SidebarItem>
                <template #heading>Calculadora de Viagem</template>
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

    .items{
        margin-top: 13%;
    }

    img{
        width: 58%;
        margin-top: 9%;
        margin-left: 7%;
    }

}

</style>