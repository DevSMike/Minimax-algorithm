import networkx as nx

tree_var10 = nx.DiGraph()

tree_var10.add_nodes_from([
    ("1", {"data": " "}),
    ("2", {"data": " "}),
    ("3", {"data": " "}),
    ("4", {"data": " "}),
    ("5", {"data": " "}),
    ("6", {"data": " "}),
    ("7", {"data": " "}),
    ("8", {"data": " "}),
    ("9", {"data": " "}),
    ("10", {"data": " "}),
    ("11", {"data": " "}),
    ("12", {"data": " "}),
    ("13", {"data": " "}),
    ("14", {"data": " "}),
    ("15", {"data": " "}),
    ("16", {"data": " "}),
    ("17", {"data": " "}),
    ("18", {"data": " "}),
    ("19", {"data": " "}),
    ("20", {"data": " "}),
    ("21", {"data": " "}),
    ("22", {"data": " "}),
    ("23", {"data": " "}),
    ("24", {"data": " "}),
    ("25", {"data": " "}),
    ("26", {"data": 4}),
    ("27", {"data": 5}),
    ("28", {"data": 6}),
    ("29", {"data": 5}),
    ("30", {"data": 6}),
    ("31", {"data": 3}),
    ("32", {"data": 1}),
    ("33", {"data": 7}),
    ("34", {"data": 8}),
    ("35", {"data": 9}),
    ("36", {"data": 8}),
    ("37", {"data": 8}),
    ("38", {"data": 9}),
    ("39", {"data": 9}),
    ("40", {"data": 9}),
    ("41", {"data": 3}),
    ("42", {"data": 2}),
    ("43", {"data": 8}),
    ("44", {"data": 6}),
    ("45", {"data": 8}),
    ("46", {"data": 7}),
    ("47", {"data": 9}),
    ("48", {"data": 8}),
    ("49", {"data": 9}),
    ("50", {"data": 9}),
    ("51", {"data": 9}),
    ("52", {"data": 5}),
    ("53", {"data": 4}),
    ("54", {"data": 2}),
    ("55", {"data": 3}),
    ("56", {"data": 4}),
    ("57", {"data": 6}),
    ("58", {"data": 8}),
    ("59", {"data": 8}),
    ("60", {"data": 8}),
    ("61", {"data": 9}),
])

tree_var10.add_edges_from([
    # -------------- LEVEL 1 --------------#
    ("1", "2", {"color": 'grey'}),
    ("1", "3", {"color": 'grey'}),
    ("1", "4", {"color": 'grey'}),
    # -------------- LEVEL 2 --------------#
    ("2", "5", {"color": 'grey'}),
    ("2", "6", {"color": 'grey'}),

    ("3", "7", {"color": 'grey'}),
    ("3", "8", {"color": 'grey'}),

    ("4", "9", {"color": 'grey'}),
    ("4", "10", {"color": 'grey'}),
    # -------------- LEVEL 3 --------------#
    ("5", "11", {"color": 'grey'}),
    ("5", "12", {"color": 'grey'}),
    ("5", "13", {"color": 'grey'}),

    ("6", "14", {"color": 'grey'}),
    ("6", "15", {"color": 'grey'}),
    ("6", "16", {"color": 'grey'}),

    ("7", "17", {"color": 'grey'}),
    ("7", "18", {"color": 'grey'}),

    ("8", "19", {"color": 'grey'}),
    ("8", "20", {"color": 'grey'}),
    ("8", "21", {"color": 'grey'}),

    ("9", "22", {"color": 'grey'}),
    ("9", "23", {"color": 'grey'}),

    ("10", "24", {"color": 'grey'}),
    ("10", "25", {"color": 'grey'}),
    # -------------- LEVEL 4 --------------#
    ("11", "26", {"color": 'grey'}),
    ("11", "27", {"color": 'grey'}),

    ("12", "28", {"color": 'grey'}),
    ("12", "29", {"color": 'grey'}),

    ("13", "30", {"color": 'grey'}),
    ("13", "31", {"color": 'grey'}),
    ("13", "32", {"color": 'grey'}),

    ("14", "33", {"color": 'grey'}),
    ("14", "34", {"color": 'grey'}),

    ("15", "35", {"color": 'grey'}),
    ("15", "36", {"color": 'grey'}),
    ("15", "37", {"color": 'grey'}),

    ("16", "38", {"color": 'grey'}),
    ("16", "39", {"color": 'grey'}),
    ("16", "40", {"color": 'grey'}),

    ("17", "41", {"color": 'grey'}),
    ("17", "42", {"color": 'grey'}),

    ("18", "43", {"color": 'grey'}),
    ("18", "44", {"color": 'grey'}),

    ("19", "45", {"color": 'grey'}),
    ("19", "46", {"color": 'grey'}),

    ("20", "47", {"color": 'grey'}),
    ("20", "48", {"color": 'grey'}),
    ("20", "49", {"color": 'grey'}),

    ("21", "50", {"color": 'grey'}),
    ("21", "51", {"color": 'grey'}),

    ("22", "52", {"color": 'grey'}),
    ("22", "53", {"color": 'grey'}),

    ("23", "54", {"color": 'grey'}),
    ("23", "55", {"color": 'grey'}),
    ("23", "56", {"color": 'grey'}),

    ("24", "57", {"color": 'grey'}),
    ("24", "58", {"color": 'grey'}),

    ("25", "59", {"color": 'grey'}),
    ("25", "60", {"color": 'grey'}),
    ("25", "61", {"color": 'grey'}),
])