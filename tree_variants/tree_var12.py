import networkx as nx

tree_var12 = nx.DiGraph()

tree_var12.add_nodes_from([
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
    ("26", {"data": " "}),
    ("27", {"data": 3}),
    ("28", {"data": 2}),
    ("29", {"data": 7}),
    ("30", {"data": 6}),
    ("31", {"data": 8}),
    ("32", {"data": 4}),
    ("33", {"data": 1}),
    ("34", {"data": 6}),
    ("35", {"data": 5}),
    ("36", {"data": 8}),
    ("37", {"data": 7}),
    ("38", {"data": 9}),
    ("39", {"data": 4}),
    ("40", {"data": 3}),
    ("41", {"data": 5}),
    ("42", {"data": 4}),
    ("43", {"data": 6}),
    ("44", {"data": 3}),
    ("45", {"data": 1}),
    ("46", {"data": 4}),
    ("47", {"data": 2}),
    ("48", {"data": 5}),
    ("49", {"data": 1}),
    ("50", {"data": 4}),
    ("51", {"data": 3}),
    ("52", {"data": 1}),
    ("53", {"data": 5}),
    ("54", {"data": 0}),
    ("55", {"data": 2}),
    ("56", {"data": 3}),
    ("57", {"data": 0}),
    ("58", {"data": 4}),
    ("59", {"data": 3}),
    ("60", {"data": 7}),
    ("61", {"data": 6}),
    ("62", {"data": 7}),
])

tree_var12.add_edges_from([
#-------------- LEVEL 1 --------------#
    ("1", "2", {"color": 'grey'}),
    ("1", "3", {"color": 'grey'}),
    ("1", "4", {"color": 'grey'}),
#-------------- LEVEL 2 --------------#
    ("2", "5", {"color": 'grey'}),
    ("2", "6", {"color": 'grey'}),

    ("3", "7", {"color": 'grey'}),
    ("3", "8", {"color": 'grey'}),
    ("3", "9", {"color": 'grey'}),

    ("4", "10", {"color": 'grey'}),
    ("4", "11", {"color": 'grey'}),
#-------------- LEVEL 3 --------------#
    ("5", "12", {"color": 'grey'}),
    ("5", "13", {"color": 'grey'}),
    ("5", "14", {"color": 'grey'}),

    ("6", "15", {"color": 'grey'}),
    ("6", "16", {"color": 'grey'}),
    ("6", "17", {"color": 'grey'}),

    ("7", "18", {"color": 'grey'}),

    ("8", "19", {"color": 'grey'}),
    ("8", "20", {"color": 'grey'}),
    ("8", "21", {"color": 'grey'}),

    ("9", "22", {"color": 'grey'}),
    ("9", "23", {"color": 'grey'}),

    ("10", "24", {"color": 'grey'}),
    ("10", "25", {"color": 'grey'}),

    ("11", "26", {"color": 'grey'}),
#-------------- LEVEL 4 --------------#
    ("12", "27", {"color": 'grey'}),
    ("12", "28", {"color": 'grey'}),

    ("13", "29", {"color": 'grey'}),
    ("13", "30", {"color": 'grey'}),

    ("14", "31", {"color": 'grey'}),
    ("14", "32", {"color": 'grey'}),
    ("14", "33", {"color": 'grey'}),

    ("15", "34", {"color": 'grey'}),
    ("15", "35", {"color": 'grey'}),

    ("16", "36", {"color": 'grey'}),
    ("16", "37", {"color": 'grey'}),
    ("16", "38", {"color": 'grey'}),

    ("17", "39", {"color": 'grey'}),
    ("17", "40", {"color": 'grey'}),

    ("18", "41", {"color": 'grey'}),
    ("18", "42", {"color": 'grey'}),
    ("18", "43", {"color": 'grey'}),

    ("19", "44", {"color": 'grey'}),
    ("19", "45", {"color": 'grey'}),

    ("20", "46", {"color": 'grey'}),
    ("20", "47", {"color": 'grey'}),

    ("21", "48", {"color": 'grey'}),
    ("21", "49", {"color": 'grey'}),
    ("21", "50", {"color": 'grey'}),

    ("22", "51", {"color": 'grey'}),
    ("22", "52", {"color": 'grey'}),

    ("23", "53", {"color": 'grey'}),
    ("23", "54", {"color": 'grey'}),

    ("24", "55", {"color": 'grey'}),
    ("24", "56", {"color": 'grey'}),

    ("25", "57", {"color": 'grey'}),
    ("25", "58", {"color": 'grey'}),
    ("25", "59", {"color": 'grey'}),

    ("26", "60", {"color": 'grey'}),
    ("26", "61", {"color": 'grey'}),
    ("26", "62", {"color": 'grey'}),
])