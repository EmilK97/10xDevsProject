# Plan Testów dla Aplikacji BoardGameTracker

## 1. Wprowadzenie i cele testowania

Celem testowania jest zapewnienie, że aplikacja BoardGameTracker spełnia wymagania funkcjonalne i niefunkcjonalne zdefiniowane w specyfikacji MVP. Testy mają zagwarantować niezawodność, poprawność i użyteczność aplikacji w kontekście zarządzania kolekcją gier planszowych.

## 2. Zakres testów

Testowanie obejmuje wszystkie kluczowe funkcjonalności aplikacji:
- Rejestracja i uwierzytelnianie użytkowników
- Zarządzanie biblioteką gier (dodawanie, przeglądanie)
- Oznaczanie gier jako zagranych
- Automatyczne oznaczanie gier ostrzeżeniami i alarmami
- Poprawność wyświetlania statystyk kolekcji

## 3. Typy testów

### 3.1. Testy jednostkowe
- Testowanie poszczególnych modeli (UserProfile, BoardGame)
- Sprawdzenie poprawności wyliczania statusów gier
- Testowanie walidacji danych wejściowych
- Testowanie generowania losowych identyfikatorów gier

### 3.2. Testy integracyjne
- Testowanie interakcji między modelami
- Testowanie poprawności działania funkcji widoków
- Sprawdzenie poprawności obsługi żądań HTTP

### 3.3. Testy funkcjonalne
- Testowanie rejestracji i logowania użytkowników
- Testowanie procesu dodawania nowej gry
- Testowanie mechanizmu oznaczania gry jako zagranej
- Sprawdzenie poprawności wyświetlania biblioteki gier

### 3.4. Testy interfejsu użytkownika
- Weryfikacja responsywności interfejsu
- Sprawdzenie poprawności wyświetlania komunikatów o błędach
- Testowanie poprawności wyświetlania ostrzeżeń i alarmów dla gier

### 3.5. Testy bezpieczeństwa
- Testowanie ochrony przed nieautoryzowanym dostępem
- Weryfikacja poprawności mechanizmów uwierzytelniania
- Testowanie ochrony przed atakami CSRF

## 4. Scenariusze testowe

### 4.1. Rejestracja i logowanie

#### 4.1.1. Rejestracja nowego użytkownika
1. Otwarcie strony rejestracji
2. Wprowadzenie unikalnej nazwy użytkownika i hasła
3. Potwierdzenie hasła
4. Sprawdzenie, czy użytkownik został utworzony
5. Weryfikacja przekierowania do biblioteki

#### 4.1.2. Logowanie istniejącego użytkownika
1. Otwarcie strony logowania
2. Wprowadzenie poprawnych danych uwierzytelniających
3. Sprawdzenie poprawności przekierowania do biblioteki

#### 4.1.3. Próba rejestracji z istniejącą nazwą użytkownika
1. Próba rejestracji z nazwą użytkownika, która już istnieje
2. Weryfikacja wyświetlenia odpowiedniego komunikatu o błędzie

#### 4.1.4. Próba logowania z nieprawidłowymi danymi
1. Wprowadzenie niepoprawnej nazwy użytkownika lub hasła
2. Weryfikacja wyświetlenia odpowiedniego komunikatu o błędzie

### 4.2. Zarządzanie biblioteką gier

#### 4.2.1. Dodawanie nowej gry
1. Otwarcie formularza dodawania gry
2. Wprowadzenie nazwy gry, typu i daty ostatniej rozgrywki
3. Sprawdzenie, czy gra została dodana do kolekcji
4. Weryfikacja poprawności wyświetlenia w bibliotece

#### 4.2.2. Przeglądanie szczegółów gry
1. Wybranie gry z biblioteki
2. Otwarcie strony szczegółów
3. Sprawdzenie poprawności wyświetlonych informacji

#### 4.2.3. Oznaczanie gry jako zagranej
1. Otwarcie strony szczegółów gry
2. Kliknięcie przycisku "Zagrałem"
3. Weryfikacja aktualizacji daty ostatniej rozgrywki

### 4.3. Ostrzeżenia i alarmy

#### 4.3.1. Weryfikacja ostrzeżenia dla gry niezagranej od roku
1. Dodanie gry z datą ostatniej rozgrywki starszą niż rok
2. Sprawdzenie, czy gra jest oznaczona ostrzeżeniem

#### 4.3.2. Weryfikacja alarmu dla gry niezagranej od trzech lat
1. Dodanie gry z datą ostatniej rozgrywki starszą niż trzy lata
2. Sprawdzenie, czy gra jest oznaczona alarmem

#### 4.3.3. Usunięcie ostrzeżenia po oznaczeniu gry jako zagranej
1. Oznaczenie gry z ostrzeżeniem jako zagranej
2. Weryfikacja usunięcia ostrzeżenia

## 5. Środowisko testowe

### 5.1. Konfiguracja środowiska deweloperskiego
- Instalacja Python i Django zgodnie z wymaganiami w requirements.txt
- Konfiguracja lokalnej bazy danych SQLite
- Uruchomienie serwera deweloperskiego Django

