
<conversation_summary>
<decisions>
1. Aplikacja będzie przechowywać podstawowe informacje o grach: nazwa, data ostatniej rozgrywki, typ (dwuosobowa/wieloosobowa).
2. System autentykacji będzie prosty - tylko nick i hasło, bez resetu hasła czy usuwania konta.
3. Użytkownik nie będzie mógł edytować ani usuwać gier ze swojej biblioteki.
4. Domyślne sortowanie gier będzie alfabetyczne, z opcją filtrowania tylko gier z alarmami lub ostrzeżeniami.
5. Gry będą oznaczane pomarańczową ramką (ostrzeżenie) lub czerwoną ramką (alarm).
6. Nie będzie możliwości dostosowania progów czasowych dla alarmów (stałe 1 rok - ostrzeżenie, 3 lata - alarm).
7. Aplikacja będzie zbudowana w technologii Python (Django) z prostym frontendem (CSS, HTML, JavaScript).
8. Kafelki gier będą miały jednolity rozmiar, po 4 kafelki w rzędzie.
9. Dozwolone będą duplikaty gier bez ostrzeżeń.
10. Wykorzystany zostanie domyślny panel admina Django.
11. Kafelki gier będą zawierać tylko nazwę gry i standardową ikonę emoji.
12. Przycisk "Zagrałem" będzie dostępny tylko na stronie szczegółów gry.
13. Formularz dodawania gry będzie miał selektor daty z domyślną datą dzisiejszą.
14. Aplikacja będzie mieć jednolity nagłówek/stopkę dla wszystkich stron.
15. Zalogowany użytkownik będzie miał możliwosć wylogowania się poprzez kliknięcie przycisku 'Wyloguj'.
16. Popup potwierdzający zagranie będzie wyświetlany przez 3 sekundy.
17. Nazwa aplikacji: "BoardGameTracker".
18. Nie ma wymagań dotyczących responsywności na urządzeniach mobilnych.
19. Niemożliwe będzie dodanie gry z datą rozgrywki w przyszłości.
20. Kolorystyka: biały dominujący kolor z jasnoniebieskimi elementami interaktywnymi.
</decisions>

<matched_recommendations>
1. Struktura aplikacji podzielona na cztery główne widoki: strona główna (logowanie/rejestracja), biblioteka użytkownika, formularz dodawania gry, oraz widok szczegółów gier plansowej, gdzie dostępny będzie przycisk "Zagrałem".
2. Kafelki gier z wyraźnym oznaczeniem kolorystycznym (pomarańczowa ramka dla ostrzeżeń, czerwona dla alarmów).
3. Liczniki na górze biblioteki wyświetlające całkowitą liczbę gier oraz liczbę gier z alarmami.
4. Prosty model danych: nazwa gry, data ostatniej rozgrywki, typ (dwuosobowa/wieloosobowa), odniesienie do użytkownika.
5. Wykorzystanie domyślnego systemu autentykacji Django z minimalnymi modyfikacjami (tylko nick i hasło).
6. Przełącznik/checkbox "Pokaż tylko gry z alarmami" nad biblioteką gier.
7. Prosty, nowoczesny interfejs z dominującym białym tłem i jasnoniebieskimi elementami interaktywnymi.
8. Popup potwierdzający aktualizację daty po naciśnięciu przycisku "Zagrałem" (wyświetlany przez 3 sekundy).
9. Walidacja dat w formularzu dodawania gry, uniemożliwiająca wybór dat z przyszłości.
10. Jednolity układ kafelków (4 w rzędzie) z prostym designem (nazwa i emoji).
</matched_recommendations>

<prd_planning_summary>
BoardGameTracker to aplikacja webowa zaprojektowana, aby pomóc użytkownikom śledzić swoją kolekcję gier planszowych i identyfikować te, które są rzadko używane.

**Główne wymagania funkcjonalne:**
- Prosty system rejestracji i logowania (tylko nick i hasło)
- Biblioteka gier planszowych przypisana do profilu użytkownika
- Możliwość dodawania gier planszowych (nazwa, data ostatniej rozgrywki, typ)
- Automatyczne oznaczanie gier ostrzeżeniem (ponad rok od ostatniej rozgrywki) lub alarmem (ponad 3 lata)
- Możliwość aktualizacji daty ostatniej rozgrywki poprzez przycisk "Zagrałem"
- Filtrowanie gier oznaczonych alarmem
- Wyświetlanie liczników (całkowita liczba gier i liczba gier z alarmami)
- Panel administracyjny dla zarządzania użytkownikami

**Ścieżki użytkownika:**
1. Rejestracja/logowanie:
   - Użytkownik wchodzi na stronę główną
   - Rejestruje się podając nick i hasło lub loguje się
   - Po zalogowaniu jest przekierowywany do swojej biblioteki

2. Przeglądanie biblioteki:
   - Użytkownik widzi kafelki z grami (4 w rzędzie)
   - Każdy kafelek zawiera nazwę gry i emoji
   - Gry z ostrzeżeniem mają pomarańczową ramkę
   - Gry z alarmem mają czerwoną ramkę
   - Na górze widoczne są liczniki gier
   - Możliwość filtrowania tylko gier z alarmami

3. Dodawanie gry:
   - Użytkownik klika przycisk "Dodaj grę planszową"
   - Wypełnia formularz z nazwą, typem gry i datą ostatniej rozgrywki
   - System nie pozwala na wybór daty z przyszłości
   - Gra zostaje dodana do biblioteki

4. Aktualizacja daty rozgrywki:
   - Użytkownik klika na kafelek gry
   - Przechodzi do strony szczegółów
   - Klika przycisk "Zagrałem"
   - System aktualizuje datę rozgrywki na dzisiejszą
   - Wyświetla się popup potwierdzający przez 3 sekundy

**Kryteria sukcesu:**
- Użytkownik może łatwo stworzyć profil
- Użytkownik może łatwo dodać nową grę do biblioteki
- System prawidłowo oznacza gry ostrzeżeniami i alarmami
- Interfejs jest przejrzysty i intuicyjny
- Użytkownik może szybko zidentyfikować gry, których dawno nie używał

**Interfejs użytkownika:**
- Nowoczesny design z białym tłem i jasnoniebieskimi elementami interaktywnymi
- Jednolity nagłówek i stopka na wszystkich stronach
- Przejrzysty układ kafelków w bibliotece (4 w rzędzie)
- Wyraźne oznaczenia kolorystyczne dla ostrzeżeń i alarmów
</prd_planning_summary>

<unresolved_issues>
1. Brak określenia, czy aplikacja będzie wymagać testów automatycznych.
2. Nie sprecyzowano szczegółowego wyglądu formularza dodawania gry.
3. Brak informacji o konkretnych zabezpieczeniach przed atakami na logowanie.
4. Nie omówiono szczegółowo procesu wdrożenia aplikacji (hosting, deployment).
5. Nie określono dokładnie, jakie dane będą widoczne na stronie głównej przed zalogowaniem.
6. Brak informacji na temat monitorowania błędów aplikacji.
</unresolved_issues>
</conversation_summary>
