# Aplicativo de Previsão do Tempo

Este aplicativo é uma interface gráfica simples construída com Tkinter em Python, que permite ao usuário buscar dados de previsão do tempo para uma cidade específica. Os dados são obtidos através da API do OpenWeatherMap.

## Funcionalidades

- **Buscar Dados do Tempo**: Permite ao usuário inserir o nome de uma cidade e buscar os dados atuais do tempo para essa localidade.
- **Exibição dos Dados**: Os dados do tempo, incluindo temperatura, umidade, pressão, velocidade do vento e descrição geral do tempo, são exibidos na interface.
- **Salvar Dados**: O aplicativo também oferece a funcionalidade de salvar os dados do tempo obtidos em um arquivo de texto para referência futura.

## Como Usar

1. Certifique-se de ter Python e pip instalados em seu sistema.
2. Instale as dependências necessárias usando o comando `pip install requests`.
3. Execute o script `clima.py` para iniciar o aplicativo.
4. Insira o nome da cidade desejada no campo de entrada e clique em "Buscar Dados do Tempo".
5. Os dados do tempo serão exibidos na interface, e você pode optar por salvá-los.

## Dependências

- Python 3.x
- Tkinter (já incluído com Python)
- Requests: Para realizar solicitações HTTP à API do OpenWeatherMap.

## Configuração da API

Este aplicativo usa a API do OpenWeatherMap para buscar dados do tempo. Você precisará de uma chave de API válida, que pode ser obtida gratuitamente registrando-se no site do OpenWeatherMap.

Após obter sua chave de API, substitua o valor da variável `API_KEY` no script `clima.py` pela sua chave.

## Contribuições

Contribuições para o projeto são bem-vindas. Sinta-se à vontade para clonar, modificar e enviar pull requests.
