# 🖥️ Automação de Cadastro de Produtos com Python

Este projeto realiza a **automação do cadastro de produtos em um sistema web**, utilizando Python para simular interações humanas com o navegador e realizar o preenchimento automático de formulários a partir de uma base de dados.

O objetivo é **otimizar tarefas repetitivas**, reduzir erros manuais e demonstrar na prática o uso de automação com Python.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **PyAutoGUI** – automação de teclado, mouse e interface gráfica
- **Pandas** – leitura e manipulação de dados
- **Time** – controle de pausas e sincronização

---

## ⚙️ Funcionalidades

✔ Abertura automática do navegador  
✔ Login automático no sistema  
✔ Leitura de dados via arquivo CSV  
✔ Cadastro automático de produtos  
✔ Tratamento de valores nulos (NaN)  
✔ Simulação de fluxo real de usuário  

---

## 🧠 Lógica de Funcionamento

1. Abre o navegador pelo sistema operacional  
2. Acessa o site de login  
3. Realiza o login automaticamente  
4. Importa a base de produtos (`produtos.csv`)  
5. Percorre cada linha da tabela  
6. Preenche os campos do formulário  
7. Registra os produtos no sistema  

---

## 📊 Exemplo da Base de Dados (CSV)

| codigo | marca | tipo | categoria | preco_unitario | custo | obs |
|------|------|------|----------|----------------|-------|-----|
| 001 | Nike | Tênis | Esporte | 299.90 | 180.00 | Promoção |

## 📚 Referência de Estudo

Este projeto foi desenvolvido com base em um curso gratuito da plataforma Jornada Python, com adaptações e personalizações realizadas durante o aprendizado.
---
