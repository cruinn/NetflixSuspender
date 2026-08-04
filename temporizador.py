"""
Temporizador de Suspensão/Desligamento do PC

Você digita a duração do filme, escolhe se quer suspender ou desligar
o PC, e o app faz isso automaticamente quando o tempo acabar.

Como rodar:
    python temporizador.py

Não precisa instalar nada — usa só bibliotecas padrão do Python.
"""

import os
import tkinter as tk
from tkinter import messagebox


class TemporizadorApp:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Temporizador de Suspensão")
        self.raiz.geometry("340x320")
        self.raiz.resizable(False, False)

        self.segundos_restantes = 0
        self.rodando = False
        self.pausado = False
        self.id_after = None

        self.acao = tk.StringVar(value="suspender")

        self._montar_interface()

    def _montar_interface(self):
        tk.Label(self.raiz, text="Duração do filme", font=("Segoe UI", 12, "bold")).pack(pady=(15, 5))

        frame_tempo = tk.Frame(self.raiz)
        frame_tempo.pack(pady=5)

        tk.Label(frame_tempo, text="Horas:").grid(row=0, column=0, padx=5)
        self.entrada_horas = tk.Spinbox(frame_tempo, from_=0, to=10, width=5)
        self.entrada_horas.grid(row=0, column=1, padx=5)

        tk.Label(frame_tempo, text="Minutos:").grid(row=0, column=2, padx=5)
        self.entrada_minutos = tk.Spinbox(frame_tempo, from_=0, to=59, width=5)
        self.entrada_minutos.grid(row=0, column=3, padx=5)
        self.entrada_minutos.delete(0, "end")
        self.entrada_minutos.insert(0, "30")

        tk.Label(self.raiz, text="O que fazer quando acabar:", font=("Segoe UI", 10)).pack(pady=(15, 5))

        frame_acao = tk.Frame(self.raiz)
        frame_acao.pack()
        tk.Radiobutton(frame_acao, text="Suspender", variable=self.acao, value="suspender").pack(side="left", padx=10)
        tk.Radiobutton(frame_acao, text="Desligar", variable=self.acao, value="desligar").pack(side="left", padx=10)

        self.rotulo_contagem = tk.Label(self.raiz, text="00:00:00", font=("Segoe UI", 28, "bold"), fg="#333")
        self.rotulo_contagem.pack(pady=20)

        frame_botoes = tk.Frame(self.raiz)
        frame_botoes.pack()

        self.botao_iniciar = tk.Button(frame_botoes, text="Iniciar", width=10, command=self.iniciar)
        self.botao_iniciar.grid(row=0, column=0, padx=5)

        self.botao_pausar = tk.Button(frame_botoes, text="Pausar", width=10, command=self.alternar_pausa, state="disabled")
        self.botao_pausar.grid(row=0, column=1, padx=5)

        self.botao_cancelar = tk.Button(frame_botoes, text="Cancelar", width=10, command=self.cancelar, state="disabled")
        self.botao_cancelar.grid(row=0, column=2, padx=5)

    def iniciar(self):
        try:
            horas = int(self.entrada_horas.get())
            minutos = int(self.entrada_minutos.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite números válidos para horas e minutos.")
            return

        total_segundos = horas * 3600 + minutos * 60
        if total_segundos <= 0:
            messagebox.showerror("Erro", "A duração precisa ser maior que zero.")
            return

        self.segundos_restantes = total_segundos
        self.rodando = True
        self.pausado = False

        self.botao_iniciar.config(state="disabled")
        self.botao_pausar.config(text="Pausar", state="normal")
        self.botao_cancelar.config(state="normal")
        self.entrada_horas.config(state="disabled")
        self.entrada_minutos.config(state="disabled")

        self._contar()

    def alternar_pausa(self):
        self.pausado = not self.pausado
        self.botao_pausar.config(text="Retomar" if self.pausado else "Pausar")

    def cancelar(self):
        self.rodando = False
        if self.id_after:
            self.raiz.after_cancel(self.id_after)
            self.id_after = None

        self.botao_iniciar.config(state="normal")
        self.botao_pausar.config(state="disabled", text="Pausar")
        self.botao_cancelar.config(state="disabled")
        self.entrada_horas.config(state="normal")
        self.entrada_minutos.config(state="normal")
        self.rotulo_contagem.config(text="00:00:00")

    def _contar(self):
        if not self.rodando:
            return

        if not self.pausado:
            if self.segundos_restantes <= 0:
                self._executar_acao()
                return
            self.segundos_restantes -= 1

        self._atualizar_rotulo()
        self.id_after = self.raiz.after(1000, self._contar)

    def _atualizar_rotulo(self):
        h = self.segundos_restantes // 3600
        m = (self.segundos_restantes % 3600) // 60
        s = self.segundos_restantes % 60
        self.rotulo_contagem.config(text=f"{h:02d}:{m:02d}:{s:02d}")

    def _executar_acao(self):
        self.rodando = False
        acao = self.acao.get()
        if acao == "suspender":
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            os.system("shutdown /s /f /t 0")


if __name__ == "__main__":
    raiz = tk.Tk()
    app = TemporizadorApp(raiz)
    raiz.mainloop()
