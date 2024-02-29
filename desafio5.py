import socket
import tkinter as tk
from tkinter import messagebox

def escanearPortas(hostAlvo, portaInicial, portaFinal):
    try:
        resultado = ""
        for porta in range(portaInicial, portaFinal + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            resultadoPorta = sock.connect_ex((hostAlvo, porta))
            if resultadoPorta == 0:
                resultado += f"Porta {porta}: Aberta\n"
                try:
                    servico = socket.getservbyport(porta)
                    resultado += f"   Serviço: {servico}\n"
                except OSError:
                    pass
            sock.close()
        return resultado
    except Exception as e:
        return f"Erro ao escanear portas: {str(e)}"

def iniciarEscanemento():
    hostAlvo = entradaHost.get()
    portaInicial = int(entradaPortaInicial.get())
    portaFinal = int(entradaPortaFinal.get())
    resultado = escanearPortas(hostAlvo, portaInicial, portaFinal)
    messagebox.showinfo("Resultado do Escaneamento", resultado)
   

app = tk.Tk()
app.title("Escaneamento de Portas")
app.configure(bg="#faca8c")  

frame = tk.Frame(app, bg="#faca8c")  
frame.pack(padx=10, pady=10)

botaoEscaneamento = tk.Button(frame, text="Escanear", command=iniciarEscanemento, bg="#268bd2", fg="black", width=70)   
botaoEscaneamento.grid(row=2, columnspan=6, padx=10, pady=10)

labelHost = tk.Label(frame, text="Host:", bg="#faca8c", fg="black")   
labelHost.grid(row=0, column=0, padx=5, pady=5)
entradaHost = tk.Entry(frame)
entradaHost.insert(0, "google.com")  
entradaHost.grid(row=0, column=1, padx=5, pady=5)

labelPortaInicial = tk.Label(frame, text="Porta Inicial:", bg="#faca8c", fg="black")   
labelPortaInicial.grid(row=0, column=2, padx=5, pady=5)
entradaPortaInicial = tk.Entry(frame)
entradaPortaInicial.insert(0, "80") 
entradaPortaInicial.grid(row=0, column=3, padx=5, pady=5)

labelPortaFinal = tk.Label(frame, text="Porta Final:", bg="#faca8c", fg="black")   
labelPortaFinal.grid(row=0, column=4, padx=5, pady=5)
entradaPortaFinal = tk.Entry(frame)
entradaPortaFinal.insert(0, "100") 
entradaPortaFinal.grid(row=0, column=5, padx=5, pady=5)


app.mainloop()