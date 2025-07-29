# 🧵 Orçamento Automático para Crochê & Tricô

Este é um projeto em Python com interface gráfica que automatiza a geração de orçamentos para peças artesanais em crochê e tricô. A aplicação permite cadastrar informações do projeto, calcula o custo total e gera um **PDF personalizado com o nome do cliente e os detalhes do orçamento**.

> ⏳ Implementação ainda em desenvolvimento... 
---

## ✨ Funcionalidades

- Interface gráfica amigável feita com **Tkinter**
- Cadastro dos seguintes dados:
  - Escolha do tipo de linha utilizada
  - Quantidade de novelos
  - Horas trabalhadas
  - Custo de materiais
  - Preço por hora
  - Nome do cliente
- **Banco de dados SQL** para armazenar os orçamentos
- Cálculo automático do valor total
- Geração de **PDF** com layout personalizado usando `reportlab`
- Histórico de orçamentos

---

## 🖼️ Interface gráfica (Tkinter)

```bash
📸 Exemplo de uso:

1. Preencha os campos
2. Clique em "Gerar Orçamento"
3. Pronto! O PDF será salvo com os dados do cliente.
