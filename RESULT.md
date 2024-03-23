# Resultado - Desáfio CoorLab

## Objetivo
O objetivo do desafio era criar um projeto seguindo os requisitos de tecnologias, de cenário e histórias de usuário e o protótipo fornecido pela CoorLab

## Tecnologias Utilizadas
Os requisitos da CoorLab são o framework Vue.js para a implementação do frontend e a linguagem Python para a implementação do backend.
<h3>A lista completa de tecnologias utilizadas no desafio é:</h4>
<ul>
    <li>Python</li>
    <li>Flask</li>
    <li>Node.js</li>
    <li>Vite</li>
    <li>Vue.js</li>
    <li>vue-material-design-icons</li>
    <li>vue-select</li>
    <li>vue-datepicker</li>
    <li>Bootstrap</li>
    <li>Tailwind CSS</li>
    <li>Axios</li>
</ul>

## Implementação
Foi utilizada a ferramenta Vite para criar o ambiente de desenvolvimento frontend com Vue.js e o framework Flask para a API REST.<br><br>
Foi criado um componente Sidebar e, pensando na escalabilidade, um componente SidebarItem, para se ter uma forma fácil de adicionar vários itens a Sidebar, no caso de crescimento da aplicação.<br>

Depois, foi criado o componente Calculator, que é onde a maior parte da funcionalidade está. O componente Calculator é responsável por receber os dados inseridos no componente CalculatorForm e enviá-los para o servidor através de um endpoint da API REST.<br>

O componente CalculatorForm possuí um formulário que utiliza as bibliotecas vue-select e vue-datepicker para criar inputs onde o usuário deve inserir o seu destino e a data de sua viagem. Caso o usuário não insira todos os dados necessários, um modal criado com o Bootstrap aparece na tela informando-o de que ele deve inserir todos os valores antes de fazer a cotação.<br>
A lista de destinos disponíveis é adquirida através de uma requisição feita para o endpoint /fetch da API REST, utilizando o Axios, que lê o JSON do banco de dados, pega todas as cidades das viagens disponíveis, insere-as em uma lista e retorna como um JSON para serem inseridas como opções do select.<br>

Após validar o formulário, os dados são enviados para o backend através de um endpoint da API REST, passando a cidade de destino do usuário como um parâmetro de rota.<br>
No servidor Flask, a rota irá receber o nome da cidade, ler o JSON do banco de dados e adquirir todas as viagens disponíveis para aquele destino, depois ele irá buscar  pela viagem mais confortável e a mais econômica, colocará as duas viagens em uma lista e as retornará para o cliente.<br>

No componente Calculator, após ser servido pela API REST as viagens disponíveis, ele irá instanciar dois componentes TripOption, que exibem ao usuário o nome da empresa, o número do assento, a duração e o preço das duas viagens cotadas para o destino inserido pelo usuário.

## Considerações finais
A solução implementada cumpre todos os requisitos da CoorLab, tanto de tecnologias quanto de funcionalidade, cenário e histórias de usuário, segue o protótipo fornecido e é feita pensando na escalabilidade do projeto, visto a organização dos componentes do Vue.js e da API REST do backend de Python.