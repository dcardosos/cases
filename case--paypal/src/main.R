library(tidyverse)
library(patchwork)
library(magrittr)

data <- readr::read_csv('data/travel_insurance.csv')

# net sales por agency e product name

tibble(
  graficos = list( 
data %>%
  group_by(Agency) %>%
  summarise(
    mean_net_sales = mean(Net_Sales, na.rm = TRUE),
    .groups = 'drop') %>%
  ggplot(aes(x = mean_net_sales, y = Agency)) +
  geom_bar(stat = 'identity', fill = '#099156') +
  theme_minimal() + 
  labs(
    x = 'Média de vendas',
    y = 'Sigla da Agência',
    title = 'Média de vendas por Agência'),

data %>%
  group_by(Product_Name) %>%
  summarise(
    mean_net_sales = mean(Net_Sales, na.rm = TRUE),
    .groups = 'drop') %>%
  ggplot(aes(x = mean_net_sales, y = Product_Name)) +
  geom_bar(stat = 'identity', fill = '#db9407') +
  theme_minimal() + 
  labs(
    x = 'Média de vendas',
    y = 'Nome do produto',
    title = 'Média de vendas por Produto'))) %$%
  reduce(graficos, `+`)