### 5.2. Konfiguracja środowiska testowego
- Użycie bazy testowej SQLite
- Konfiguracja pytest dla Django
- Przygotowanie danych testowych (fixtures)

## 6. Narzędzia do testowania

### 6.1. Frameworki testowe
- pytest jako główny framework testowy
- pytest-django do integracji z Django
- pytest-cov do analizy pokrycia kodu testami

### 6.2. Narzędzia pomocnicze
- Factory Boy do generowania obiektów testowych
- Django Test Client do testowania żądań HTTP
- Selenium WebDriver do testów interfejsu użytkownika

## 7. Harmonogram testów

### 7.1. Testy przygotowawcze
- Utworzenie infrastruktury testowej
- Przygotowanie danych testowych
- Implementacja podstawowych przypadków testowych

### 7.2. Testy jednostkowe
- Implementacja testów modeli
- Implementacja testów widoków
- Implementacja testów logiki biznesowej

### 7.3. Testy integracyjne
- Testowanie interakcji między komponentami
- Testowanie przepływu danych

### 7.4. Testy funkcjonalne
- Testy pełnego przepływu pracy użytkownika
- Testy edge case'ów i obsługi błędów

### 7.5. Testy UI
- Testy responsywności
- Testy zgodności z różnymi przeglądarkami

## 8. Kryteria akceptacji testów

### 8.1. Kryteria ilościowe
- Pokrycie kodu testami na poziomie minimum 80%
- Wszystkie ścieżki krytyczne pokryte testami
- Brak błędów krytycznych w testach funkcjonalnych

### 8.2. Kryteria jakościowe
- Aplikacja spełnia wszystkie wymagania MVP
- Interfejs użytkownika jest intuicyjny i responsywny
- Aplikacja działa stabilnie pod obciążeniem

## 9. Role i odpowiedzialności

### 9.1. Inżynier QA
- Projektowanie przypadków testowych
- Implementacja automatycznych testów
- Raportowanie błędów
- Weryfikacja poprawek

### 9.2. Deweloper
- Implementacja testów jednostkowych
- Poprawianie błędów zgłoszonych przez QA
- Utrzymanie infrastruktury CI/CD
- Wykonywanie testów przed commit'em

### 9.3. Product Owner
- Definiowanie kryteriów akceptacji
- Weryfikacja zgodności z wymaganiami biznesowymi
- Priorytetyzacja błędów

## 10. Procedury raportowania błędów

### 10.1. Format zgłoszenia błędu
- Tytuł: krótki, opisowy
- Środowisko: wersja, przeglądarka, OS
- Kroki reprodukcji: kolejność działań prowadzących do błędu
- Oczekiwany rezultat: co powinno się stać
- Aktualny rezultat: co się dzieje w rzeczywistości
- Priorytet: krytyczny/wysoki/średni/niski
- Załączniki: zrzuty ekranu, logi

### 10.2. Proces obsługi błędów
1. Zgłoszenie błędu w systemie śledzenia
2. Kategoryzacja i priorytetyzacja
3. Przypisanie do dewelopera
4. Rozwiązanie błędu
5. Weryfikacja przez QA
6. Zamknięcie zgłoszenia

### 10.3. Metryki jakości
- Liczba zgłoszonych błędów
- Czas rozwiązania błędu
- Liczba ponownie otwartych błędów
- Liczba błędów według priorytetu

## 11. Załączniki

### 11.1. Wzory testów jednostkowych

```python
import pytest
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from boardGameApp.models import BoardGame, GameStatus

@pytest.mark.django_db
def test_game_status_normal():
    user = User.objects.create_user(username='testuser', password='password')
    game = BoardGame.objects.create(
        name='Test Game',
        owner=user,
        game_type='MULTI',
        last_played=timezone.now()
    )
    assert game.status == GameStatus.NORMAL

@pytest.mark.django_db
def test_game_status_warning():
    user = User.objects.create_user(username='testuser', password='password')
    game = BoardGame.objects.create(
        name='Test Game',
        owner=user,
        game_type='MULTI',
        last_played=timezone.now() - timedelta(days=366)
    )
    assert game.status == GameStatus.WARNING

@pytest.mark.django_db
def test_game_status_alarm():
    user = User.objects.create_user(username='testuser', password='password')
    game = BoardGame.objects.create(
        name='Test Game',
        owner=user,
        game_type='MULTI',
        last_played=timezone.now() - timedelta(days=3*366)
    )
    assert game.status == GameStatus.ALARM
```

### 11.2. Wzory testów widoków

```python
import pytest
from django.urls import reverse
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_login_view(client):
    User.objects.create_user(username='testuser', password='password')
    response = client.post(reverse('login'), {'username': 'testuser', 'password': 'password'})
    assert response.status_code == 302
    assert response.url == reverse('library')

@pytest.mark.django_db
def test_add_game_view(client):
    user = User.objects.create_user(username='testuser', password='password')
    client.login(username='testuser', password='password')
    response = client.post(reverse('add_game'), {
        'name': 'Test Game',
        'game_type': 'MULTI',
        'last_played': '2023-01-01'
    })
    assert response.status_code == 200
    assert response.json()['success'] is True
```
```