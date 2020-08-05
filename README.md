# WYKAZ_CZASOPISM_2019

## Bit of history ...
In 2019 [Ministry of Science and Higher Education in Poland](https://www.gov.pl/web/science) announced updated list of journals and conferences (available [here](https://www.bip.nauka.gov.pl/akty-prawne-mnisw/komunikat-ministra-nauki-i-szkolnictwa-wyzszego-z-dnia-31-lipca-2019-r-w-sprawie-wykazu-czasopism-naukowych-i-recenzowanych-materialow-z-konferencji-miedzynarodowych-wraz-z-przypisana-liczba-punktow.html) in Polish). Every scientist that would publish in any of selected journals or would attend to any of selected conferences will gain special points. These points are important during grant or scholarship application and provide some measure of scientist's excellence. We, scientists are not necessarily satisfied with that solution, thus we locally call this phenomenon the "punktoza". 

## Usage

Go to the project folder and run following command in your terminal:

```
$ python WYKAZ.py
```

After loading you will see:

```
$ python WYKAZ.py 
Loading database ...
Ready !
Choose: 
1 - Search
0 - EXIT 
```

Type `0` and hit ENTER to exit the program.
Type `1` and hit ENTER to proceed to selection menu:

```
Let's search !
Choose: 
1 - Journals
2 - Conferences 
0 - EXIT 
```

Choose `1` to search the list of journals or `2` to search the list of conferences.
After selection you will be asked to provide range of points of your scope (integer numbers).
Enter positive integer number (range 0 to 200) and hit ENTER to provide a limit on minimum number of points.
Do it again for maximum number of points.

For example:

```
Chosen JOURNALS !
Minimum points : 
5    
Maximum points : 
100
(OPTIONAL) Partial name OR single keywords (separate with ; ) : 
```
You will be asked to enter names or keywords separated with semicolons.
You can also hit ENTER without providing names or keywords.

After this you will see the results like this:

```
                                                                                                Tytuł 1  Punkty
264   IEEE Journal of Selected Topics in Signal Processing                                               200.0 
268   IEEE SIGNAL PROCESSING MAGAZINE                                                                    200.0 
275   IEEE TRANSACTIONS ON IMAGE PROCESSING                                                              200.0 
474   MECHANICAL SYSTEMS AND SIGNAL PROCESSING                                                           200.0 
2048  NeuroImage-Clinical                                                                                140.0 
1474  IEEE TRANSACTIONS ON SIGNAL PROCESSING                                                             140.0 
1481  IEEE-ACM Transactions on Audio Speech and Language Processing                                      140.0 
1354  FUEL PROCESSING TECHNOLOGY                                                                         140.0 
1961  MATERIALS SCIENCE AND ENGINEERING A-STRUCTURAL MATERIALS PROPERTIES MICROSTRUCTURE AND PROCESSING  140.0 
1974  MEDICAL IMAGE ANALYSIS                                                                             140.0 
1782  JOURNAL OF MATERIALS PROCESSING TECHNOLOGY                                                         140.0 
2296  SIGNAL PROCESSING                                                                                  140.0 
1502  INFORMATION PROCESSING & MANAGEMENT                                                                140.0 
2047  NEUROIMAGE                                                                                         140.0
```

## Examples

### Search for particular journal / conference score

### Search for conference if you remeber only part of the name 

### Search for journal matching keywords and with score more than 150 points

### Search for IEEE conferences with score of 200

