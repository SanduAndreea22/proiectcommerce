
![Screenshot 2024-05-26 221716](https://github.com/SanduAndreea22/proiectcommerce/assets/144158945/1f0e3406-6a99-4330-b928-0861f4f459cf)

# Andreea's PerfumStore 🛍️🌸

![Screenshot](img/screenshot-2024-05-26-221716.png)

Bine ai venit la **Andreea's PerfumStore**!
Acest proiect este un **magazin online de parfumuri** dezvoltat în **Django Python**. Oferă o experiență captivantă pentru achiziționarea parfumurilor preferate, într-un univers aromatic elegant și accesibil. 💖

---

## 🌟 Caracteristici principale

### 🛍️ Navigare în Magazin

* `store(request)` afișează lista de parfumuri disponibile.

### 💼 Informații Despre Parfumuri

* `perfum_info(request, slug)` afișează detalii despre un anumit parfum.

### 🛒 Gestionarea Coșului de Cumpărături

* `cart_add(request, id)` — adăugare produs în coș
* `cart_update(request)` — actualizare cantitate produs
* `cart_delete(request)` — ștergere produs din coș
* `cart_summary(request)` — afișare rezumat coș

### 📦 Finalizarea Comenzii

* `checkout(request)` și `complete_order(request)` — finalizează comanda și completează informațiile despre livrare și plată.

### 🔐 Autentificare și Autorizare

* `register(request)` — înregistrare utilizator
* `my_login(request)` — autentificare
* `user_logout(request)` — deconectare
* `dashboard(request)` — panou de control utilizator

### 📋 Urmărirea Comenzilor

* `track_orders(request)` — urmărire comenzi pentru utilizatori autentificați

### 🔑 Gestionarea Sesiunii

* `order_success(request)` — curățarea cheilor de sesiune după finalizarea comenzii

---

## 🛠️ Tehnologii și instrumente

* **Django Framework** – backend robust și funcționalități principale
* **Python** – logică și funcționalități aplicație
* **HTML, CSS, JavaScript** – frontend interactiv și responsive
* **Django Templates** – generare pagini HTML dinamice
* **Django Authentication** – gestionare autentificare și autorizare
* **Django Sessions** – gestionare sesiuni și coș de cumpărături

---

## 📌 Instrucțiuni de utilizare

1. Clonează repository-ul:

```bash
git clone https://github.com/SanduAndreea22/AndreeaSPerfumStore.git
```

2. Creează un mediu virtual:

```bash
python -m venv env
```

3. Activează mediul virtual:

   * Windows: `env\Scripts\activate`
   * Linux/Mac: `source env/bin/activate`

4. Instalează dependențele:

```bash
pip install -r requirements.txt
```

5. Pornește serverul Django:

```bash
python manage.py runserver
```

6. Deschide browser-ul și navighează la:

```
http://127.0.0.1:8000/ sau http://localhost:8000/
```

---

## 🎨 Stil și design

* Fundal cu gradient pastel
* Carduri parfum cu efect **glass** și hover subtil
* Butoane cu gradient și animații fine
* Responsive pentru desktop, tabletă și mobil
* Confirmare comenzi cu popup animat
* Prețuri evidențiate și ușor de citit

---

## 🌐 Link-uri utile

* [Cod sursă GitHub](https://github.com/SanduAndreea22/AndreeaSPerfumStore)
* [Proiect Live / Demo](https://sanduandreea22.github.io/AndreeaSPerfumStore/)

---

## 📄 Licență

Acest proiect este **open-source** și poate fi utilizat pentru portofoliu și uz personal.

---

## 🏆 Badge-uri sugerate pentru README

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge\&logo=python\&logoColor=ffdd54)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge\&logo=django\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge\&logo=javascript\&logoColor=black)

