# TC-LOGIN – Przypadki testowe: Moduł logowania

**Aplikacja:** SauceDemo (https://www.saucedemo.com)  
**Moduł:** Logowanie użytkownika  
**Autor:** Jakub Mazur  
**Data:** 2026-10  
**Środowisko:** Chrome (headless), Playwright 1.47

---

## TC-001 – Poprawne logowanie

| Pole | Wartość |
|---|---|
| **ID** | TC-001 |
| **Priorytet** | Krytyczny |
| **Typ testu** | Funkcjonalny, pozytywny |
| **Warunki wstępne** | Aplikacja dostępna pod adresem BASE_URL |

**Kroki:**
1. Otwórz stronę główną aplikacji.
2. W polu "Username" wpisz: `standard_user`.
3. W polu "Password" wpisz: `secret_sauce`.
4. Kliknij przycisk "Login".

**Oczekiwany rezultat:**  
Użytkownik zostaje przekierowany na stronę `/inventory.html`. Wyświetlona jest lista produktów.

**Status:** ✅ PASS

---

## TC-002 – Logowanie z błędnym hasłem

| Pole | Wartość |
|---|---|
| **ID** | TC-002 |
| **Priorytet** | Wysoki |
| **Typ testu** | Funkcjonalny, negatywny |

**Kroki:**
1. Otwórz stronę główną.
2. Wpisz poprawną nazwę użytkownika: `standard_user`.
3. Wpisz błędne hasło: `wrong_password`.
4. Kliknij "Login".

**Oczekiwany rezultat:**  
Pojawia się komunikat błędu: *"Epic sadface: Username and password do not match any user in this service"*. Użytkownik pozostaje na stronie logowania.

**Status:** ✅ PASS

---

## TC-003 – Puste pole nazwy użytkownika

| Pole | Wartość |
|---|---|
| **ID** | TC-003 |
| **Priorytet** | Wysoki |
| **Typ testu** | Walidacja formularza, negatywny |

**Kroki:**
1. Otwórz stronę główną.
2. Pozostaw pole "Username" puste.
3. Wpisz poprawne hasło.
4. Kliknij "Login".

**Oczekiwany rezultat:**  
Komunikat błędu: *"Epic sadface: Username is required"*. Brak przekierowania.

**Status:** ✅ PASS

---

## TC-004 – Puste pole hasła

| Pole | Wartość |
|---|---|
| **ID** | TC-004 |
| **Priorytet** | Wysoki |
| **Typ testu** | Walidacja formularza, negatywny |

**Kroki:**
1. Otwórz stronę główną.
2. Wpisz poprawną nazwę użytkownika.
3. Pozostaw pole "Password" puste.
4. Kliknij "Login".

**Oczekiwany rezultat:**  
Komunikat błędu: *"Epic sadface: Password is required"*. Brak przekierowania.

**Status:** ✅ PASS

---

## TC-005 – Zablokowane konto użytkownika

| Pole | Wartość |
|---|---|
| **ID** | TC-005 |
| **Priorytet** | Średni |
| **Typ testu** | Funkcjonalny, negatywny, graniczny |

**Kroki:**
1. Otwórz stronę główną.
2. Wpisz nazwę użytkownika: `locked_out_user`.
3. Wpisz poprawne hasło: `secret_sauce`.
4. Kliknij "Login".

**Oczekiwany rezultat:**  
Komunikat błędu zawiera informację o zablokowaniu konta: *"Sorry, this user has been locked out."*.

**Status:** ✅ PASS

---

## TC-006 – Tytuł strony po zalogowaniu

| Pole | Wartość |
|---|---|
| **ID** | TC-006 |
| **Priorytet** | Niski |
| **Typ testu** | Funkcjonalny, UI |

**Kroki:**
1. Zaloguj się poprawnymi danymi.
2. Sprawdź tytuł zakładki przeglądarki (document.title).

**Oczekiwany rezultat:**  
Tytuł strony zawiera tekst *"Swag Labs"*.

**Status:** ✅ PASS
