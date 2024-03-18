<script setup>
import Sidebar from './components/Sidebar.vue'
</script>

<template>
    <div class="wrapper">
        <Sidebar />
        <div class="content">
            
        </div>
    </div>
</template>

<style scoped>

.wrapper{
    background-color: #fefefe;
    display: flex;
}

.content {
    background-color: #f7f7f7;
    margin-top: 6%;
    border-top: 1px solid #ccc;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
    width: 100vw;
    flex: 5;
    position: static;
}

</style>