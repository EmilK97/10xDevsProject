### Główny problem
Manualne śledzenie gier planszowych w w dużej kolekcji jest trudne, co sprawia że często posiadamy zbyt dużo gier planoszwych, w które nigdy nie gramy.
Rozwiązaniem będzie aplikacja webowa umożliwiająca użytkownikowi prowadzenie swojej bilioteki gier planszowych, które posiada, oraz śledzenie daty ostatniej rozgrywki w daną grę planszową. Jeśli rozgrywka w gre planszową nie odbyła się przez długi okres czasu, gra planszowa powinna być oznaczona alarmem.

### Najmniejszy zestaw funkcjonalności
- Strona pozwala użytkownikowi śledzić swoją kolekcję gier planszowych oraz identyfikować te, w które gra na tyle rzadko, że warto rozważyć ich pozbycie się.
- Prosty system kont użytkowników do powiązania użytkownika z notatkami
- Użytkownik ma dostęp do bilbioteki gier plansozwych przypisanej do jego profilu.
- Strona profilu użytkownika służąca do wyświetlania bilbioteki.
- Użytkownik może dodać grę planszową do swojej biblioteki.
- Każda gra planszowa jest skategoryzowana według liczby graczy: dwuosobowa lub wieloosobowa.
- Dodając grę planszową do swojej bilbioteki, użytkownik musi podać jej nazwę, określić datę ostatniej rozgrywki oraz określić czy jest dwuosobowa, czy wieloosbowa.
- Użytkownik może wejść na stronę z detalami każdej gry planszowej i kliknąć przycisk „Zagrałem”, który resetuje datę ostatniej rozgrywki do dnia dzisiejszego.
- Jeśli ostatnia data zagrania jest starsza niż rok, gra planszowa zostaje oznaczona ostrzeżeniem – sugerującym, że jest rzadko używana.
- Jeśli ostatnia data zagrania jest starsza niż 3 lata, gra planszowa zostaje objęta alarmem – sugerującym, że gry warto się pozbyć.

### Co NIE wchodzi w zakres MVP
- Moźliwość oceniania jakośći gier w skali 1-10.
- Wysyłania powiadomień mailowych odnośnie alarmów o stanie gier.
- Współdzielenie zestawów gier pomiędzy użytkownikami
- Integracje z innymi platformami internetowymi
- Aplikacje mobilne (na początek tylko web)

### Kryteria sukcesu
- Użytkownik jest w stanie łatwo stworzyć swój profil.
- Użytkownik jest w stanie łatwo dodać nowę grę do swojej bilbioteki.
- Odpowiednie oznaczenia gier: ostrzeżenie i alarm, zostają wizualnie oznaczone na widoku bilbioteki użytkownika.