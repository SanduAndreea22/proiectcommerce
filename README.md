**Andreea's PerfumStore**


***Descriere:***

Bine ai venit la Andreea's PerfumStore! Acest proiect este un magazin online de parfumuri dezvoltat în Django Python. Aici găsești un univers aromatic de parfumuri excepționale, oferind o experiență captivantă și accesibilă pentru achiziționarea parfumurilor preferate.

***Caracteristici***:

🛍️ **Navigare în Magazin**
   - Funcția store(request) afișează lista de parfumuri disponibile în magazin.

💼 **Informații Despre Parfumuri**
   - Funcția perfum_info(request, slug) afișează detalii despre un anumit parfum pe baza slug-ului acestuia.

🛒 **Gestionarea Coșului de Cumpărături**
   - Există funcții pentru adăugarea, actualizarea și ștergerea produselor din coșul de cumpărături (cart_add(request, id), cart_update(request), cart_delete(request)).
   - Funcția cart_summary(request) afișează un rezumat al coșului de cumpărături.

📦 **Finalizarea Comenzii**
   - Funcțiile checkout(request) și complete_order(request) permit utilizatorilor să finalizeze comanda și să completeze informațiile despre livrare și plată.

🔐 **Autentificare și Autorizare**
   - Există funcții pentru înregistrare (register(request)), autentificare (my_login(request)), deconectare (user_logout(request)) și afișarea unui panou de control (dashboard(request)).

📋 **Urmărirea Comenzilor**
   - Funcția track_orders(request) permite utilizatorilor autentificați să urmărească comenzile lor.

🔑 **Gestionarea Sesiunii**
   - Funcția order_success(request) șterge cheile de sesiune după finalizarea cu succes a unei comenzi.

***Tehnologii si instrumente***:

🛠️ **Django Framework**
   - Utilizat pentru dezvoltarea backend-ului și a funcționalităților principale ale aplicației web.

💻 **Python Programming Language**
   - Limbajul de programare principal folosit pentru implementarea logică și a funcționalităților.

🌐 **HTML, CSS, JavaScript**
   - Folosite pentru dezvoltarea frontend-ului, pentru a crea interfețe utilizator prietenoase și interactive.

📦 **Django Templates**
   - Utilizate pentru generarea paginilor HTML dinamic, bazate pe datele preluate din backend.

🔐 **Django Authentication System**
   - Folosit pentru gestionarea autentificării și autorizării utilizatorilor în aplicație.

🛒 **Django Sessions**
   - Utilizate pentru gestionarea sesiunilor utilizatorilor și a coșului de cumpărături.

Acestea sunt tehnologiile și instrumentele principale utilizate în dezvoltarea Andreea's PerfumStore, care au contribuit la crearea unei aplicații web robuste și eficiente!

***Instrucțiuni de Utilizare:***

1. **Deschide terminalul în PyCharm**

2. Rulează comanda **`git clone <url_proiect_git>`**, înlocuind `<url_proiect_git>` cu URL-ul proiectului de pe GitHub. Aceasta va clona întregul proiect în directorul curent.

3. Rulează comanda **python -m venv env** pentru a crea un mediu virtual numit "env". Acest mediu virtual va izola dependințele proiectului pentru a evita conflictele cu alte proiecte Python.

4. Pentru a activa mediu virtual, ruleaza comanda: 
   - Pe Windows: Rulează comanda **env\Scripts\activate**
   - Pe Linux/Mac: Rulează comanda **source env/bin/activate** 

5. Rulează comanda **pip install -r requirements.txt** pentru a instala toate dependințele proiectului. Acest lucru va instala toate modulele Python necesare pentru a rula aplicația.

6. Rulează comanda **python manage.py runserver** pentru a porni serverul de dezvoltare Django. Acesta va începe să servească aplicația la adresa `http://127.0.0.1:8000/` sau `http://localhost:8000/`.





