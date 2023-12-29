<p align="center">
  <img src="https://github.com/Szymon-Glinka/skillsComp/assets/131162335/61ca9152-2164-4cfa-b2b0-14bd25c4e0f3">
</p>

# O projekcie
To repzytorium zawiera rozwiązane wszystkie zadania półfinałowe [SkillsComp - Robotyka Mobilna](https://skillscomp.itee.radom.pl/service/robotyka-mobilna/) razem z wszystkimi plikami użytymi podczas tworzenia tych programów (foldery ```test```). Dodatkowo znajduje się jeden program, który jest połączeniem wszystkich czterech zadań w jedną aplikację.  
*logo zostało wygenerowane przy pomocy [simple logo generator](https://creecros.github.io/simple_logo_gen/)*

# Spis Treści:
* [Maze Solver](#MazeSolver)
* [PID](#PID)
* [Color Recognition](#ColorRecognition)
* [Reading QR codes](#ReadingQR)
* [All in one](#All_in-one)

# MazeSolver
### Informacje o programie
Program ten jest rozwiązaniem pierwszego zadania, znajduje się w folderze *maze*.
Algorytm rozwiązujący labirynty składa się z dwóch plików Python'a: ```mazeSolver.py``` i ```backendSolvable.py``` 
W pliku ```backendSolvable.py``` znajdują się wszystkie funkcje używane do rozwiązania labiryntu, importowania labiryntu z pliku tekstowego, przygotowywania zaimportowanego labiryntu do rozwiązania oraz znajdowania początku labiryntu.  
W pliku ```mazeSolver.py``` znajduje się rozwiązywanie labirynu (sprawdzanie czy da się go rozwiązać, jeśli się nie da to dlaczego) przy użyciu funkcji w pliku ```backendSolvable.py```.   

### Zasada działania
Program sprawdza czy są dookoła obecnego położenia wolne komórki (" "), jeżeli tak zapisuje wszystkie pozycje do których jest w stanie *przejść* w następnym kroku. Wykonuje możliwy ruch usuwając go jednocześnie z listy ruchów mopżliwych do wykonania, as poprzednią pozycje dodaje do tabeli z poprzednimi ruchami. Jeżeli dana pozycja nie ma żadnego możliwegop ruchu do wykonania, progam wraca do innych możliowych pozycji (jeżeli takie zostały zapisane podczas np. jakiegoś rozwidlenia)
Algorytm zwraca ```True``` jeżeli dotarł do wyjścia ```E```. Jeżeli nie jest we stanie wykonać żadnych ruchów program zwróci False. Dodatkowo jeżeli labirynt jest niemożliwy do rozwiązania program również zwróci dlaczego, np. ```False, E5 - No solution found``` - oznacza, to że w podanym labiryncie znajduje się więcej niż jedno rozpoczęcie (więcej niż jedna litera, od której program ma zacząć rozwiązywanie)

### Używanie programu do rozwiązania labiryntu
Aby rozwiązać wybrany labirynt należy wpisać ścieżkę do pliku tekstowego z wybranym labiryntem   
```maze = getMazeFromTXT(r"TUTAJ LOKALIZACJA PLIKU") #get maze from txt file```   
NP.  
```maze = getMazeFromTXT(r"F:\skillscomp\z1textFiles\labirynt9.txt") #get maze from txt file```
Następine należy wpisać jaka litera oznacza pozycję od której program ma zacząć rozwiązywanie labiryntu  
```solvable, info = mazeSolver(maze, "LITERA") #solve the maze```   
NP.   
```solvable, info = mazeSolver(maze, "r") #solve the maze``` - Program rozwiąże labirynt dla małej litery r  
Aby wyświetlić dane do debagowania należy w tej lini   
```logging.basicConfig(level=logging.ERROR, format="%(asctime)s %(levelname)s %(message)s", datefmt="%y-%m-%d %H:%M") #logging setup```   
zmienić ```level=logging.ERROR``` na ```level=logging.DEBUG```

# PID

# ColorRecognition

# ReadingQR

# All_in-one
