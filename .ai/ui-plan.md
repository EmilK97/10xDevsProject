# Architektura UI dla BoardGameTracker

## 1. Przegląd struktury UI

BoardGameTracker to prosta, intuicyjna aplikacja webowa z minimalistycznym designem, wykorzystująca HTML, CSS i vanilla JavaScript. Interfejs użytkownika składa się z kilku kluczowych widoków, które pozwalają użytkownikom zarządzać swoją kolekcją gier planszowych.

Główna struktura UI bazuje na:
- Białym tle jako kolorze podstawowym
- Niebieskich elementach interaktywnych (przyciski, nagłówki)
- Kolorowych oznaczeniach statusu gier (brak ramki - normalny status, pomarańczowa ramka - ostrzeżenie, czerwona ramka - alarm)
- Układzie kafelkowym dla biblioteki gier (4 w rzędzie)
- Prosty system nawigacji z przyciskiem wylogowania w nagłówku

Aplikacja oferuje dwa główne tryby dostępu:
1. Panel użytkownika - do zarządzania własną biblioteką gier
2. Panel administratora - dostępny tylko dla administratorów, do zarządzania użytkownikami i wszystkimi grami

## 2. Lista widoków

### 2.1. Strona główna (niezalogowany użytkownik)

- **Ścieżka**: `/` lub `/login/`
- **Główny cel**: Umożliwienie logowania lub przekierowanie do rejestracji
- **Kluczowe informacje**:
  - Nazwa aplikacji
  - Krótki opis funkcjonalności
- **Kluczowe komponenty**:
  - Formularz logowania z polami: nazwa użytkownika, hasło
  - Link do rejestracji
  - Komunikaty o błędach logowania
- **UX, dostępność i bezpieczeństwo**:
  - Prosty, przejrzysty układ
  - Walidacja formularza przed wysłaniem
  - Zabezpieczenie przed CSRF

### 2.2. Rejestracja

- **Ścieżka**: `/register/`
- **Główny cel**: Rejestracja nowego użytkownika
- **Kluczowe informacje**:
  - Wymagania dotyczące nazwy użytkownika i hasła
- **Kluczowe komponenty**:
  - Formularz rejestracji z polami: nazwa użytkownika, hasło, potwierdzenie hasła
  - Przycisk "Zarejestruj się"
  - Link powrotu do strony logowania
  - Komunikaty o błędach rejestracji
- **UX, dostępność i bezpieczeństwo**:
  - Walidacja formularza w czasie rzeczywistym
  - Informacja o zajętości nazwy użytkownika
  - Zabezpieczenie przed CSRF
  - Automatyczne przekierowanie do biblioteki po pomyślnej rejestracji

### 2.3. Biblioteka gier

- **Ścieżka**: `/library/`
- **Główny cel**: Wyświetlenie i zarządzanie kolekcją gier użytkownika
- **Kluczowe informacje**:
  - Liczniki (całkowita liczba gier, liczba gier z alarmami)
  - Status filtrowania
- **Kluczowe komponenty**:
  - Nagłówek z licznikami i przyciskiem wylogowania
  - Sekcja filtrowania z trzema toggle switchami:
    - "Pokaż gry bez ostrzeżeń" (domyślnie włączony)
    - "Pokaż gry z ostrzeżeniami" (domyślnie włączony)
    - "Pokaż gry z alarmami" (domyślnie włączony)
  - Przycisk "Dodaj grę planszową"
  - Siatka kafelków gier (4 w rzędzie)
  - System paginacji (maksymalnie 16 kafelków na stronie)
  - Komunikat, gdy biblioteka jest pusta
- **UX, dostępność i bezpieczeństwo**:
  - Dynamiczna aktualizacja widoku po zmianie filtrów
  - Zabezpieczenie przed dostępem niezalogowanych użytkowników
  - Wizualne oznaczenie statusu gier kolorami ramek

### 2.4. Kafelek gry (komponent)

