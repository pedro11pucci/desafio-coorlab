<template>
    <div class="option">
        <div class="company">
            <div class="left-wrapper">
                <div class="icon">
                    
                </div>
                <div class="informations">
                    <p class="company-label">
                        <slot name="company-label"></slot>
                    </p>
                    <p class="seat">
                        <slot name="seat"></slot> 
                    </p>
                    <p class="duration">
                        Tempo estimado: 
                        <slot name="duration"></slot>
                    </p>
                </div>
            </div>
            <div class="price">
                <p class="price-label">Preço</p>
                <p class="price-value">
                    <slot name="price"></slot>
                </p>
            </div>
        </div>
    </div>
</template>
<style scoped>
.option{
    
    .company{
        display: flex;
        height: 12vh;
        margin-top: 4%;
        
        .left-wrapper{
            display: contents;
            border-collapse: separate;
            
            .icon{
                background-color: #03a7b3;
                width: 17%;
                border-top-left-radius: 10px;
                border-bottom-left-radius: 10px;
            }
            
            .informations{
                background-color: #e1e1e1;
                width: 52%;
                padding-left: 5%;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
                
                .company-label{
                    font-weight: bold;
                    font-size: 19px;
                    margin-top: 4%;
                }
                
                .seat{
                    font-size: 17px;
                }
                
                .duration{
                    margin-bottom: 5%;
                    font-size: 17px;
                }
            }
        }
    }
        
        .price{
            margin-left: 4%;
            width: 23%;
            border-radius: 10px;
            background-color: #e1e1e1;

            .price-label{
                margin-top: 15%;
                margin-left: 10%;
                font-size: 17px;
                font-weight: bold;
            }

            .price-value{
                margin-left: 15%;
                font-size: 16px;
            }
    }
}

.option:hover{
    transform: scale(1.02);
    transition: 0.2s;
    cursor: pointer;
}

</style>