import customtkinter as ctk
from ai.brain import responder
from voice.tts import hablar

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class ShuwaWindow(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Shuwa AI v0.2")

        self.geometry("1200x750")

        self.resizable(False, False)

        #=========================
        # Título
        #=========================

        titulo = ctk.CTkLabel(
            self,
            text="🤖 SHUWA AI",
            font=("Arial", 32, "bold")
        )

        titulo.pack(pady=15)

        #=========================
        # Contenedor principal
        #=========================

        principal = ctk.CTkFrame(self)

        principal.pack(fill="both", expand=True, padx=15)

        #=========================
        # Panel izquierdo
        #=========================

        izquierda = ctk.CTkFrame(
            principal,
            width=250
        )

        izquierda.pack(side="left", fill="y", padx=10, pady=10)

        avatar = ctk.CTkLabel(
            izquierda,
            text="😊",
            font=("Arial", 100)
        )

        avatar.pack(pady=25)

        ctk.CTkLabel(
            izquierda,
            text="Shuwa",
            font=("Arial",22,"bold")
        ).pack()

        ctk.CTkLabel(
            izquierda,
            text="Estado\n🟢 En línea",
            font=("Arial",16)
        ).pack(pady=20)

        self.estado = ctk.CTkTextbox(
            izquierda,
            width=200,
            height=220
        )

        self.estado.pack(pady=10)

        self.estado.insert(
            "end",
            "LM Studio : 🟢\n\n"
            "Memoria : 🟢\n\n"
            "Contexto : 🟢\n\n"
            "Voz : 🔴\n\n"
            "Twitch : 🔴\n\n"
            "OBS : 🔴\n\n"
            "VTube : 🔴"
        )

        self.estado.configure(state="disabled")

        #=========================
        # Panel derecho
        #=========================

        derecha = ctk.CTkFrame(principal)

        derecha.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.chat = ctk.CTkTextbox(
            derecha,
            font=("Arial",15)
        )

        self.chat.pack(fill="both", expand=True)

        self.chat.insert(
            "end",
            "🤖 Shuwa:\n¡Hola Naofumy! 😊\n\n"
        )

        abajo = ctk.CTkFrame(derecha)

        abajo.pack(fill="x", pady=10)

        self.entrada = ctk.CTkEntry(
            abajo,
            height=40
        )

        self.entrada.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10
        )

        self.entrada.bind("<Return>", self.enviar)

        micro = ctk.CTkButton(
            abajo,
            text="🎤",
            width=50
        )

        micro.pack(side="left", padx=5)

        enviar = ctk.CTkButton(
            abajo,
            text="Enviar",
            width=120,
            command=self.enviar
        )

        enviar.pack(side="left", padx=5)

        config = ctk.CTkButton(
            abajo,
            text="⚙",
            width=50
        )

        config.pack(side="left", padx=5)

    def enviar(self, event=None):

        mensaje = self.entrada.get().strip()

        if mensaje == "":
            return

        self.chat.insert(
            "end",
            f"👤 Tú:\n{mensaje}\n\n"
        )

        self.entrada.delete(0,"end")

        self.update()

        respuesta = responder(mensaje)
        hablar(respuesta)

        self.chat.insert(
            "end",
            f"🤖 Shuwa:\n{respuesta}\n\n"
        )

        self.chat.see("end")