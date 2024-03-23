<script>
import TruckDeliveryIcon from 'vue-material-design-icons/AlertBoxOutline.vue';
import 'vue-material-design-icons/styles.css';

export default {
    name: 'Modal',
    props: {
        visible: Boolean
    },
    data () {
        return {
            openClose: this.visible
        }
    },
    methods: {
        openCloseFun () {
            this.openClose = !this.openClose
        }
    },
    watch: {
        visible: function (newVal, oldVal) {
            this.openClose = newVal
            console.log('new ' + newVal + '==' + oldVal)
        }
    },
    components: {
        TruckDeliveryIcon
    }
}

</script>

<template>
    <div v-if="openClose" class="modal fade show" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"
        role="dialog">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-body">
                    <h1 class="icon"><truck-delivery-icon/></h1>
                    <h1><slot></slot></h1>
                </div>
                <button type="button" class="btn" @click="openCloseFun()">Fechar</button>
            </div>
        </div>
    </div>
</template>


<style scoped>
@import "bootstrap/dist/css/bootstrap.min.css";
@import "bootstrap";
@import "bootstrap-icons/font/bootstrap-icons.css";

.modal {
    display: block;
    padding-top: 18%;
    padding-left: 10%;
    background-color: rgba(0, 0, 0, 0.2);

    .icon{
        color: #336480;
        font-size: 70px; 
        margin-top: 6%;
    }

    h1{
        font-size: 24px;
        text-align: center
    }

    button{
        width: 40%;
        margin-left: 30%;
        margin-bottom: 6%;
        background-color: #00a8b3;
        font-weight: bold
    }

    button:hover{
        background-color: #09dae9;
    }
}
</style>