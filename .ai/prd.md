# Dokument wymagań produktu (PRD) - BoardGameTracker

## 1. Przegląd produktu

BoardGameTracker to prosta aplikacja webowa zaprojektowana, aby pomóc użytkownikom śledzić swoją kolekcję gier planszowych i identyfikować te, które są rzadko używane. Aplikacja pozwala użytkownikom na prowadzenie własnej biblioteki gier planszowych, śledzenie dat ostatnich rozgrywek oraz automatyczne oznaczanie gier, które nie były używane przez dłuższy czas. Aplikacja nie jest produktem komerycjnym, a jej przeznaczenie to demontracja na potrzeby kursu.

Główne funkcje aplikacji:
- Prosty system rejestracji i logowania
- Zarządzanie biblioteką gier planszowych
- Automatyczne oznaczanie rzadko używanych gier
- Aktualizacja dat ostatnich rozgrywek
- Filtrowanie i przeglądanie kolekcji

Aplikacja będzie zbudowana w technologii Python (Django) z prostym frontendem (CSS, HTML, JavaScript). Interfejs użytkownika będzie charakteryzował się nowoczesnym designem z białym tłem i jasnoniebieskimi elementami interaktywnymi.

## 2. Problem użytkownika

### Problem

Manualne śledzenie gier planszowych w dużej kolekcji jest trudne, co prowadzi do sytuacji, w której użytkownicy często posiadają zbyt dużo gier planszowych, w które nigdy nie grają. Brak systematycznego śledzenia dat rozgrywek powoduje, że właściciele kolekcji:
- Nie mają świadomości, które gry nie były używane przez długi czas
- Niepotrzebnie zajmują przestrzeń przechowywania rzadko używanymi grami
- Mają trudności z zarządzaniem swoją kolekcją
- Kupują nowe gry, nie wykorzystując w pełni tych, które już posiadają

### Rozwiązanie

BoardGameTracker rozwiązuje te problemy poprzez:
- Śledzenie dat ostatnich rozgrywek
- Wyraźne oznaczanie gier, które nie były używane przez określony czas (ostrzeżenia i alarmy)
- Dostarczanie przejrzystego widoku całej kolekcji z możliwością filtrowania
- Umożliwienie szybkiej aktualizacji daty rozgrywki jednym kliknięciem
- Pomoc w podejmowaniu decyzji o pozbyciu się nieużywanych gier

## 3. Wymagania funkcjonalne

### System użytkowników
1. Rejestracja użytkownika z wykorzystaniem nicku i hasła
2. Logowanie użytkownika do systemu
3. Wylogowanie użytkownika
4. Przypisanie biblioteki gier do profilu użytkownika

### Zarządzanie biblioteką
5. Przeglądanie biblioteki gier w formie kafelków (4 kafelki w rzędzie)
6. Dodawanie nowej gry do biblioteki (nazwa, data ostatniej rozgrywki, typ)
7. Wyświetlanie szczegółów gry
8. Aktualizacja daty ostatniej rozgrywki przyciskiem "Zagrałem", który zmienia datę ostatniej rozgrywki na dzisiejszą.
9. Filtrowanie gier oznaczonych alarmem lub ostrzeżeniem
10. Wyświetlanie liczników (całkowita liczba gier i liczba gier z alarmami dla profilu użytkownika)

### System oznaczania gier
11. Automatyczne oznaczanie gier ostrzeżeniem, gdy data ostatniej rozgrywki jest starsza niż 1 rok
12. Automatyczne oznaczanie gier alarmem, gdy data ostatniej rozgrywki jest starsza niż 3 lata
13. Wizualne oznaczenie gier (pomarańczowa ramka dla ostrzeżeń, czerwona dla alarmów)

### Panel administracyjny
14. Zarządzanie użytkownikami przez administratora
15. Przeglądanie wszystkich gier w systemie przez administratora

## 4. Granice produktu

### W zakresie MVP
- Prosty system rejestracji i logowania (tylko nick i hasło)
- Biblioteka gier planszowych przypisana do profilu użytkownika
- Kategoryzacja gier na dwuosobowe i wieloosobowe
- Automatyczne oznaczanie gier ostrzeżeniem lub alarmem
- Aktualizacja daty ostatniej rozgrywki
- Filtrowanie gier oznaczonych alarmem lub ostrzeżeniem
- Panel administracyjny dla zarządzania użytkownikami
- Interfejs webowy

