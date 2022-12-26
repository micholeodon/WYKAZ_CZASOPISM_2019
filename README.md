# UPDATE 26.XII.2022

This repository contains outdated excel sheet.

For now, I recommend using another (not my authorship) tool here - https://punktoza.pl/
It is more frequently updated and convenient to use.
Enjoy!

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

```
Choose: 
1 - Search
0 - EXIT 
1
Let's search !
Choose: 
1 - Journals
2 - Conferences 
0 - EXIT 
1
Chosen JOURNALS !
Minimum points : 
0
Maximum points : 
200
(OPTIONAL) Partial name OR single keywords (separate with ; ) : 
cerebral cortex
['cerebral cortex']
              Tytuł 1  Punkty
1028  CEREBRAL CORTEX  140.0 
Choose: 
1 - Search
0 - EXIT
```

### Search for conference if you remeber only part of the name 

```
Choose: 
1 - Search
0 - EXIT 
1
Let's search !
Choose: 
1 - Journals
2 - Conferences 
0 - EXIT 
2
Chosen CONFERENCES !
Minimum points : 
0
Maximum points : 
200
(OPTIONAL) Partial name OR single keywords (separate with ; ) : 
international conference on acoustics
['international conference on acoustics']
                                                            Tytuł konferencji  Liczba punktów
696  IEEE International Conference on Acoustics, Speech and Signal Processing  70            
Choose: 
1 - Search
0 - EXIT
```


### Search for journals matching one of few keywords and with score more than 150 points

```
Choose: 
1 - Search
0 - EXIT 
1
Let's search !
Choose: 
1 - Journals
2 - Conferences 
0 - EXIT 
1
Chosen JOURNALS !
Minimum points : 
151
Maximum points : 
200
(OPTIONAL) Partial name OR single keywords (separate with ; ) : 
brain ; psychology ; human
['brain', 'psychology', 'human']
                                                                                                                                                                                   Tytuł 1  Punkty
290  Industrial and Organizational Psychology-Perspectives on Science and Practice                                                                                                          200.0 
738  Annual Review of Psychology                                                                                                                                                            200.0 
218  European Review of Social Psychology                                                                                                                                                   200.0 
152  CLINICAL PSYCHOLOGY REVIEW                                                                                                                                                             200.0 
370  JOURNAL OF HUMAN RESOURCES                                                                                                                                                             200.0 
182  Dialogues in Human Geography                                                                                                                                                           200.0 
244  GLOBAL ENVIRONMENTAL CHANGE-HUMAN AND POLICY DIMENSIONS                                                                                                                                200.0 
340  JOURNAL OF APPLIED PSYCHOLOGY                                                                                                                                                          200.0 
563  PERSONNEL PSYCHOLOGY                                                                                                                                                                   200.0 
562  PERSONALITY AND SOCIAL PSYCHOLOGY REVIEW                                                                                                                                               200.0 
751  Vital & health statistics. Series 3, Analytical and epidemiological studies / [U.S. Dept. of Health and Human Services, Public Health Service, National Center for Health Statistics]  200.0 
109  BRAIN                                                                                                                                                                                  200.0 
41   AMERICAN JOURNAL OF HUMAN GENETICS                                                                                                                                                     200.0 
617  Psychology of Religion and Spirituality                                                                                                                                                200.0 
599  PROGRESS IN HUMAN GEOGRAPHY                                                                                                                                                            200.0 
389  JOURNAL OF PERSONALITY AND SOCIAL PSYCHOLOGY                                                                                                                                           200.0 
260  HUMAN REPRODUCTION UPDATE                                                                                                                                                              200.0 
95   BEHAVIORAL AND BRAIN SCIENCES                                                                                                                                                          200.0 
Choose: 
1 - Search
0 - EXIT
```

### Search for IEEE conferences with score of 200

```
Choose: 
1 - Search
0 - EXIT 
1   
Let's search !
Choose: 
1 - Journals
2 - Conferences 
0 - EXIT 
2
Chosen CONFERENCES !
Minimum points : 
200
Maximum points : 
200
(OPTIONAL) Partial name OR single keywords (separate with ; ) : 
IEEE
['IEEE']
                                                          Tytuł konferencji  Liczba punktów
32  IEEE Information Visualization Conference                                200           
33  IEEE International Conference on Computer Vision                         200           
34  IEEE International Conference on Data Mining                             200           
35  IEEE International Conference on Pervasive Computing and Communications  200           
36  IEEE International Symposium on Wearable Computing                       200           
37  IEEE Symposium on Foundations of Computer Science                        200           
38  IEEE Symposium on Logic in Computer Science                              200           
39  IEEE Symposium on Security and Privacy                                   200           
40  IEEE/ACM International Symposium on Mixed and Augmented Reality          200           
65  IEEE International Conference on Computer Communications                 200           
31  IEEE Conference on Computer Vision and Pattern Recognition               200           
Choose: 
1 - Search
0 - EXIT 
```
