# Pizzaz-Cinema

## Description

The program will allow users to view the available movies, order tickets for one or multiple persons, and make transactions on the orders.

Schedule of movies, their times and room:
```
The Shining. 1980. 2h 26m. 10:00. Room 1
Your Name. 2016. 1h 52m. 13:00. Room 1
Fate/Stay Night: Heaven's Feel - III. Spring Song. 2020. 2h 0m. 15:00. Room 1
The Night Is Short, Walk on Girl. 2017. 1h 32m. 17:30. Room 1
The Truman Show. 1998. 1h 47m. 19:30. Room 1
Genocidal Organ. 2017. 1hr 55m. 21:45. Room 1

Jacob's Ladder. 1990. 1h 56m. 10:00. Room 2
Parasite. 2019. 2h 12m. 12:15. Room 2
The Dark Knight. 2008. 2h 32min. 14:45. Room 2
Blade Runner 2049. 2017. 2h 44m. 17:45. Room 2
The Mist. 2007. 2h 6m. 21:00. Room 2
Demon Slayer: Mugen Train. 2020. 1h59min. 23:20. Room 2

The Matrix. 1999. 2h 16m. 10:00. Room 3
Inception. 2010. 2h 42m. 11:30. Room 3
Shutter Island. 2010. 2h 19m. 14:30. Room 3
Soul. 2020. 1hr 40m. 17:00. Room 3
Mrs. Brown. 1997. 1h 41min. 19:00. Room 3
Peppa Pig: Festival of Fun. 2019. 1h 8min. 21:00. Room 3
Titanic. 1997. 3h 30min. 22:15. Room 3
```
***

__* - represents empty space for walkways.__ 

__A,B,C,D,E, - represent a section of seating__

Room 1 - 35 seats
```
****************
*CCC*AAAA*BBB*DD
*CCC*AAAA*BBB*DD
*C*C*AAAA*BBB*DD
****************
```
Room 2 - 136 seats
```
***********************
AAA**BBBBB**CCCCCC**EEE
AAA**BBBBB**CCCCCC**EEE
 AAA**BBBB**CCCCC**EEE
 AAA**BBBB**CCCCC**EEE
 AAA**BBBB**CCCCC**EEE
  AAA*************EEE
  AAAA*DDDDDDDDD*EEEE
  AAAA*DDDDDDDDD*EEEE
  AAAA*DDDDDDDDD*EEEE
  *******************
```
Room 3 - 42 seats
```
AAA*BBBB
AAA*BBBB
AAA*BBBB
AAA*BBBB
AAA*BBBB
AAA*BBBB
```

## Set Up Environment
Clone this repository to set up environment to execute program.

```bash
git clone https://github.com/sloth8890/pizzaz-cinema.git
cd pizzaz-cinema
```

## Program Operation

```bash
python3 pizzaz.py --<switch> [<further options>]
```

Where ```<switch>``` is a command used to control the purpose of the program.

There are three switches in this program:

```bash
python3 pizzaz.py --show <timenow>
```
-> Will show all movie information where they begin after time ```<timenow>```.
```bash
python3 pizzaz.py --book
```
-> Will process the order and transaction for one person.
```bash
python3 pizzaz.py --group
```
-> Will process the order and transaction for a group of people.




## Reference
This project is assignment 1 of 2021 INFO1110 and extended by adding some features.  

