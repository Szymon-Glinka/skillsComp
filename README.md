<p align="center">
  <img src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/61ca9152-2164-4cfa-b2b0-14bd25c4e0f3">
</p>
<p align="center">
  <img alt="Static Badge" src="https://img.shields.io/badge/skillsComp-Robotyka_Mobilna-blue">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/t/Szymon-Glinka/skillsComp-semifinals">
  <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/Szymon-Glinka/skillsComp-semifinals">
</p>


# Tłumaczenia:
* [ENGLISH](https://github.com/Szymon-Glinka/skillsComp-semifinals/edit/main/README.md)
* [POLSKI](https://github.com/Szymon-Glinka/skillsComp-semifinals/blob/main/README.pl.md)

# O projekcie
To repzytorium zawiera rozwiązane wszystkie zadania półfinałowe [SkillsComp - Robotyka Mobilna](https://skillscomp.itee.radom.pl/service/robotyka-mobilna/) razem z wszystkimi plikami użytymi podczas tworzenia tych programów (foldery ```test```).  
*logo zostało wygenerowane przy pomocy [simple logo generator](https://creecros.github.io/simple_logo_gen/)*

# Spis treści:
* [Maze Solver](#MazeSolver)
* [PID](#PID)
* [Color Recognition](#ColorRecognition)
* [Reading QR codes](#ReadingQR)

# MazeSolver
<p align="center"><img width="800" src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/f0805cfc-add5-4541-b7c3-a47464567184"></p>

### Informacje o programie
Program ten jest rozwiązaniem pierwszego zadania, znajduje się w folderze **_maze_**.
Program rozwiązujący labirynty składa się z dwóch plików Python'a: ```mazeSolver.py``` i ```backendSolvable.py``` 
W pliku ```backendSolvable.py``` znajdują się wszystkie funkcje używane do rozwiązania labiryntu, importowania labiryntu z pliku tekstowego, przygotowywania zaimportowanego labiryntu do rozwiązania, znajdowania początku labiryntu i wytaczania ścieżki do wyjscia.  
W pliku ```mazeSolver.py``` znajduje się funckja rozwiązująca labirynt (sprawdzanie czy da się go rozwiązać, jeśli się nie da to dlaczego) przy pomocy wszystkich funkcji w pliku ```backendSolvable.py```.   

### Zasada działania
Program sprawdza czy dookoła obecnego położenia są wolne komórki - " ", jeżeli tak zapisuje wszystkie pozycje do których jest w stanie *przejść* w następnym kroku. Następnie wykonuje możliwy ruch usuwając go jednocześnie z listy ruchów możliwych do wykonania, a poprzednią pozycje dodaje do tabeli z poprzednimi popzycjami. Jeżeli dana pozycja nie ma żadnego możliwego ruchu do wykonania, progam wraca do innych możliowych pozycji (jeżeli takie zostały zapisane podczas np. jakiegoś rozwidlenia).  
Algorytm zwraca ```True``` jeżeli dotarł do wyjścia **E** i liste z dokładnym rozwiązaniem labiryntu, np. **_['RIGHT', 'RIGHT', 'RIGHT', 'DOWN', 'DOWN', 'DOWN']_**. Jeżeli program nie jest we stanie dotrzeć do wyjścia zwróci ```False``` oraz dlaczego nie rozwiązał labiryntu, np. **_E3 - multiple starting positions for letter 'r'_** - oznacza, to że w podanym labiryncie znajduje się więcej niż jedno rozpoczęcie (więcej niż jedna litera, od której program ma zacząć rozwiązywanie)

### Używanie programu do rozwiązania labiryntu
Aby rozwiązać wybrany labirynt należy:   
* wpisać lokalizację pliku tekstowego z tym labiryntem   
```maze = getMazeFromTXT(r"TUTAJ LOKALIZACJA PLIKU")```   
NP.  
```maze = getMazeFromTXT(r"F:\skillscomp\z1textFiles\labirynt9.txt")```  
* wpisać jaka litera oznacza pozycję od której program ma zacząć rozwiązywanie labiryntu  
```solvable, info = mazeSolver(maze, "LITERA")```   
NP.   
```solvable, info = mazeSolver(maze, "r")``` - Program rozwiąże labirynt dla małej litery **_r_**

### Debugowanie
Aby wyświetlić dane do debagowania należy w poniższej lini zmienić **_level=logging.ERROR_** na **_level=logging.DEBUG_**   
```logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M")```


# PID
<p align="center"><img width="800" src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/a8ec10c5-6833-4c41-a882-81c891f7b855"></p>

### Informacje o programie
Ta aplikacja jest rozwiązaniem 2 zadania, znajduje się w folderze **_pid_** i składa się z dwóch plików,    
aplikacji ```app.py``` oraz algorytmu PID i obiektu sterowanego w pliku ```pid.py```

### Obiekt sterowany
Poniżej został przedstawiony użyty obiekt drugiego rzędu, którym steruje regulator PID.
<p align="center"><img width="200" src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/cb9bb9f6-730f-4670-824b-38677b2fcbfa"></p>

### Zasada działania
Program pobiera dane wprowadzone przez użytkownika i używa ich do symulacji regulatora PID. Aby wyświetlić wykres symulacji należy nacisnać przycisk ```Submit```   
Jeżeli opcja ```Ziegler-nichols autotuning``` nie jest zaznaczona, użytkownik może ręcznie dobierać nastawy (za pomocą suwaków lub wprowadzając z klawiatury)   
Jeżeli opcja ```Zeigler-nichols autotuning``` jest zaznaczona, program wyświetli wykres symulacji regulatora PID dla nastaw obliczonych za pomocą metody Zeiglera-nicholsa   
Dodatkowo użytkownik może zmienić poniższe wartości:
* Cel symulacji, domyślnie 100
* Wartość początkową, domyślnie 0
* ilość powtórzeń, domyślnie 250
* zmianę czasu, domyślnie 0.1

### Metoda dobierania nastaw Zeiglera-nicholsa
Oscylacja układu została wyznaczona eksperymentalnie, używając ręcznej manipulacji nastaw w aplikacji.   
Układ oscyluje przy nastawach: Ki = 0, Kd = 0, Kp = 7.(27)  czyli Ku = 7.(27)   
Okres oscylacji układu (Tu): 0.1s   
Do wyznaczenia nastaw użyto poniższych wzorów:  
* Kp = 0.6 * Ku = 0.6 * 7.(27) = +-4.36
* Ki = 0.5 * Tu = 0.5 * 0.1 = 0.05
* Kd = 0.125 * Tu = 0.125 * 0.1 = 0.0125


# ColorRecognition
<p align="center"><img width="800" src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/f139313b-e086-4672-896f-35e4f989a99e"></p>

### Informacje o programie
Ten program jest rozwiązaniem trzeciego zadania, znajduje się w folderze **_colorRecogniotion_** i składa się z dwóch plików,    
aplikacji ```app.py``` oraz algorytmów rozpoznających i zaznaczających kolory w pliku ```backend.py```

### Zasada działania
Kiedy użytkownik zaimportuje wybrany obraz i naciśnie przycisk ```Detect Colors```, program wykona dwie funkcje:  
* Funkcja pierwsza ```detectColor_markOutlines()```. Wykryje kolor, stworzy maskę, gdzie tylko ten kolor jest zaznaczony, wyznaczy zarys i doda ten zarys do ostatecznej grafiki (sam obrys na czarnym tle). Ta funkcja wykona się 4 razy dla każdego z zdefiniowanego w programie koloru (czerwony, zielony, niebieski, żółty). Ta funkcja również zwraca jakie kolory zostały wykryte.
* Funckja druga ```detectPositionsOfColors()```. Wykrywa kolory i je zaznacza na tym samym zdjęciu, z którego kolory zostały wykryte. Dodatkowo funkcja ta zwraca słownik - nazwę koloru jako klucz i przpisaną do niego wartość jako tuple, w którym znajdują się: odległość środka prostokąta (prostokątem jest oznaczony wykryty przedmiot w daynym kolorze) od lewego górnego rogu w osi X oraz w osi Y, pozycja środka tego zaznaczenia w odniesieniu od środka ekranu (left, right, top, bottom) oraz odległość tego zaznaczenia od środka obrazu w osi X i Y

### Zapisywanie danych do pliku tekstowego
Dodatkową funkcją programu jest możliwość zapisania danych do pliku tekstowego przyciskiem ```Plot Data```

  
# ReadingQR
<p align="center"><img width="800" src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/5b9c1ccb-1544-4b63-a660-e38b3b336449"></p>

### Informacje o programie
Program ten jest rozwiązaniem czwartego zadania, znajduje się w folderze **_qrCode_** i składa się z dwóch plików,   
aplikacji ```app.py``` oraz algorytmów przekształcających i rozpoznających kody QR ```backend.py```

### Zasada działania
Kiedy użytkownik zaimportuje kod QR i naciśnie przycisk ```detect QR```, program wykona poniższe funkcje. Jeżeli jednej z poniższych funkcji uda się odczytać kod QR, pozostałe nie zostaną wykonane:     
Najpierw program zastosuje poszczególne filtry dla pierwotnego zdjęcia:     
* znajdzie rogi kodu QR i go "wyprostuje" poczym spróbuje odczytać kod QR
* zastosuje rozmycie Gaussa i spóbuje odczytać kod QR
* użyje funkcji ```fixBlur()```, której zadaniem jest pozbycie się rozmazania obrazu, nastęnie spróbuje odczytać kod QR
  
Jeżeli żadnej z powyższych funkcji nie udało się odczytać kodu QR program zastosuje poszczególne filtr dla zdjęcia wcześniej zmodyfikowanego. Program:
* znajdzie rogi kodu QR i go "wyprostuje" poczym spróbuje odczytać kod QR
* użyje zdjęcia uzyskanego przez użycie powyższego filtra i zastosuje rozmycie Gaussa, a następnie spróbuje odczytać kod QR
* wykona funkcję ```fixBlur()``` na zdjęciu uzyskanym po zastosowaniu rozmycia Gaussa i spróbuje odczytać kod QR
  
Jeżel żadnej z powyższych funkcji nie uda się odczytać kodu QR program zwróci **_No QR code detected_**

### Zapisywanie danych do pliku tekstowego
Dodatkową funkcją programu jest, tak jak w programie **_colorRecognition_**, możliwość zapisania danych do pliku tekstowego przyciskiem ```Plot Data```
