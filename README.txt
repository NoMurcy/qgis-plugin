# Projekt 2 - Wtyczka dla programu QGIS
## Opis wtyczki:
Wtyczka Basic Calculations pozwala na wykonywanie prostych obliczeń w programie QGIS. Za jej pomocą jesteśmy w stanie obliczyć przewyższenie między dwoma punktami oraz pole powierzchni obszaru. 

## Wymagania do obsługi wtyczki 
Projekt tworzony był za pomocą Pythona w wersji 3.11.5. Zaimportowane biblioteki niezbędne do działania programu to ‘numpy’, ‘PyQt5’, ‘qgis.core’,  ‘qgis.utilis’ oraz ‘qgis.PyQt’

## Działania w interfejsie użytkownika:

Po zainstalowaniu oraz włączeniu naszej wtyczki wyświetli się interfejs użytkownika, posiadający następujące funkcje wyboru parametrów: 
* `Wybierz warstwę:` jest to funkcja pozwalająca na wybór warstwy na której znajdują się zaznaczone przez nas punkty w programie QGIS. Rozwijana lista pozwala na wybór dowolnej warstwy istniejącej na aktywnym projekcie. 
* `Przewyższenie:` jest to opcja pozwalająca na obliczenie przewyższenia między dwoma dowolnymi punktami. Wymaganiem dla tej funkcji jest zdefiniowana wysokość punktów.
* `Pole:` jest to opcja pozwalająca na obliczenie pola zaznaczonymi między minimum trzema punktami.
* `Jednostka:` jest to opcja pozwalająca użytkownikowi na wybranie jednostki w której wyświetlą się wyniki wykonanych obliczeń (metry kwadratowe, ary, hektary).
* `Utwórz i oblicz poligon` funkcja tworzy dodatkową warstwę o nazwie poligon między punktami które zostały przez nasz oznaczone.
* `Wczytywanie pliku` pozwala użytkownikowi na wczytanie pliku ze współrzędnymi. Program następnie umieszcza te punkty jako nową warstwę. 
Podczas wczytywania pliku musimy pamiętać o wybraniu odpowiednich ustawień. 
* `Układ` jest to opcja pozwalająca na wybranie układu odniesienia w którym znajdują się współrzędne punktów z pliku. 
* `Wczytaj` za pomocą tego przycisku wyszukujemy z plików znajdujących się na naszym urządzeniu plik ze współrzędnymi punktów. 
* `Strefa` jest to funkcja pozwalająca wprowadzić strefie w której znajdują się współrzędne punktu w przypadku gdy wybieramy układ PL-2000.
* `Czyść wyniki` opcja ta pozwala na usunięcie wyników z poprzedniego pomiaru wyświetlających się w interfejsie.
* `Zaznacz nowe` jest to opcja pozwalająca na zaznaczenie punktów między którymi chcemy obliczyć przewyższenie lub pole.

## Wybór punktów 

Aby skorzystać z funkcji obliczania pola użytkownik musi na początek zaznaczyć punkty między którymi chce wykonać obliczenia za pomocą funkcji programu QGIS `Zaznacz obiekty` lub funkcji umieszczonej na interfejsie użytkownika `Zaznacz nowe`.
Ważne jest aby wiedzieć na jakiej warstwie znajdują się punkty przez nas zaznaczone, aby później w funkcji `Wybierz warstwę` na pewno zaznaczyć odpowiednią opcję.

## Plik zewnętrzny 

Aby wczytać plik zewnętrzny za pomocą wtyczki trzeba zachować odpowiedni format. Współrzędne punktów muszą zostać podane w kolumnach gdzie pierwsza stanowi X [m], a druga Y [m], kolumny należy oddzielić spacją. Jeżeli wartość X i Y mają wartości dziesiętne, to muszą zostać one oddzielone kropką (np. 6495761.020010711 5700346.070648875). Plik musi mieć rozszerzenie .txt lub .csv .

## Błędy 

Program oblicza pole powierzchni metodą Gaussa, jednakże czasem nie zachowuje stałej skrętności przechodzenia na punkty po długości boków poligonu, a zmienia ją w trakcie obliczania pola. Oznacza to, że zaczyna obliczanie zgodnie z ruchem wskazówek zegara ,a następnie zmienia kierunek na przeciwny.Ten błąd widać dopiero w momencie narysowania poligonu przez wtyczkę. Niestety nie udało nam się wyeliminować tego błędu i na określonych poligonach będzie on pojawiał się zawsze. 