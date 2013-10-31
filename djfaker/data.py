# -*- coding: utf-8 -*-

LAST_NAMES = ["MARTIN", "SMITH", "THOMAS", "BERNARD", "ROUX", "PETIT", "ROBERT", "MICHEL", "RICHARD", "DURAND", "DUBOIS", "MOREAU", "SIMON", "HENRY", "BROWN", "DAVID", "ROY", "BERTRAND", "LAURENT", "GIRARD", "LAMBERT", "BLANC", "FOURNIER", "JOHNSON", "GARNIER", "ROUSSEAU", "JONES", "GUERIN", "MOREL", "ANDRE", "VINCENT", "GAUTIER", "BONNET", "MERCIER", "MILLER", "MARCHAND", "DAVIS", "CHEVALIER", "DUPONT", "FAURE", "LEROY", "MORIN", "LEFEBVRE", "MASSON", "JOHN", "PERRIN", "WILLIAMS", "GIRAUD", "MATHIEU", "CLEMENT", "NICOLAS", "ROBIN", "BRUN", "FRANCOIS", "GERARD", "WILSON", "CLARK", "BLANCHARD", "BARBIER", "FABRE", "FONTAINE", "ARNAUD", "WHITE", "BOYER", "DENIS", "PIERRE", "AUBERT", "TAYLOR", "ROUSSEL", "NOEL", "ADAMS", "LEGRAND", "BRUNET", "DUVAL", "HALL", "MOORE", "LEFEVRE", "JAMES", "JEAN", "PARIS", "COLIN", "LUCAS", "ROCHE", "GAUTHIER", "BOURGEOIS", "BRETON", "DUMAS", "PICARD", "THOMPSON", "GEORGE", "BOUCHER", "DUMONT", "GAILLARD", "RENARD", "LECLERC", "CHARLES", "DUFOUR", "JOLY", "CAMPBELL", "ALLEN", "SCOTT", "OLIVIER", "RENAUD", "ROGER", "GUILLAUME", "WALKER", "ADAM", "HILL", "BERGER", "PELLETIER", "ROLLAND", "LOUIS", "MISS", "BAILLY", "PHILIPPE", "MARIE", "WRIGHT", "LACROIX", "GRAND", "MULLER", "MARY", "MEUNIER", "LEROUX", "HUBERT", "DESCHAMPS", "DANIEL", "STEWART", "RIVIERE", "ROYER", "MEYER", "BARON", "REY", "PAUL", "YOUNG", "GILBERT", "PREVOST", "GUILLOU", "LEMAIRE", "BRIAND", "KING", "WOOD", "ANDERSON", "CHARPENTIER", "BAKER", "ROBINSON", "CARON", "LANGLOIS", "HUET", "JACOB", "LEE", "GUILLOT", "VIDAL", "BENOIT", "LEMOINE", "AUBRY", "GERMAIN", "CARRE", "LEWIS", "COLLIN", "JULIEN", "PERROT", "DUPUIS", "HAMON", "HERVE", "GREEN", "GOFF", "POIRIER", "GILLET", "FRANCE", "JACKSON", "FLEURY", "COUNTY", "GALL", "MILLET", "GAY", "DUPUY", "JACQUET", "GUYOT", "CLERC", "COLLET", "HAMILTON", "WILLIAM", "BESSON", "MOULIN", "COUSIN", "PARKER", "ANN", "MARCHAL", "PAGE", "ALBERT", "BARTHELEMY", "HARDY", "GROS", "LEBLANC", "BOUVIER", "HARRIS", "RENAULT", "REMY", "BOURBON", "OLLIVIER", "LEGER", "MAY", "REYNAUD", "LINCOLN", "LECOMTE", "GUICHARD", "ROGERS", "MENARD", "ANTOINE", "MARECHAL", "HUMBERT", "COOK", "MALLET", "RUSSELL", "MONNIER", "LEBRUN", "HEBERT", "CHAUVIN", "WM", "GRAY", "BARRE", "MAILLARD", "LONG", "CHURCH", "BERTIN", "MICHAUD", "BELL", "PERRET", "JOURDAN", "GAULTIER", "TURNER", "COSTE", "PICHON", "MARTEL", "ROBERTS", "PONS", "BIGOT", "CORRE", "BOULANGER", "CHEVALLIER", "CARPENTIER", "BLANCHET", "REGNIER", "BUISSON", "PHILLIPS", "EVANS", "RAYMOND", "SEGUIN", "FOSTER", "WATSON", "IMBERT", "LOMBARD", "MORVAN", "VALLEE", "LABBE", "STEVENS", "MORRIS", "HUGO", "ROSE", "ALLARD", "GREGOIRE", "CAMUS", "FAVRE", "PASQUIER", "SCHNEIDER", "JOUBERT", "BOUCHARD", "HOWARD", "LAMY", "JACQUES", "RIOU", "SALMON", "CORDIER", "THIERS", "JOSEPH", "BERNIER", "MARION", "ETIENNE", "EDWARDS", "RICHARDSON", "GUILLON", "WARD", "THIBAULT", "FLOCH", "BENOIST", "TEXIER", "DELAUNAY", "REED", "BOUCHET", "PASCAL", "MORGAN", "MITCHELL", "ELIZABETH", "BESNARD", "ALEXANDER", "GAUDIN", "PORTER", "MASSE", "RICARD", "COURTOIS"]
FIRST_NAMES = ["Gabriel", "Louise", "Arthur", "Raphaël", "Adam", "Louis", "Alexandre", "Chloé", "Camille", "Paul", "Emma", "Sarah", "Maxime", "Victor", "Alice", "Inès", "Eva", "Jeanne", "Lucas", "Antoine", "Nathan", "Léa", "Sacha", "Lina", "Jules", "Thomas", "Juliette", "Anna", "Mohamed", "Manon", "Hugo", "Enzo", "Samuel", "Oscar", "Jade", "Clément", "Mathilde", "Lou", "Adrien", "Gaspard", "Simon", "Martin", "Léo", "Noah", "Anaïs", "Joseph", "Clara", "Yanis", "Charlotte", "Zoé", "Nina", "Clémence", "Romane", "Gabrielle", "Rayan", "Lucie", "Ethan", "Rose", "Marie", "Adèle", "Noé", "Axel", "Baptiste", "Alexis", "Mathis", "Benjamin", "Victoire", "Maxence", "Noémie", "Margaux", "Pierre", "Augustin", "Noa", "Jean", "Amine", "Aaron", "Alix", "Elise", "Julia", "Valentin", "Maya", "Timothée", "Théo", "Lola", "Elisa", "Margot", "Quentin", "Lisa", "Héloïse", "Pauline", "Apolline", "Ava", "Côme", "Valentine", "Laura", "Diane", "Romain", "Charles", "Evan", "Basile", "Salomé", "Tom", "Capucine", "Félix", "Mehdi", "Victoria", "Sasha", "Elsa", "Nour", "Léna", "David", "Iris", "Emilie", "Tristan", "Agathe", "Alicia", "Elias", "Sofia", "Maël", "Aya", "Sara", "Eliott", "Yasmine", "Léon", "Joséphine", "Ambre", "Ulysse", "William", "Ismaël", "Mila", "Ruben", "Julie", "Titouan", "Noam", "Charlie", "Julien", "Luca", "Violette", "Lily", "Liam", "Gabin", "Matthieu", "Fatoumata", "Justine", "Constance", "Nicolas", "Olivia", "Léonard", "Léonie", "Lucien", "Maëlys", "Garance", "Aurélien", "Robin", "Naël", "Mathieu", "Yassine", "Madeleine", "Stella", "Youssef", "Eden", "Octave", "Ibrahim", "Eléonore", "Suzanne", "Hector", "Myriam", "Solal", "Océane", "Anouk", "Ayoub", "Romy", "Isaac", "Nolan", "Faustine", "Diego", "Abel", "Marius", "Sophie", "Marion", "Yacine", "Thibault", "Lenny", "Achille", "Esther", "Mathéo", "Théodore", "Ines", "Blanche", "Lilia", "Edouard", "Ali", "Daniel", "Mariam", "Edgar", "Clémentine", "Alexandra", "Luna", "Mélina", "Guillaume", "Léopold", "Andrea", "Jasmine", "Amaury", "Ilyes", "Daphné", "Mathias", "Elie", "Marc", "Lena", "Joshua", "Rafael", "Mamadou", "Lucile", "Anton", "Antonin", "Nils", "César", "Lila", "Hippolyte", "Anis", "Rayane", "Tess", "Lise", "Max", "Aïcha", "Ahmed", "Samy", "Matteo", "Vadim", "Inaya", "Milo", "Roxane", "Claire", "Corentin", "Aminata", "Mélissa", "Bérénice", "Céleste", "Lilou", "Théophile", "Hadrien", "Amir", "Esteban", "Auguste", "Armand", "Mia", "Eve", "Chiara", "Hamza", "Timothé", "Eloïse", "Milan", "Manel", "Gustave", "Ilian", "Erwan", "Sophia", "Salma", "Lorenzo", "Anatole", "Emile", "Malo", "Amandine", "Hanna", "Maïa", "Marin", "Sirine", "Sofiane", "Elena", "Nassim", "Wassim", "Eugénie", "Kaïs", "Florian", "Joachim", "Andréa", "Ella", "Hawa", "Ana", "Lyna", "Ninon", "Emmanuel", "Dylan", "Lana", "Célia", "Balthazar", "Timéo", "Stanislas", "Selma", "Ryan", "Hanaé", "Kevin", "Assia", "Nino", "Zakaria", "Kylian", "Colombe", "Louna", "Tiago", "Kenza", "Fatima", "Nathanaël", "Cassandre", "Moussa", "Grégoire", "Flora", "Loïc", "Hortense", "Rachel", "Omar", "Arsène", "Aymen", "Naomi", "Raphaëlle", "Isaure", "Naïm", "Thaïs", "Maëlle", "Elisabeth", "Mattéo", "Djibril", "Maïssa", "Raphael", "Melissa", "Paloma", "Hannah", "Farah", "Alex", "Pénélope", "Giulia", "Aurore", "Aliénor", "Zélie", "Henri", "Judith", "Luc", "Sixtine", "Roman", "Pablo", "Julian", "Mina", "Eliot", "Jonathan", "Fanta", "Nora", "Lison", "Malik", "Elliot", "Solène", "Mathys", "Alexia", "Sami", "Naomie", "Owen", "Rebecca", "Vincent", "Eléa", "Anthony", "Louisa", "Damien", "Liv", "Alban", "Younes", "Anaëlle", "Amélie", "Camélia", "Elia", "Maria", "Albane", "Matéo", "Issa", "Adama", "Jessica", "Roméo", "Luka", "Marine", "Hélène", "Ambroise", "Brune", "Jérémy", "Aurèle", "Bilal", "Virgile", "Bianca", "Louane", "Philippine", "Marceau", "Carla", "Maximilien", "Adel", "Abdoulaye", "Dina", "Dorian", "Livia", "Etienne", "Zacharie", "Adem", "Maryam", "Aksel", "Alyssa", "Anas", "Tessa", "Rosalie", "Swann", "Eloi", "Sam", "Imane", "Rafaël", "Ibrahima", "Lili", "Marwa", "François", "Jacques", "Emmy", "Yohan", "Jad", "Fanny", "Bastien", "Lilian", "Enora", "Melvil", "Paola", "Laetitia", "Asma", "Lara", "Rémi", "Noham", "James", "Yaël", "Nael", "Flore", "Amina", "Léandre", "Dounia", "Bintou", "Ewan", "Prune", "Ilan", "Gaël", "Sana", "Awa", "Shana", "Aboubacar", "Ange", "Kelly", "Céline", "Charline", "Olivier", "Louison", "Marianne", "Audrey", "Leïla", "Karim", "Axelle", "Loan", "Idriss", "Johan", "Souleymane", "Morgane", "Georges", "Dimitri", "Yann", "Philippe", "Mohammed", "Candice", "Jérémie", "Ferdinand", "Jonas", "Jana", "Rania", "Marguerite", "Serena", "Emy", "Aloïs", "Angelina", "Merlin", "Ismael", "Kenzo", "Salim", "Laure", "Malak", "Éléonore", "Ernest", "Marco", "Amadou", "Elyas", "Dan", "Oumou", "Aïssatou", "Morgan", "Emmanuelle", "Pia", "Rita", "Christian", "Alessandro", "Cassandra", "Astrid", "Constantin", "Eric", "Ilyana", "Amira", "Elijah", "Mélanie", "Hana", "Maé", "Gaëtan", "Cloé", "Nell", "Jenna", "Mahaut", "Ariane", "Luce", "Neil", "Cindy", "Alya", "Ariel", "Lino", "Mahamadou", "Aymeric", "Scarlett", "Maeva", "Rémy", "Sandro", "Mariama", "Calixte", "Léonore", "Jean-Baptiste", "Yoann", "Tao", "Alexander", "Mateo", "Ilyès", "Lydia", "Norah", "Sébastien", "Lea", "Sonia", "Domitille", "Marwan", "Émilie", "Lassana", "Ilana", "Irène", "Anastasia", "Andy", "Maïlys", "Cécile", "Wael", "Elouan", "Léana", "Gabriela", "Syrine", "Abdallah", "Ashley", "Tania", "Nahel", "Shirel", "Kenny", "Théa", "Nesrine", "Ilyan", "Maylis", "Walid", "Yannick", "Maïmouna", "Elyes", "Loris", "Fatou", "Ethel", "Aylan", "Niels", "Mayeul", "Clovis", "Mona", "Diana", "Mayssa", "Augustine", "Sidonie", "Méline", "Yohann", "Anne", "Ema", "Aurélie", "Estelle", "Ivan", "Elina", "Angèle", "Khadija", "Eya", "Kévin", "Yousra", "Vladimir", "Christophe", "Mellina", "Soren", "Émile", "Clarisse", "Helena", "Milla", "Yoan", "Benoît", "Leo", "André", "Line", "Ludivine", "Ilyas", "Malek", "Talia", "Leonardo", "Mickaël", "Mahé", "Kahina", "Aliya", "Annabelle", "Fatma", "Adrian", "Yannis", "Marcus", "Eline", "Clotilde", "Sadio", "Jordan", "Vianney", "Marcel", "Lily-Rose", "Ousmane", "Assa", "Elissa", "Clarence", "Marilou", "Emir", "Marwane", "Bakary", "Castille", "Warren", "Olympe", "Tara", "Ysée", "Thibaud", "Théophane", "Quitterie", "Stéphane", "Jibril", "Maelys", "Pacôme", "Angelo", "Youcef", "Nine", "Lazare", "Nikita", "Giovanni", "Janna", "Tony", "Angela", "Ismaïl", "Cléo", "Idris", "Moustapha", "Téo", "Camila", "Sabrina", "Chaïma", "Agnès", "Kiara", "Elio", "Arthus", "Nayla", "Vanessa", "Leny", "Léane", "Adriana", "Léopoldine", "Gauthier", "Joyce", "Emna", "Lior", "Liya", "Ziyad", "Ranya", "Michael", "Lucia", "Liza", "Boubacar", "Malick", "Maïssane", "Guilhem", "Mathurin", "Yuna", "Coline", "Oumar", "Filip", "Farès", "Gaston", "Viviane", "Darius", "Tiphaine", "Karl", "Philomène", "Meriem", "Fleur", "Emily", "Nada", "Hajar", "Lia", "Albert", "Shelly", "Soan", "Aïda", "Maia", "Elliott", "Anaé", "Milena", "Issam", "Mael", "Jaden", "Bilel", "El", "Bertille", "Robinson", "Imrane", "Loane", "Abdoul", "Amel", "Nahil", "Malone", "Adil", "Jason", "Inés", "Melina", "Elya", "Fiona", "Youssouf", "Colette", "Elodie", "Lilly", "Marina", "Neïla", "Michelle", "Amélia", "Ania", "Naïla", "Soraya", "Soline", "Lyes", "Isabelle", "Ysé", "Mahdi", "Gabriella", "Demba", "Barnabé", "Liora", "Annaëlle", "Lya", "Cyprien", "Dana", "Amy", "Thelma", "Amalia", "Louka", "Ian", "Eléna", "Jalil", "Angélique", "Joey", "Yara", "Sienna", "Ayman", "Carmen", "Isra", "June", "Keziah", "Halima", "Ombeline", "Kyllian", "Kim", "Amicie", "Manelle", "Xavier", "Ben", "Lamine", "Joana", "Colin", "Anissa", "Riyad", "Hiba", "Rahma", "Nikola", "Goundo", "Ornella", "Irina", "Maïwenn", "Zadig", "Antony", "Ilias", "Izia", "Fatimata", "Thalia", "Denis", "Jayson", "Yani", "Selyan", "Waël", "Matthias", "Nizar", "Shanna", "Fares", "Safa", "Clélia", "Haya", "Josué", "Tasnim", "Ilona", "Youri", "Enguerrand", "Hafsa", "Joanna", "Arielle", "Marko", "Naëlle", "Clothilde", "Lucille", "Safia", "Linda", "Penda", "Noha", "Thibaut", "Iyed", "Kamil", "Marouane", "Rébecca", "Lucy", "Aliyah", "Lancelot", "Tomas", "Catherine", "Chahine", "Curtis", "Siméon", "Pierre-Louis", "Maëly", "Lubin", "Théotime", "Cléophée", "Saul", "Matisse", "Alistair", "Evann", "Fabio", "Aloys", "Justin", "Sérine", "Tiffany", "Mohamed-Amine", "Divine", "Israël", "Florent", "Milhan", "Nadine", "Nelson", "Maud", "Jimmy", "Abigaël", "Delphine", "Noélie", "Adélaïde", "Haroun", "Tali", "Maëva", "Kadiatou", "Cameron", "Matias", "Eglantine", "Allan", "Lilas", "Élise", "Paolo", "Tidiane", "Christelle", "Amin", "Joaquim", "Oriane", "Daphnée", "Steven", "Athénaïs", "Shaï", "Sandra", "Célian", "Joy", "Shaïna", "Marylou", "Christ", "Anya", "Gaspar", "Nicole", "Harry", "Anael", "Luisa", "Jihane", "Cyrine", "Yasmina", "John", "Éric", "Prince", "Samba", "Yona", "Oren", "Nelly", "Cheikh", "Adélie", "Mélia", "Bruno", "Sephora", "Aaliyah", "Arié", "Zachary", "Emeline", "Karamba", "Maÿlis", "Ramata", "Philémon", "Caroline", "Nélia", "Hillel", "Lazar", "Abdou", "Erin", "Aboubakar", "Lamia", "Jane", "Cyrille", "Loup", "Riad", "Younès", "Luke", "Siloé", "Arnaud", "Enola", "Célestine", "Haïm", "Ellie", "Andreas", "Luz", "Perrine", "Paula", "Matilda", "Loïs", "Macéo", "Rosa", "Moïra", "Elyès", "Éloïse", "Avital", "Alassane", "Orlane", "Sekou", "Dany", "Neyla", "Grace", "Moustafa", "Lahna", "Alycia", "Jarod", "Fantine", "Iyad", "Laurent", "Paris", "Nabil", "Liliane", "Perla", "Eyal", "Eloane", "Emilien", "Maëline", "Lou-Anne", "Aurélia", "Nolhan", "Preston", "Christine", "Tim", "Amelia", "Lylia", "Melvin", "Maxine", "Sohan", "Haron", "Rodrigue", "Christopher", "Dahlia", "Kassim", "Meïssa", "Léandro", "Zakarya", "Coralie", "Élie", "Carl", "Isis", "Gwendoline", "Miguel", "Soumaya", "Elyssa", "Baya", "Aimée", "Dune", "Élisa", "Priscille", "Maxim", "Leyna", "Eulalie", "Eli", "Yoav", "Lilie", "Gaétan", "Stan", "Elior", "Rami", "Héléna", "Viktor", "Éva", "Archibald", "Nolann", "Alan", "Mathilda", "Lohan", "Samir", "Cheick", "Yassin", "Lindsay", "Djénéba", "Coumba", "Cassiopée", "Adame", "Safiya", "Léanne", "Hedi", "Mélodie", "Dali", "Cyrielle", "Cynthia", "Ely", "Fatim", "Adeline", "Mélinda", "Idrissa", "Gloria", "Claudia", "Blandine", "Danaé", "Taha", "Melchior", "Maksim", "Solange", "Marvin", "Rokia", "Natalia", "Stefan", "Mattia", "Angel", "Anaelle", "Johanna", "Aristide", "Anselme", "Igor", "Ron", "Mickael", "Ambrine", "Zahra", "Fodé", "Arwen", "Emmie", "Baudouin", "Daria", "Haby", "Chris", "Edgard", "Hamidou", "Clélie", "Thierno", "Luan", "Salimata", "Emilia", "Boubou", "Aly", "Gaïa", "Jayden", "Cédric", "Tiana", "Jérôme", "Ismail", "Saïd", "Aubin", "Malia", "Nawel", "Bouchra", "Mya", "Aziz", "Selena", "Bahia", "Tasnime", "Foucauld", "Aïssata", "Kayna", "Hélie", "Firas", "Nil", "Elora", "Cléa", "Binta", "Kilian", "Hatem", "Alone", "Zoë", "Kenzy", "Brieuc", "Alima", "Kenzi", "Maïly", "Wissam", "Lula", "Fabien", "Lyne", "Killian", "Tancrède", "Lyam", "Wendy", "Ludmila", "Khady", "Anouck", "Elyne", "Damian", "Bonnie", "Sidy", "Yael", "Rym", "Maceo"]
COMPANIES = [u'AITRANSPORT', u'ARTRANSPORT', u'BATRANSPORT', u'BITRANSPORT', u'BOTRANSPORT', u'BUTRANSPORT', u'CETRANSPORT', u'CITRANSPORT', u'CPTRANSPORT', u'DITRANSPORT', u'DOTRANSPORT', u'DUTRANSPORT', u'ESTRANSPORT', u'EUTRANSPORT', u'FATRANSPORT', u'FITRANSPORT', u'FUTRANSPORT', u'TRANSPORTIF', u'TRANSPORTIR', u'TRANSPORTOC', u'TRANSPORTOI', u'TRANSPORTON', u'TRANSPORTOP', u'TRANSPORTRI', u'TRANSPORTUA', u'TRANSPORTUB', u'TRANSPORTUE', u'TRANSPORTUF', u'TRANSPORTUS', u'TUTRANSPORT', u'TRANSPORTUT', u'TRANSPORTUE', u'TRANSPORTEL', u'TRANSPORTES', u'VITRANSPORT', u'VETRANSPORT', u'BOPETRO', u'CAPETRO', u'CEPETRO', u'DEPETRO', u'FTPETRO', u'GAPETRO', u'HEPETRO', u'HOPETRO', u'PETROCT', u'PETRODE', u'PETROFF', u'PETROHM', u'PETROHE', u'PETROIE', u'PETROIS', u'PETROLE', u'PETRONT', u'PETROPE', u'PETRORS', u'PETROSA', u'PETROSE', u'PETROSE', u'PETROUF', u'PETROUI', u'PETROUT', u'PETROUI', u'PETROVE', u'PETROIL', u'PEPETRO', u'POPETRO', u'SEPETRO', u'TOPETRO', u'AGINDUSTRIE', u'AMINDUSTRIE', u'APINDUSTRIE', u'BAINDUSTRIE', u'COINDUSTRIE', u'CRINDUSTRIE', u'INDUSTRIEAU', u'INDUSTRIEGO', u'INDUSTRIENV', u'INDUSTRIERG', u'INDUSTRIEST', u'INDUSTRIETC', u'INDUSTRIEUE', u'INDUSTRIEUH', u'INDUSTRIEUS', u'INDUSTRIEUT', u'INDUSTRIEUX', u'INDUSTRIEUT', u'EPINDUSTRIE', u'FOINDUSTRIE', u'FUINDUSTRIE', u'GAINDUSTRIE', u'GUINDUSTRIE', u'HUINDUSTRIE', u'ICINDUSTRIE', u'KSINDUSTRIE', u'LAINDUSTRIE', u'LEINDUSTRIE', u'LOINDUSTRIE', u'LUINDUSTRIE', u'MAINDUSTRIE', u'MOINDUSTRIE', u'NUINDUSTRIE', u'OUINDUSTRIE', u'PHINDUSTRIE', u'PLINDUSTRIE', u'PSINDUSTRIE', u'QUINDUSTRIE', u'RAINDUSTRIE', u'ROINDUSTRIE', u'SKINDUSTRIE', u'SOINDUSTRIE', u'TOINDUSTRIE', u'TRINDUSTRIE', u'UNINDUSTRIE', u'SOCIETE', u'BOBP', u'CABP', u'JOBP', u'LIBP', u'LOBP', u'NIBP', u'DUOX', u'EGOX', u'FCOX', u'NEOX', u'PROX', u'QUOX', u'ZOOX', u'ANAT', u'ARAT', u'AXAT', u'BOAT', u'BEAT', u'DIAT', u'FIAT', u'FLAT', u'HUAT', u'IRAT', u'LIAT', u'MUAT', u'AUXT', u'BOXT', u'DIXT', u'EUXT', u'FAXT', u'FOXT', u'LUXT', u'MAXT', u'SIXT', u'XTAC', u'XTAN', u'XTAS', u'XTEE', u'XTEK', u'XTEL', u'XTER', u'XTES', u'XTHE', u'BOTECHNO', u'BUTECHNO', u'BATECHNO', u'BUTECHNO', u'CETECHNO', u'CITECHNO', u'CPTECHNO', u'DITECHNO', u'DOTECHNO', u'DUTECHNO', u'DITECHNO', u'DUTECHNO', u'ESTECHNO', u'EUTECHNO', u'FATECHNO', u'FITECHNO', u'FUTECHNO', u'JETECHNO', u'KITECHNO', u'TECHNOIE', u'TECHNOIS', u'TECHNOLX', u'ONTECHNO', u'TECHNONT', u'TECHNOPE', u'AGINFO', u'AMINFO', u'APINFO', u'BAINFO', u'COINFO', u'CRINFO', u'EPINFO', u'FOINFO', u'FUINFO', u'GAINFO', u'GUINFO', u'HUINFO', u'ICINFO', u'KSINFO', u'LAINFO', u'LEINFO', u'LOINFO', u'LUINFO', u'MAINFO', u'MOINFO', u'NUINFO', u'INFOCT', u'INFODE', u'INFOFF', u'INFOHM', u'INFOUF', u'OUINFO', u'INFOUI', u'INFOUT', u'INFOUI', u'INFOVE', u'INFOIL', u'PHINFO', u'PLINFO', u'PSINFO', u'QUINFO', u'RAINFO', u'ROINFO', u'SKINFO', u'SOINFO', u'TOINFO', u'TRINFO', u'UNINFO', u'GAMART', u'GAMAUX', u'GAMAVR', u'GAMAXA', u'GAMAXE', u'GAMAIS', u'ERGAMA', u'FIGAMA', u'GAGAMA', u'REGAMA', u'ZIGAMA', u'ANDELTA', u'DELTAND', u'DELTAPI', u'DELTAPR', u'DELTARA', u'DELTARC', u'DELTARE', u'DELTARS', u'DELTART', u'DELTAUX', u'DELTAVR', u'DELTAXA', u'DELTAXE', u'LADELTA', u'NIDELTA', u'SUDELTA', u'ALPHACE', u'ALPHAGI', u'ALPHAIE', u'ALPHAIL', u'ALPHAIR', u'ALPHAIS', u'ALPHAIT', u'ALPHALE', u'ALPHALU', u'ALPHAMI', u'ANALPHA', u'ALPHANA', u'ALPHAND', u'ALPHAPI', u'ALPHAPR', u'DIALPHA', u'FIALPHA', u'FLALPHA', u'HUALPHA', u'IRALPHA', u'LIALPHA', u'MUALPHA', u'NIALPHA', u'NUALPHA', u'OSALPHA', u'OTALPHA', u'PUALPHA', u'RIALPHA', u'RUALPHA', u'REALPHA', u'SUALPHA', u'TUALPHA', u'USALPHA', u'VIALPHA', u'BETART', u'BETAUX', u'BETAVR', u'BETAXA', u'BETAXE', u'BOBETA', u'CABETA', u'JOBETA', u'LIBETA', u'LOBETA', u'NIBETA', u'PUBETA', u'ROBETA', u'TUBETA']
COMPANIES_EXTRA = ['COOP', 'SA', 'SAS', 'SARL', 'EURL']
MAIL_EXTS = ['free', 'orange', 'gmail', 'aol']
