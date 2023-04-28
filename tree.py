import networkx as nx

from networkx.drawing.nx_agraph import graphviz_layout

G = nx.DiGraph()

G.add_nodes_from([
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
    ("1", "2", {"color": 'grey'}),
    ("1", "3", {"color": 'grey'}),
    ("1", "4", {"color": 'grey'}),
    ("2", "5", {"color": 'grey'}),
    ("2", "6", {"color": 'grey'}),
    ("3", "7", {"color": 'grey'}),
    ("3", "8", {"color": 'grey'}),
    ("3", "9", {"color": 'grey'}),
    ("4", "10", {"color": 'grey'}),
    ("4", "11", {"color": 'grey'}),
    ("5", "12", {"color": 'grey'}),
    ("5", "13", {"color": 'grey'}),
    ("5", "14", {"color": 'grey'}),
    ("6", "15", {"color": 'grey'}),
    ("6", "16", {"color": 'grey'}),
    ("6", "17", {"color": 'grey'}),
    ("7", "18", {"color": 'grey'}),
    ("7", "19", {"color": 'grey'}),
    ("8", "20", {"color": 'grey'}),
    ("8", "21", {"color": 'grey'}),
    ("9", "22", {"color": 'grey'}),
    ("9", "23", {"color": 'grey'}),
    ("10", "24", {"color": 'grey'}),
    ("10", "25", {"color": 'grey'}),
    ("11", "26", {"color": 'grey'}),
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
    ("17", "41", {"color": 'grey'}),
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
    ("23", "55", {"color": 'grey'}),
    ("24", "56", {"color": 'grey'}),
    ("24", "57", {"color": 'grey'}),
    ("25", "58", {"color": 'grey'}),
    ("25", "59", {"color": 'grey'}),
    ("26", "60", {"color": 'grey'}),
    ("26", "61", {"color": 'grey'}),
    ("26", "62", {"color": 'grey'}),
])


def color_map_update():
    for u, v in G.edges:
        G.edges[u, v]['color'] = 'grey'


def draw_tree():
    pos = graphviz_layout(G, prog='dot')
    node_keys = {n: n for n, d in G.nodes(data=True)}
    node_values = {n: (d["data"]) for n, d in G.nodes(data=True)}
    edge_color_map = {(u, v): (d["color"]) for u, v, d in G.edges(data=True)}

    nx.draw(G, pos, arrows=True, node_size=90, node_color="green", edge_color=edge_color_map.values())
    nx.draw_networkx_labels(G, pos, labels=node_values,font_size=10, font_color="white")

    for i in pos:
        my_list = list(pos[i])
        my_list[1] -= 10
        pos[i] = tuple(my_list)

    nx.draw_networkx_labels(G, pos, labels=node_keys, font_size=6, font_color="blue")

    # plt.show()