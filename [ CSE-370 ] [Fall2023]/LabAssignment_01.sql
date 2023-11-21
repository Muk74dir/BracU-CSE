INSERT INTO developers values
(1, "Taylor Otwell", "otwell@laravel.com", 739360, "2020*6*10", 10),
(2, "Ryan Dahl", "ryan@nodejs.org", 633632, "2020*4*22", 10), 
(3, "Brendan Eich", "eich@javascript.com", 939570, "2020*5*07", 8), 
(5, "Evan You", "you@vuejs.org", 982630, "2020*6*11", 7), 
(6, "Rasmus Lerdorf", "lerdorf@php.net", 937927, "2020*6*3", 8), 
(7, "Guido van Rossum", "guido@python.org", 968827, "2020*7*18", 19), 
(8, "Adrian Holova", "adrian@djangoproject.com", 570724, "2020*5*7", 5), 
(9, "Simon Willison", "simon@djangoproject.com", 864615, "2020*4*30", 4), 
(10, "James Gosling", "james@java.com", 719491, "2020*5*18", 5), 
(11, "Rod Johnson", "rod@spring.io", 601744, "2020*5*18", 7), 
(12, "Satoshi Nakamoto", "nakamoto@blockchain.com", 630488, "2020*5*10", 10);



ALTER TABLE developers
CHANGE influence_count followers int;