### Poza zakresem MVP
- Ocenianie jakości gier w skali 1-10
- Wysyłanie powiadomień mailowych odnośnie alarmów o stanie gier
- Współdzielenie zestawów gier pomiędzy użytkownikami
- Integracje z innymi platformami internetowymi
- Aplikacje mobilne
- Możliwość usuwania lub edytowania gier z biblioteki
- Dostosowanie progów czasowych dla alarmów
- Możliwość resetu hasła
- Możliwość usuwania konta

### Ograniczenia techniczne
- Aplikacja nie musi być responsywna na urządzeniach mobilnych
- Aplikacja będzie wykorzystywać domyślny panel admina Django
- Brak wymagań dotyczących testów automatycznych (nierozwiązane)
- Brak szczegółowych informacji o zabezpieczeniach przed atakami na logowanie (nierozwiązane)
- Brak szczegółowych informacji o procesie wdrożenia aplikacji (nierozwiązane)

## 5. Historyjki użytkowników

### US-001: Rejestracja użytkownika
Jako nowy użytkownik, chcę zarejestrować się w aplikacji BoardGameTracker, aby móc korzystać z jej funkcjonalności.

Kryteria akceptacji:
- Na stronie głównej dostępny jest formularz rejestracji
- Formularz wymaga podania nicku i hasła
- System weryfikuje, czy podany nick nie jest już zajęty
- Po poprawnej rejestracji użytkownik jest automatycznie zalogowany, oraz przekierowywany do swojej pustej biblioteki
- Użytkownik otrzymuje komunikat o pomyślnej rejestracji w formie prostego pop-upu

### US-002: Logowanie użytkownika
Jako zarejestrowany użytkownik, chcę zalogować się do aplikacji, aby uzyskać dostęp do mojej biblioteki gier.

Kryteria akceptacji:
- Na stronie głównej dostępny jest formularz logowania
- Formularz wymaga podania nicku i hasła
- System weryfikuje poprawność danych logowania
- Po poprawnym logowaniu użytkownik jest przekierowywany do swojej biblioteki
- W przypadku błędnych danych logowania, użytkownik otrzymuje odpowiedni komunikat błędu

### US-003: Wylogowanie użytkownika
Jako zalogowany użytkownik, chcę wylogować się z aplikacji, aby zakończyć sesję.

Kryteria akceptacji:
- Na każdej stronie aplikacji (gdy użytkownik jest zalogowany) dostępny jest przycisk "Wyloguj"
- Po kliknięciu przycisku "Wyloguj" sesja użytkownika jest zamykana
- Po wylogowaniu użytkownik jest przekierowywany na stronę główną
- Wylogowany użytkownik nie ma dostępu do zasobów wymagających zalogowania

### US-004: Przeglądanie biblioteki gier
Jako zalogowany użytkownik, chcę przeglądać moją bibliotekę gier, aby zobaczyć wszystkie moje gry planszowe.

Kryteria akceptacji:
- Biblioteka wyświetla gry w formie kafelków (4 w rzędzie)
- Każdy kafelek zawiera nazwę gry i standardową ikonę emoji
- Gry z ostrzeżeniem mają pomarańczową ramkę
- Gry z alarmem mają czerwoną ramkę
- Na górze biblioteki widoczne są liczniki: całkowita liczba gier i liczba gier z alarmami
- Domyślne sortowanie gier jest alfabetyczne

### US-005: Dodawanie nowej gry do biblioteki
Jako zalogowany użytkownik, chcę dodać nową grę planszową do mojej biblioteki, aby śledzić jej używanie.

Kryteria akceptacji:
- W bibliotece dostępny jest przycisk "Dodaj grę planszową"
- Po kliknięciu przycisku wyświetla się formularz dodawania gry
- Formularz zawiera pola: nazwa gry, typ (dwuosobowa/wieloosobowa), data ostatniej rozgrywki
- Formularz ma selektor daty z domyślną datą dzisiejszą
- System nie pozwala na wybór daty z przyszłości
- Po pomyślnym dodaniu gry, użytkownik jest przekierowywany do biblioteki
- Nowo dodana gra jest widoczna w bibliotece

