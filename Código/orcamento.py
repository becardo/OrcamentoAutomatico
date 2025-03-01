from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from calMaster import CalculoOrcamento  # Importa a classe de cálculo
from bd_orcamento import salvar_orcamento
from documento import GerarDocumento

janela = Tk()

class Orcamento:
    def __init__(self):
        self.janela = janela
        self.calculadora = CalculoOrcamento()  # Instância da calculadora
        self.tela()
        self.widgets()
        self.menus()
        janela.mainloop()

    def tela(self):
        imagem = Image.open("fundo.jpg")
        imagem = imagem.resize((900, 500))
        self.imagem_fundo = ImageTk.PhotoImage(imagem)
        self.label_fundo = Label(self.janela, image=self.imagem_fundo)
        self.label_fundo.place(x=0, y=0, relwidth=1, relheight=1)
        self.janela.title("Orçamento")
        self.janela.configure(background='#DAEDF4')
        self.janela.geometry("900x500")
        self.janela.resizable(False, False)

    def widgets(self):
        # Campo para o Nome
        self.lb_nome = Label(text="Nome: ", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_nome.place(relx=0.4, rely=0.01)
        self.nome_entry = Entry(font=('helvetica', 11), bg='#DAEDF4')
        self.nome_entry.place(relx=0.46, rely=0.0, relwidth=0.4)

        # Campo para o Produto
        self.lb_produto = Label(text="Nome do Produto: ", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_produto.place(relx=0.4, rely=0.09)
        self.produto_entry = Entry(font=('helvetica', 11), bg='#DAEDF4')
        self.produto_entry.place(relx=0.54, rely=0.08, relwidth=0.32)
        
        # para selecionar o tipo
        self.lb_tipo = Label(text="Classe: ", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_tipo.place(relx=0.4, rely=0.17) 
        
        self.opcao_1 = StringVar(value="Amigurumi")
        
        self.amig = Radiobutton(text='Amigurumi', variable= self.opcao_1, value="Amigurumi", bg='#DAEDF4', fg='#363636', 
                                activebackground='#DAEDF4', highlightbackground='#DAEDF4', font=('helvetica', 10))
        self.amig.place(relx=0.45, rely=0.26)
        self.amig = Radiobutton(text='Bolsa', variable= self.opcao_1, value="Bolsa", bg='#DAEDF4', fg='#363636', 
                                activebackground='#DAEDF4', highlightbackground='#DAEDF4', font=('helvetica', 10))
        self.amig.place(relx=0.6, rely=0.26)
        self.amig = Radiobutton(text='Vestuário', variable= self.opcao_1, value="Vestuário", bg='#DAEDF4', fg='#363636', 
                                activebackground='#DAEDF4', highlightbackground='#DAEDF4', font=('helvetica', 10))
        self.amig.place(relx=0.72, rely=0.26)

        # Campo para o Tipo do Fio
        self.lb_fio = Label(text="Tipo do Fio: ", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_fio.place(relx=0.4, rely=0.35)

        self.opcao_2 = StringVar(value="Amigurumi Soft")
        self.opcao_2.trace("w", self.atualizar_campos)

        tipos_fio = [
            ("Amigurumi Soft", 0.37, 0.45),
            ("Amigurumi Pelúcia", 0.37, 0.5),
            ("Barbante", 0.37, 0.55),
            ("Lã", 0.55, 0.45),
            ("Anne", 0.55, 0.5),
            ("Outro", 0.55, 0.55),
        ]

        for tipo, x, y in tipos_fio:
            Radiobutton(
                text=tipo, variable=self.opcao_2, value=tipo, bg='#DAEDF4', fg='#363636', font=('helvetica', 10)
            ).place(relx=x, rely=y)

        # Valor customizado
        self.lb_valor_la = Label(text="Valor da Lã: R$", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_valor_la.place(relx=0.7, rely=0.45)
        self.valor_la_entry = Entry(font=('helvetica', 11), bg='#DAEDF4', state=DISABLED)
        self.valor_la_entry.place(relx=0.82, rely=0.45, relwidth=0.1)

        self.lb_valor_outro = Label(text="Valor para outro Fio: R$", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_valor_outro.place(relx=0.7, rely=0.5)
        self.valor_outro_entry = Entry(font=('helvetica', 11), bg='#DAEDF4', state=DISABLED)
        self.valor_outro_entry.place(relx=0.88, rely=0.5, relwidth=0.1)

        # Quantidade de Novelos
        self.lb_qnt_novelos = Label(text="Quantidade de Novelos:", bg='#DAEDF4', fg='#363636', font=('helvetica', 11)) 
        self.lb_qnt_novelos.place(relx=0.4, rely=0.64)
        self.qnt_novelos = ttk.Combobox(values=list(range(1, 11)), state="readonly")
        self.qnt_novelos.place(relx=0.65, rely=0.64)

        # Quantidade de Horas
        self.lb_qnt_horas = Label(text="Horas trabalhadas:", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_qnt_horas.place(relx=0.4, rely=0.73)
        self.qnt_horas = ttk.Combobox(values=list(range(1, 21)), state="readonly")
        self.qnt_horas.place(relx=0.65, rely=0.73)

        # Quantidade de enchimento
        self.lb_qnt_enchimento = Label(text="Enchimento (50g):", bg='#DAEDF4', fg='#363636', font=('helvetica', 11))
        self.lb_qnt_enchimento.place(relx=0.4, rely=0.82)
        self.qnt_enchimento = ttk.Combobox(values=list(range(1, 21)), state=DISABLED)
        self.qnt_enchimento.place(relx=0.65, rely=0.82)
        
        # Botão Gerar Orçamento
        self.bt_gerar_orcamento = Button(
            text="Gerar Orçamento", bg='#DB7093', fg='white', font=('verdana', 8, 'bold'), command=self.gerar_orcamento
        )
        self.bt_gerar_orcamento.place(relx=0.75, rely=0.9, relwidth=0.2, relheight=0.05)

    def atualizar_campos(self, *args):
        if self.opcao_1.get() == "Amigurumi":
            self.qnt_enchimento.config(state=NORMAL)
        else:
            self.qnt_enchimento.config(state=DISABLED)    
        
        if self.opcao_2.get() == "Lã":
            self.valor_la_entry.config(state=NORMAL)
            self.valor_outro_entry.config(state=DISABLED)
        elif self.opcao_2.get() == "Outro":
            self.valor_la_entry.config(state=DISABLED)
            self.valor_outro_entry.config(state=NORMAL)
        else:
            self.valor_la_entry.config(state=DISABLED)
            self.valor_outro_entry.config(state=DISABLED)

    def gerar_orcamento(self):
        tipo_fio = self.opcao_2.get()  # Captura o tipo de fio selecionado
        num_novelos = int(self.qnt_novelos.get())  # Quantidade de novelos
        horas = int(self.qnt_horas.get())  # Horas trabalhadas
        valor_customizado = None

        # Verifica se há valores customizados para Lã ou Outro
        if tipo_fio == "Lã":
            valor_customizado = self.valor_la_entry.get()
        elif tipo_fio == "Outro":
            valor_customizado = self.valor_outro_entry.get()
            
        # Verificar quantidade de enchimento
        qnt_ench = 0  # Valor padrão
        if self.opcao_1.get() == "Amigurumi":
            qnt_ench = int(self.qnt_enchimento.get())

        # Realiza o cálculo do orçamento
        resultado = self.calculadora.calcular_orcamento(tipo_fio, num_novelos, horas, valor_customizado, qnt_ench)
        if resultado is not None:
            nome_cliente = self.nome_entry.get()  # Nome do cliente
            tipo_produto = self.produto_entry.get()  # Nome do produto
            classe_produto = self.opcao_1.get()  # Captura a classe do produto diretamente da variável

            # Captura o valor do fio
            valor_fio = float(valor_customizado) if valor_customizado else self.calculadora.valores_linhas.get(tipo_fio, 0.0)

            # Salva os dados no banco de dados
            salvar_orcamento(nome_cliente, tipo_produto, classe_produto, tipo_fio, valor_fio, num_novelos, horas)

            # Gera o PDF para o cliente
            GerarDocumento().gerar_pdf_cliente(
                nome_cliente, tipo_produto, classe_produto, tipo_fio, valor_fio, num_novelos, horas, resultado
            )
            self.exibir_orcamento(resultado)

    def exibir_orcamento(self, valor):
        top = Toplevel(self.janela)
        top.title("Orçamento Gerado")
        top.geometry("300x200")
        top.configure(bg='#DAEDF4')
        Label(top, text=f"Total: R$ {valor:.2f}", font=('helvetica', 14, 'bold'), bg='#DAEDF4').pack(pady=50)

    def menus(self):
        menubar = Menu(self.janela)
        self.janela.config(menu=menubar)
        filemenu = Menu(menubar)
        menubar.add_cascade(label="Menu", menu=filemenu)
        filemenu.add_command(label="Sair", command=self.janela.destroy)

Orcamento()
