# -*- coding: utf-8 -*-
#por algum motivo sombrio não está aparecendo os simbolos no app. Mas na versão de "terminal" tava funfando. botei isso pq meu windows é podre
import customtkinter as ctk
import basemtm
import design
import entradas
import PIL


class AppConjuntos(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # 1. Aplica o tema definido no design.py
        design.aplicar_tema_global()
        
        self.title("UFMA - Analisador de Conjuntos")
        self.geometry("750x750")
        self.configure(fg_color=design.CORES["fundo"])
        self.conj_b = entradas.gerar_conjunto_aleatorio(modo="numeros") # Gera o conjunto B aleatório inicialmente, usando a função do entradas.py. O modo padrão é "numeros", mas pode ser alterado pelo usuário.
        # Aqui é pra construir a interface
        
        # Título usando o design.py
        self.label_titulo = ctk.CTkLabel(self, text="ANÁLISE DE CONJUNTOS", #aqui é um comentário meio solto, mas anteriormente, eu tinha feito colocando tipo, as cores diretamente aqui no main
                                         font=design.FONTES["titulo"], 
                                         text_color=design.CORES["detalhe"])
        self.label_titulo.pack(pady=(40, 20))

        # Entrada
        self.entry_usuario = ctk.CTkEntry(self, placeholder_text="Ex: 1, 2, a, b...", #Mas eu achei mais "profissional" fazer assim, chamando do design.py, e mais fácil de ajeitar né
                                         width=450, height=45,
                                         fg_color=design.CORES["card"],
                                         border_color=design.CORES["card"])
        self.entry_usuario.pack(pady=10)

        # Seletor Segmentado
        self.seletor = ctk.CTkSegmentedButton(self, values=["numeros", "letras", "misto"], #só que não tenho experiência suficiente pra saber se isso tá bom ou ruim, por isso vai ficar meio simples
                                             selected_color=design.CORES["detalhe"],
                                             command=self.atualizar_conjunto_b)
        self.seletor.pack(pady=15)

        # Botão Principal
        self.btn_calcular = ctk.CTkButton(self, text="CALCULAR", 
                                         fg_color=design.CORES["botao"],
                                         hover_color=design.CORES["botao_hover"],
                                         font=design.FONTES["subtitulo"],
                                         height=50, width=200,
                                         command=self.executar_calculos)
        self.btn_calcular.pack(pady=20)

        # Área de Resultados usando a Classe Customizada do design.py
        self.txt_resultados = design.CaixaTextoEstilizada(self, width=650, height=350)
        self.txt_resultados.pack(pady=10, padx=20)

    def atualizar_conjunto_b(self, modo):
        #Método que regenera o B quando o usuário troca no botão segmentado (basicamente um reroll para o B)
        self.conj_b = entradas.gerar_conjunto_aleatorio(modo=modo)
        # Limpa o texto para indicar que o B mudou
        self.txt_resultados.delete("0.0", "end")
        self.txt_resultados.insert("0.0", f"Modo alterado para '{modo}'. Conjunto B foi renovado!")

    def mostrar_feedback(self, mensagem, tipo="erro"): #isso aqui é só pra mostrar a mensagem de erro ou sucesso, tipo, se o usuário colocar um conjunto com 3 elementos, ele vai mostrar a mensagem de erro, e se ele colocar um conjunto com 5 elementos, ele vai mostrar a mensagem de sucesso
        cor = design.CORES["erro"] if tipo == "erro" else design.CORES["sucesso"]
        self.label_feedback = ctk.CTkLabel(self, text=mensagem, text_color=cor)
        self.label_feedback.pack(pady=5)
        # Efeito: remove a mensagem após 3 segundos
        self.after(3000, self.label_feedback.destroy)
        #mas tipo, eu botei só pra mostrar o feedback mesmo, como um caso de teste. 
    def executar_calculos(self):
        entrada = self.entry_usuario.get().lower()
        
        # Simulando a lógica inteligente que você já criou
        partes = entrada.replace(',', ' ').split()
        A = set()
        for item in partes:
            try:
                A.add(int(item))
            except ValueError:
                A.add(item.strip())

        # Validação de Tamanho
        if not (4 <= len(A) <= 8):
            # Chamada do feedback visual de erro
            self.mostrar_feedback(f"Erro: {len(A)} elementos detectados. Use entre 4 e 8.", "erro")
            
            self.txt_resultados.delete("0.0", "end")
            self.txt_resultados.insert("0.0", "⚠️ Tente novamente com a quantidade correta de elementos.")
            return

        B = self.conj_b
        U = basemtm.uniao(A, B) #cria um universo meio genérico, botei só nomes para
        U.update({0, 100, 'x', 'y'}) # Adiciona extras para garantir que o complemento não seja vazio
        # Realizando Operações do seu basemtm.py
        uniao = basemtm.uniao(A, B)
        inter = basemtm.intersecao(A, B)
        dif_ab = basemtm.diferenca(A, B)
        dif_ba = basemtm.diferenca(B, A)
        simetrica = basemtm.diferenca_simetrica(A, B)
        comp_a = basemtm.complemento(U, A)
        comp_b = basemtm.complemento(U, B)
        comp_a_em_b = basemtm.complemento(B, A)  # Isso é igual a B - A
        comp_b_em_a = basemtm.complemento(A, B)  # Isso é igual a A - B
        #coloquei esses 2 acima pois acho que talvez o professor queira.
        #Limpa a tela antes de escrever
        self.txt_resultados.delete("0.0", "end")
        # Exibição Formatada no App
        self.txt_resultados.insert("end", "𓂃𓂃𓂃CONJUNTOS𓂃𓂃𓂃\n", "titulo_azul")
        texto_conjuntos = f"Conjunto A (usuário): A =  {A}\n"
        texto_conjuntos += f"Conjunto B (aleatório): B = {B}\n"
        texto_conjuntos += f"Conjunto U (Universo): U = {U}\n" # Mostra o universo definido
        
        self.txt_resultados.insert("end", texto_conjuntos)

        # vou dividir por blocos. Cada espaço aqui é um bloco. Aqui é Operações.
        self.txt_resultados.insert("end", "\n ─────── OPERAÇÕES ───────  \n", "titulo_vermelho")
        texto_operacoes = f"A ∪ B = {uniao}\n"
        # Verifica se a interseção tem elementos (antes ele só colocava o resultado, mas se for vazio, vai ficar meio estranho, então coloquei um fallback)
        if inter:
            texto_operacoes += f"A ∩ B = {inter}\n"
        else:
            # Fallback para conjunto vazio
            texto_operacoes += "A ∩ B = ∅ (Sem valores compartilhados)\n"
        texto_operacoes += f"A - B  = {dif_ab}\n"
        texto_operacoes += f"B - A  = {dif_ba}\n" # Exibe a diferença inversa 
        texto_operacoes += f"A Δ B  = {simetrica}\n"
        texto_operacoes += f"Aᶜ(em U) = {comp_a}\n"
        texto_operacoes += f"Bᶜ(em U) = {comp_b}\n"
        texto_operacoes += f"Aᶜ(em B) = {comp_a_em_b}\n"
        texto_operacoes += f"Bᶜ(em A) = {comp_b_em_a}\n"
        self.txt_resultados.insert("end", texto_operacoes)

        self.txt_resultados.insert("end", "\n﹌﹌﹌﹌﹌﹌﹌ CARDINALIDADES ﹌﹌﹌﹌﹌﹌﹌ \n", "titulo_verde")
        texto_cardinalidades = f"|A| = {basemtm.cardinalidade(A)}  |  |B| = {basemtm.cardinalidade(B)}\n"
        texto_cardinalidades += f"|A ∪ B| = {basemtm.cardinalidade(uniao)}\n"
        texto_cardinalidades += f"|U| = {basemtm.cardinalidade(U)}"

        self.txt_resultados.insert("end", texto_cardinalidades)
        #  RELAÇÕES E PROPRIEDADES
        self.txt_resultados.insert("end", "\n\n✦ ─── ANÁLISE EXTRA ─── ✦\n", "titulo_roxo")
        
        # Verifica Subconjunto (A ⊆ B?)
        is_sub = basemtm.eh_subconjunto(A, B)
        texto_extra = f"A é subconjunto de B? {'Sim' if is_sub else 'Não'}\n"
        
        # Verifica Disjunção (A ∩ B = Ø?)
        is_disjunto = basemtm.sao_disjuntos(A, B)
        texto_extra += f"São conjuntos disjuntos? {'Sim' if is_disjunto else 'Não'}\n"
        
        self.txt_resultados.insert("end", texto_extra)
        #mensagem de sucesso pra confirmar que tá tudo ok. Vai que teve algum erro louco que eu n sei
        self.mostrar_feedback("Análise concluída com sucesso!", "sucesso")
if __name__ == "__main__":
    app = AppConjuntos()
    app.mainloop()