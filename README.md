# Music Streaming App

* **Studente:** Carlotta Mercolini

---

## 🛠️ Specifiche del Progetto
* **Tipo di Progetto Scelto:** Full-Stack Web Application
* **Framework Utilizzato:** Django (Python)
* **Link del Deployment Online:** https://vellutotta.eu.pythonanywhere.com/

---

## 📝 Descrizione dell'Applicazione e Scopo
L'applicazione è una piattaforma web full-stack progettata per la gestione e l'ascolto di cataloghi musicali e playlist. Lo scopo del progetto è offrire agli utenti una navigazione fluida tra i brani musicali disponibili a livello globale e permettere agli utenti registrati (Premium) di organizzare la propria musica preferita in playlist personalizzate con un sistema di riproduzione continua.

---

## ✨ Funzionalità Implementate (Divise per Ruolo)

### 👥 Utente Anonimo / Visitatore
* **Esplorazione del Catalogo:** Accesso in sola lettura alla pagina principale (`/`) con la lista completa di tutti i brani, artisti e album registrati sulla piattaforma.
* **Ascolto Singolo:** Possibilità di riprodurre un'anteprima audio di ogni singolo brano direttamente dal catalogo globale tramite player HTML5 nativo.

### 🎧 Listener (Utente Premium Autenticato)
* **Gestione Playlist Personali (CRUD Completo):** Creazione, visualizzazione dei dettagli, modifica (nome e canzoni incluse) ed eliminazione delle proprie playlist musicali personali.
* **Isolamento dei Dati:** Ogni utente Premium può vedere e gestire *esclusivamente* le playlist create da lui stesso.
* **Player Intelligente con Riproduzione Continua:** All'interno del dettaglio della playlist, il lettore audio gestisce automaticamente la coda dei brani, passando in automatico alla canzone successiva al termine della precedente.

### 🛡️ Curator (Utente Staff / Admin)
* **Gestione Globale del Catalogo:** Accesso completo al pannello di amministrazione avanzato di Django (`/admin/`).
* **Controllo Data Model:** Permessi esclusivi per inserire, modificare o eliminare nuovi brani musicali (`Song`), caricare file audio, creare generi musicali ed inserire nuovi artisti nel database globale.

---

## 👥 Account Demo per la Valutazione

| Ruolo / Gruppo | Username       | Password   | Permessi |
| :--- |:---------------|:-----------| :--- |
| **Listener (Premium)** | `user_demo`    | user12345  | Accesso a Catalogo, Gestione Playlist proprie e Player Continuo. |
| **Curator (Staff/Admin)** |  `admin_demo`  | admin12345 | Controllo totale del catalogo musicale dal pannello `/admin/`. |

---

## 🧪 Scenario di Test Consigliato (Browser-based)

Per valutare rapidamente le funzionalità e i permessi del progetto, si consiglia il seguente flusso di test:

1. **Test Utente Visitatore (Permessi limitati):**
   * Aprire l'applicazione in una finestra in incognito senza fare il login.
   * Navigare la Home e cliccare sul tasto "Play" di un brano per testare l'ascolto libero.
   * *Verifica Permessi:* Notare che il link alle "Playlist" non è presente e provando ad accedere manualmente a `/playlists/` si viene reindirizzati al Login.

2. **Test Utente Premium (CRUD e Player Continuo):**
   * Effettuare il login con le credenziali di `user_demo`.
   * Andare nella sezione "Le tue Playlist" e testare la creazione di una nuova playlist (Create).
   * Aprire il dettaglio della playlist appena creata per visualizzare i brani (Read).
   * Testare il player in basso cliccando "Riproduci tutto": verificare lo scorrimento automatico al termine di ogni brano.
   * Utilizzare i tasti "Modifica" (Update) per cambiare il nome alla playlist o "Elimina" (Delete) per cancellarla.

3. **Test Amministratore (Gestione Globale):**
   * Effettuare il logout, e fare il login come `admin_demo`.
   * Accedere al pannello `/admin/`.
   * Aggiungere un nuovo brano al database o modificare il titolo di un brano esistente.
   * Tornare alla Home page per verificare che il catalogo si sia aggiornato istantaneamente per tutti gli utenti.

---

## 💾 Database Incluso e Dati Demo
Il progetto include il file di database **`db.sqlite3`**. 
Si conferma che il database è **pre-popolato** con account di test funzionanti e dati realistici (artisti, album e brani musicali con file audio associati) per permettere un'esplorazione immediata e completa di tutte le funzionalità dell'applicazione senza configurazioni aggiuntive.

---

## 💻 Istruzioni per l'Installazione e l'Esecuzione Locale

Seguire questi passaggi per scaricare ed eseguire il progetto in locale:

1. **Clonare il repository GitHub:**
   ```bash
   git clone [INSERISCI IL LINK DEL TUO GITHUB]
   cd music_streaming