### US-006: Wyświetlanie szczegółów gry
Jako zalogowany użytkownik, chcę zobaczyć szczegóły gry, aby uzyskać więcej informacji o niej.

Kryteria akceptacji:
- Kliknięcie na kafelek gry w bibliotece przekierowuje do strony szczegółów gry
- Strona szczegółów wyświetla: nazwę gry, typ (dwuosobowa/wieloosobowa), datę ostatniej rozgrywki
- Strona szczegółów informuje o statusie gry (normalna, ostrzeżenie, alarm)
- Na stronie szczegółów dostępny jest przycisk "Zagrałem"
- Na stronie szczegółów dostępny jest przycisk powrotu do biblioteki

### US-007: Aktualizacja daty ostatniej rozgrywki
Jako zalogowany użytkownik, chcę zaktualizować datę ostatniej rozgrywki w grę, aby śledzić jej używanie.

Kryteria akceptacji:
- Na stronie szczegółów gry dostępny jest przycisk "Zagrałem"
- Po kliknięciu przycisku "Zagrałem" data ostatniej rozgrywki jest aktualizowana na dzisiejszą
- Po aktualizacji wyświetla się popup potwierdzający przez 3 sekundy
- Status gry (normalna, ostrzeżenie, alarm) jest aktualizowany na podstawie nowej daty
- Użytkownik pozostaje na stronie szczegółów gry

### US-008: Filtrowanie gier z alarmami
Jako zalogowany użytkownik, chcę filtrować gry z alarmami, aby łatwo identyfikować rzadko używane gry.

Kryteria akceptacji:
- W bibliotece dostępny jest przełącznik/checkbox "Pokaż tylko gry z alarmami"
- Po włączeniu filtra, w bibliotece wyświetlane są tylko gry z alarmami lub ostrzeżeniami
- Po wyłączeniu filtra, w bibliotece wyświetlane są wszystkie gry
- Stan filtra jest zachowywany podczas sesji użytkownika

### US-009: Logowanie jako administrator
Jako administrator, chcę zalogować się do panelu administracyjnego, aby zarządzać systemem.

Kryteria akceptacji:
- Panel administracyjny dostępny jest pod dedykowanym adresem
- Logowanie do panelu wymaga podania poświadczeń administratora
- Po poprawnym logowaniu administrator ma dostęp do panelu administracyjnego Django
- Panel administracyjny umożliwia zarządzanie użytkownikami i grami

### US-010: Zarządzanie użytkownikami
Jako administrator, chcę zarządzać użytkownikami w systemie, aby utrzymać porządek.

Kryteria akceptacji:
- W panelu administracyjnym dostępna jest sekcja zarządzania użytkownikami
- Administrator może przeglądać listę wszystkich użytkowników
- Administrator może dodawać nowych użytkowników
- Administrator może resetować hasła użytkowników
- Administrator może usuwać użytkowników

### US-011: Przeglądanie wszystkich gier w systemie
Jako administrator, chcę przeglądać wszystkie gry w systemie, aby mieć pełny obraz zawartości.

Kryteria akceptacji:
- W panelu administracyjnym dostępna jest sekcja zarządzania grami
- Administrator może przeglądać listę wszystkich gier w systemieŁ
- Lista gier zawiera informacje: nazwa, użytkownik, typ, data ostatniej rozgrywki
- Administrator może filtrować i sortować listę gier

## 6. Metryki sukcesu

### Metryki produktowe
1. Liczba zarejestrowanych użytkowników
2. Liczba dodanych gier planszowych
3. Liczba aktualizacji dat rozgrywek (kliknięć przycisku "Zagrałem")Ł

### Kryteria sukcesu MVP
1. 90% użytkowników jest w stanie zarejestrować się bez pomocy
2. 95% użytkowników jest w stanie dodać nową grę do biblioteki bez pomocy
3. 100% gier jest poprawnie oznaczanych ostrzeżeniami i alarmami
4. 80% użytkowników rozumie znaczenie kolorystycznych oznaczeń gier