- **Główny cel**: Wyświetlenie podstawowych informacji o grze
- **Kluczowe informacje**:
  - Nazwa gry
  - Data ostatniej rozgrywki
  - Liczba dni od ostatniej rozgrywki
  - Status gry (normalny, ostrzeżenie, alarm)
- **Kluczowe komponenty**:
  - Odpowiednie emoji w zależności od typu gry (dwuosobowa/wieloosobowa)
  - Kolorowa ramka odpowiadająca statusowi gry
- **UX, dostępność i bezpieczeństwo**:
  - Wyraźne wizualne rozróżnienie statusów (brak ramki, pomarańczowa, czerwona)
  - Kliknięcie na kafelek przenosi do szczegółów gry

### 2.5. Modal dodawania nowej gry

- **Główny cel**: Umożliwienie dodania nowej gry do biblioteki
- **Kluczowe informacje**:
  - Wymagane pola
- **Kluczowe komponenty**:
  - Formularz z polami:
    - Nazwa gry (tekst)
    - Typ gry (dwuosobowa/wieloosobowa) - radio buttons
    - Data ostatniej rozgrywki (selektor daty z domyślną datą dzisiejszą)
  - Przyciski "Dodaj" i "Anuluj"
  - Przycisk zamknięcia modalu (X w rogu)
- **UX, dostępność i bezpieczeństwo**:
  - Walidacja formularza przed wysłaniem
  - Blokada wyboru dat z przyszłości
  - Zabezpieczenie przed CSRF
  - Możliwość zamknięcia modalu klikając poza jego obszar

### 2.6. Szczegóły gry

- **Ścieżka**: `/game/{id}/`
- **Główny cel**: Wyświetlenie szczegółowych informacji o grze i umożliwienie aktualizacji daty ostatniej rozgrywki
- **Kluczowe informacje**:
  - Nazwa gry
  - Typ gry (dwuosobowa/wieloosobowa)
  - Data ostatniej rozgrywki
  - Liczba dni od ostatniej rozgrywki
  - Status gry (normalny, ostrzeżenie, alarm)
- **Kluczowe komponenty**:
  - Przycisk "Zagrałem"
  - Przycisk powrotu do biblioteki
  - Odpowiednie emoji w zależności od typu gry
  - Wizualne oznaczenie statusu (kolor tekstu lub element graficzny)
- **UX, dostępność i bezpieczeństwo**:
  - Pop-up potwierdzający aktualizację daty rozgrywki
  - Zabezpieczenie przed dostępem niezalogowanych użytkowników
  - Zabezpieczenie przed dostępem do gier innych użytkowników

### 2.7. Panel administratora

- **Ścieżka**: `/admin/`
- **Główny cel**: Zarządzanie użytkownikami i grami w systemie
- **Kluczowe informacje**:
  - Korzysta z domyślnego panelu administracyjnego Django
- **Kluczowe komponenty**:
  - Sekcja zarządzania użytkownikami
  - Sekcja zarządzania grami
  - Filtry i wyszukiwarka
- **UX, dostępność i bezpieczeństwo**:
  - Dostęp tylko dla użytkowników z uprawnieniami administratora
  - Standardowe zabezpieczenia Django

## 3. Mapa podróży użytkownika

### 3.1. Rejestracja i pierwsze logowanie

1. Użytkownik wchodzi na stronę główną
2. Klika link "Zarejestruj się"
3. Wypełnia formularz rejestracji i zatwierdza
4. System automatycznie loguje użytkownika
5. Użytkownik zostaje przekierowany do pustej biblioteki gier
6. System wyświetla komunikat powitalny zachęcający do dodania pierwszej gry

### 3.2. Dodawanie nowej gry

1. Użytkownik klika przycisk "Dodaj grę planszową" w bibliotece
2. System wyświetla modal z formularzem dodawania gry
3. Użytkownik wypełnia pola (nazwa, typ, data ostatniej rozgrywki)
4. Użytkownik klika "Dodaj"
5. System dodaje grę do biblioteki
6. System odświeża widok biblioteki z nowo dodaną grą

