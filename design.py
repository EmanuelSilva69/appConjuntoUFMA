import customtkinter as ctk

# PALETA DE CORES (Estilo Moderno/Slate) (eu não sei as cores padrões de app hj em dia.)
CORES = { #Tirei todas as cores do site:https://coolors.co/dec5e3-cdedfd-b6dcfe-a9f8fb-81f7e5 !! MUITO BOM pra pegar cores.
    "fundo": "#0F172A",        # Slate 900 (Fundo escuro profundo)
    "card": "#1E293B",         # Slate 800 (Fundo dos elementos)
    "detalhe": "#38BDF8",      # Sky Blue (Títulos e bordas)
    "botao": "#6366F1",        # Indigo (Botão principal)
    "botao_hover": "#4F46E5",  # Indigo Escuro
    "texto": "#F1F5F9",        # Slate 100 (Texto principal)
    "erro": "#EF4444",          # Vermelho (Alertas)
    "sucesso": "#10B981",      # Verde (Sucesso)
    "titulo3": "#68448D",      # Roxo Escuro (Títulos 3)
    "titulo4": "#FF6FD8",      # Rosa Neon (Títulos 4)   
    "titulo5":"#B75D69" ,       #esse vermelho ai é meio brabo
    "titulo6" : "#9A9B73",
    "titulo7": "#81F7E5", #neon ice
    "titulo8": "#B6DCFE" #icy blue
}#eu to adicionando cores a mais ai, que eu possivelmente não vou usar, mas é para teste. 

# CONFIGURAÇÕES DE FONTE 
# O CustomTkinter usa as fontes do sistema. 
# Roboto e Montserrat são ótimas, se não tiver, ele usará a padrão do sistema.
FONTES = {
    "titulo": ("Roboto", 26, "bold"),
    "subtitulo": ("Montserrat", 13, "bold"),
    "corpo": ("Montserrat", 12),
    "resultados": ("Segoe UI Symbol", 15) # Esta fonte é ótima para símbolos
}

def aplicar_tema_global():
    #Configura o comportamento básico do CustomTkinter
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

class CaixaTextoEstilizada(ctk.CTkTextbox):
    #Componente customizado para os resultados
    def __init__(self, master, **kwargs):
        super().__init__(master, 
                         corner_radius=12,
                         border_width=2,
                         border_color=CORES["card"],
                         fg_color=CORES["card"],
                         text_color=CORES["texto"],
                         font=FONTES["resultados"],
                         wrap="word", # Quebra linha se o conjunto for grande. Não é obrigatório, mas me permite colocar cor no texto (só por isso que to quebrando o bloco de texto.)
                         **kwargs)
        
        # CONFIGURAÇÃO AUTOMÁTICA DE TAGS 
        # Isso permite usar cores diferentes dentro do mesmo texto
        
        # Tag para títulos (Azul Neon)
        self.tag_config("titulo_azul", foreground=CORES["titulo5"])
        
        # Tag para Títulos 2 (Vermelho)
        self.tag_config("titulo_vermelho", foreground=CORES["titulo8"])
        
        # Tag para Títulos 3 (Verde)
        self.tag_config("titulo_verde", foreground=CORES["titulo7"])
         # Tag para Títulos 4 (Roxo)
        self.tag_config("titulo_roxo", foreground=CORES["titulo3"])