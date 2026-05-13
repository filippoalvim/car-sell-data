# Análise de Anúncios de Venda de Carros

Aplicativo web desenvolvido como projeto do Sprint 5 do TripleTen, focado em análise exploratória de dados de anúncios de venda de veículos nos EUA.

## Descrição

Este aplicativo permite explorar visualmente um conjunto de dados com anúncios de venda de carros. O usuário pode gerar gráficos interativos diretamente no navegador, sem precisar de nenhuma instalação local.

## Funcionalidades

- **Histograma de quilometragem**: visualiza a distribuição da quilometragem (odômetro) dos veículos anunciados.
- **Gráfico de dispersão**: exibe a relação entre o preço e a quilometragem dos veículos.
- Gráficos interativos gerados com Plotly Express.
- Interface simples com caixas de seleção para ativar cada visualização.

## Tecnologias utilizadas

- Python
- Pandas
- Plotly Express
- Streamlit

## Como executar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Aplicativo publicado

Acesse o aplicativo em: https://tripleten-sprint5.onrender.com