### 3.3. Aktualizacja daty ostatniej rozgrywki

1. Użytkownik klika na kafelek gry w bibliotece
2. System wyświetla stronę szczegółów gry
3. Użytkownik klika przycisk "Zagrałem"
4. System aktualizuje datę ostatniej rozgrywki na dzisiejszą
5. System wyświetla pop-up potwierdzający aktualizację
6. System odświeża stronę szczegółów z zaktualizowaną datą i statusem

### 3.4. Filtrowanie gier

1. Użytkownik wchodzi do biblioteki gier
2. Użytkownik zmienia stan toggle switchy, aby filtrować gry
3. System dynamicznie aktualizuje widok biblioteki, pokazując tylko gry spełniające kryteria filtrowania

### 3.5. Wylogowanie

1. Użytkownik klika przycisk "Wyloguj" w nagłówku
2. System kończy sesję użytkownika
3. System przekierowuje użytkownika na stronę główną z formularzem logowania

## 4. Układ i struktura nawigacji

### 4.1. Nawigacja główna

- **Niezalogowany użytkownik**:
  - Strona główna (logowanie)
  - Rejestracja
  
- **Zalogowany użytkownik**:
  - Biblioteka gier (strona domowa po zalogowaniu)
  - Szczegóły gry (dostępne po kliknięciu na kafelek)
  - Przycisk wylogowania (w nagłówku na wszystkich stronach)

- **Administrator**:
  - Wszystkie powyższe
  - Panel administratora

### 4.2. Hierarchia nawigacji

```
BoardGameTracker
├── Strona główna / Logowanie
│   └── Rejestracja
├── Biblioteka gier (wymaga logowania)
│   ├── Modal dodawania gry
│   └── Szczegóły gry
└── Panel administratora (wymaga uprawnień)
```

## 5. Kluczowe komponenty

### 5.1. Nagłówek

- **Funkcja**: Nawigacja i wyświetlanie podstawowych informacji
- **Zawartość**:
  - Logo/nazwa aplikacji
  - Przyciski nawigacyjne
  - Przycisk wylogowania (dla zalogowanych użytkowników)
  - Informacja o zalogowanym użytkowniku

### 5.2. Kafelek gry

- **Funkcja**: Wyświetlanie podstawowych informacji o grze
- **Zawartość**:
  - Nazwa gry
  - Emoji odpowiadające typowi gry
  - Data ostatniej rozgrywki
  - Liczba dni od ostatniej rozgrywki
  - Ramka kolorystyczna odpowiadająca statusowi
- **Interakcja**: Kliknięcie przenosi do szczegółów gry

### 5.3. Toggle switche filtrowania

- **Funkcja**: Filtrowanie biblioteki gier według statusu
- **Zawartość**:
  - Trzy switche (normalny, ostrzeżenie, alarm)
  - Etykiety tekstowe
- **Interakcja**: Przełączanie powoduje natychmiastową aktualizację widoku biblioteki

### 5.4. Pop-up powiadomień

- **Funkcja**: Wyświetlanie krótkich komunikatów dla użytkownika
- **Zawartość**:
  - Komunikat tekstowy
  - Ikonka odpowiadająca typowi komunikatu (sukces, błąd, informacja)
- **Interakcja**: Automatyczne znikanie po 3 sekundach

### 5.5. Liczniki biblioteki

- **Funkcja**: Wyświetlanie statystyk biblioteki
- **Zawartość**:
  - Całkowita liczba gier
  - Liczba gier z alarmami
- **Interakcja**: Brak, element informacyjny

### 5.6. System paginacji

- **Funkcja**: Nawigacja między stronami biblioteki
- **Zawartość**:
  - Przyciski poprzednia/następna strona
  - Numeracja stron
  - Informacja o aktualnej stronie
- **Interakcja**: Kliknięcie zmienia wyświetlaną stronę biblioteki 