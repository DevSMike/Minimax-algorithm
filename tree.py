import networkx as nx

from networkx.drawing.nx_agraph import graphviz_layout

G = nx.DiGraph()

G.add_nodes_from([
    ("1", {"data": "-"}),
    ("2", {"data": "-"}),
    ("3", {"data": "-"}),
    ("4", {"data": "-"}),
    ("5", {"data": "-"}),
    ("6", {"data": "-"}),
    ("7", {"data": "-"}),
    ("8", {"data": "-"}),
    ("9", {"data": "-"}),
    ("10", {"data": "-"}),
    ("11", {"data": "-"}),
    ("12", {"data": "-"}),
    ("13", {"data": "-"}),
    ("14", {"data": "-"}),
    ("15", {"data": "-"}),
    ("16", {"data": "-"}),
    ("17", {"data": "-"}),
    ("18", {"data": "-"}),
    ("19", {"data": "-"}),
    ("20", {"data": "-"}),
    ("21", {"data": "-"}),
    ("22", {"data": "-"}),
    ("23", {"data": "-"}),
    ("24", {"data": "-"}),
    ("25", {"data": "-"}),
    ("26", {"data": "-"}),
    ("27", {"data": 3}),
    ("28", {"data": 2}),
    ("29", {"data": 1}),
    ("30", {"data": 0}),
    ("31", {"data": 3}),
    ("32", {"data": 4}),
    ("33", {"data": 3}),
    ("34", {"data": 3}),
    ("35", {"data": 2}),
    ("36", {"data": 5}),
    ("37", {"data": 4}),
    ("38", {"data": 5}),
    ("39", {"data": 6}),
    ("40", {"data": 5}),
    ("41", {"data": 6}),
    ("42", {"data": 5}),
    ("43", {"data": 4}),
    ("44", {"data": 2}),
    ("45", {"data": 1}),
    ("46", {"data": 5}),
    ("47", {"data": 6}),
    ("48", {"data": 1}),
    ("49", {"data": 0}),
    ("50", {"data": 2}),
    ("51", {"data": 7}),
    ("52", {"data": 6}),
    ("53", {"data": 4}),
    ("54", {"data": 3}),
    ("55", {"data": 1}),
    ("56", {"data": 3}),
    ("57", {"data": 2}),
    ("58", {"data": 1}),
    ("59", {"data": 0}),
    ("60", {"data": 2}),
    ("61", {"data": 2}),
    ("62", {"data": 1}),
])

G.add_edges_from([
    ("1", "2"),
    ("1", "3"),
    ("1", "4"),
    ("2", "5"),
    ("2", "6"),
    ("3", "7"),
    ("3", "8"),
    ("3", "9"),
    ("4", "10"),
    ("4", "11"),
    ("5", "12"),
    ("5", "13"),
    ("5", "14"),
    ("6", "15"),
    ("6", "16"),
    ("6", "17"),
    ("7", "18"),
    ("7", "19"),
    ("8", "20"),
    ("8", "21"),
    ("9", "22"),
    ("9", "23"),
    ("10", "24"),
    ("10", "25"),
    ("11", "26"),

    ("12", "27"),
    ("12", "28"),
    ("13", "29"),
    ("13", "30"),
    ("14", "31"),
    ("14", "32"),
    ("14", "33"),
    ("15", "34"),
    ("15", "35"),
    ("16", "36"),
    ("16", "37"),
    ("16", "38"),
    ("17", "39"),
    ("17", "40"),
    ("17", "41"),
    ("18", "42"),
    ("18", "43"),
    ("19", "44"),
    ("19", "45"),
    ("20", "46"),
    ("20", "47"),
    ("21", "48"),
    ("21", "49"),
    ("21", "50"),
    ("22", "51"),
    ("22", "52"),
    ("23", "53"),
    ("23", "54"),
    ("23", "55"),
    ("24", "56"),
    ("24", "57"),
    ("25", "58"),
    ("25", "59"),
    ("26", "60"),
    ("26", "61"),
    ("26", "62"),
])

def draw_tree():
    pos = graphviz_layout(G, prog='dot')
    node_keys = {n: n for n, d in G.nodes(data=True)}
    node_values = {n: (d["data"]) for n, d in G.nodes(data=True)}

    node_color_map = []
    for node in G:
        if G.nodes[node]['data'] == "-":
            node_color_map.append('brown')
        else:
            node_color_map.append('green')

    edge_color_map = []
    for u, v in G.edges:
        if G.nodes[v]['data'] == "-":
            edge_color_map.append('red')
        else:
            edge_color_map.append('grey')

    nx.draw(G, pos, arrows=True, node_size=90, node_color=node_color_map, edge_color=edge_color_map)
    nx.draw_networkx_labels(G, pos, labels=node_values,font_size=10, font_color="white")

    print(pos)
    for i in pos:
        my_list = list(pos[i])
        my_list[1] -= 10
        pos[i] = tuple(my_list)
    print()
    print(pos)
    # print(G.nodes.keys())

    nx.draw_networkx_labels(G, pos, labels=node_keys, font_size=6, font_color="blue")

    # plt.show()

