from fpdf import FPDF

class GerarDocumento:
    def gerar_pdf_cliente(self, nome, produto, classe, tipo_fio, valor_fio, qnt_novelos, horas, total):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Cabeçalho
        pdf.cell(200, 10, txt="Orçamento Individual", ln=True, align="C")
        pdf.ln(10)

        # Dados do cliente e orçamento
        pdf.cell(200, 10, txt=f"Cliente: {nome}", ln=True)
        pdf.cell(200, 10, txt=f"Produto: {produto} ({classe})", ln=True)
        pdf.cell(200, 10, txt=f"Tipo de Fio: {tipo_fio} - R$ {valor_fio:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Quantidade de Novelos: {qnt_novelos}", ln=True)
        pdf.cell(200, 10, txt=f"Horas Trabalhadas: {horas}", ln=True)
        pdf.cell(200, 10, txt=f"Valor Total: R$ {total:.2f}", ln=True)

        # Salvar o PDF com o nome do cliente
        nome_arquivo = f"orcamento_{nome.replace(' ', '_')}.pdf"
        pdf.output(nome_arquivo)
        print(f"PDF gerado para {nome}: {nome_arquivo}")
