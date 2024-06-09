# Projekt 2 - Wtyczka dla programu QGIS
## Opis wtyczki:
Wtyczka Basic Calculations pozwala na wykonywanie prostych obliczeń w programie QGIS. Za jej pomocą jesteśmy w stanie obliczyć przewyższenie między dwoma punktami oraz pole powierzchni obszaru. 

## Wymagania do obsługi wtyczki 
Projekt tworzony był za pomocą Pythona w wersji 3.11.5. Zaimportowane biblioteki niezbędne do działania programu to ‘numpy’, ‘PyQt5’, ‘qgis.core’,  ‘qgis.utilis’ oraz ‘qgis.PyQt’

## Działania w interfejsie użytkownika:

Po zainstalowaniu oraz włączeniu naszej wtyczki wyświetli się interfejs użytkownika, wyglądający następująco 
![interfejs]("grafiki/interfejs.png")
Dla ułatwienia opisu funkcji na załączonym obrazku każdej opcji przypisany został numer. 
* `1 - Choose layer:` jest to funkcja pozwalająca na wybór warstwy na której znajdują się zaznaczone przez nas punkty w programie QGIS. Rozwijana lista pozwala na wybór dowolnej warstwy istniejącej na aktywnym projekcie. 
![warstwy]("./qgis-plugin/warstwy.png")
* `2 - Przewyższenie:` jest to opcja pozwalająca na obliczenie przewyższenia między dwoma dowolnymi punktami. Wymaganiem dla tej funkcji jest zdefiniowana wysokość punktów.
* `3 - Pole:` jest to opcja pozwalająca na obliczenie pola zaznaczonymi między minimum trzema punktami.
* `4 - Jednostka:` jest to opcja pozwalająca użytkownikowi na wybranie jednostki w której wyświetlą się wyniki wykonanych obliczeń.
![jednostki]("./qgis-plugin/jednostki.png")
* `5 - Utwórz i oblicz poligon` funkcja tworzy dodatkową warstwę o nazwie poligon między punktami które zostały przez nasz oznaczone.
![poligon]("./qgis-plugin/poligon.png")
* `Wczytywanie pliku` pozwala użytkownikowi na wczytanie pliku ze współrzędnymi. Program następnie umieszcza te punkty jako nową warstwę. 
Podczas wczytywania pliku musimy pamiętać o wybraniu odpowiednich ustawień. 
* `6 - Układ` jest to opcja pozwalająca na wybranie układu odniesienia w którym znajdują się współrzędne punktów z pliku. 
![układ]("./qgis-plugin/układ.png")
* `7 - Wczytaj` za pomocą tego przycisku wyszukujemy z plików znajdujących się na naszym urządzeniu plik ze współrzędnymi punktów. 
* `8 - Strefa` jest to funkcja pozwalająca wprowadzić strefie w której znajdują się współrzędne punktu w przydatku gdy wybieramy układ PL-2000.
![strefa]("./qgis-plugin/strefa.png")

## Wybór punktów 

Aby skorzystać z funkcji obliczania pola użytkownik musi na początek zaznaczyć punkty między którymi chce wykonać obliczenia za pomocą funkcji programu QGIS `Zaznacz obiekty`.
Ważne jest aby wiedzieć na jakiej warstwie znajdują się punkty przez nas zaznaczone, aby później 

## Plik zewnętrzny 

Aby wczytać plik zewnętrzny za pomocą wtyczki trzeba zachować odpowiedni format. Współrzędne punktów muszą zostać podane w kolumnach gdzie pierwsza stanowi X [m], a druga Y [m]. Plik musi mieć rozszerzenie .txt.


