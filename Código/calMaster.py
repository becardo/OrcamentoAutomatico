class CalculoOrcamento:
    def __init__(self):
        # Tabela de preços das linhas
        self.valores_linhas = {
            "Amigurumi Soft": 15.90,
            "Amigurumi Pelúcia": 14.90,
            "Anne": 20.90,
            "Barbante": 15.90
        }
        self.valor_hora = 20.00  # Valor por hora trabalhada
        self.valor_enchimento = 2.00 # Valor de 50 gramas de enchimento

    def calcular_orcamento(self, tipo_fio, num_novelos, horas, valor_customizado=None, qnt_ench=0):
        """
        Realiza o cálculo do orçamento.
        :param tipo_fio: Tipo do fio selecionado
        :param num_novelos: Número de novelos utilizados
        :param horas: Horas trabalhadas
        :param valor_customizado: Valor do fio para 'Lã' ou 'Outro'
        :return: Valor total do orçamento
        """
        try:
            # Verifica o tipo do fio e obtém o valor correspondente
            if tipo_fio in self.valores_linhas:
                valor_fio = self.valores_linhas[tipo_fio]
            elif valor_customizado is not None:
                valor_fio = float(valor_customizado)
            else:
                raise ValueError("Valor do fio customizado não fornecido.")

            # Garante que qnt_ench é um número válido
            qnt_ench = qnt_ench if qnt_ench is not None else 0

            # Calcula o orçamento
            orcamento = (
                (num_novelos * valor_fio) +  # Custo dos novelos
                (horas * self.valor_hora) +  # Custo do trabalho
                (qnt_ench * self.valor_enchimento)  # Custo do enchimento
            )
            return round(orcamento, 2)
        except Exception as e:
            print(f"Erro ao calcular o orçamento: {e}")
            return None
