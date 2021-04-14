import aoc_help as aoc
import re
import networkx as nx


rules = aoc.get_input('007')
rules = rules.split('\n')


def parse_contents(txt):
    txt = txt.split(" ")
    weight = int(txt[0])
    bag_type = txt[1] + "_" + txt[2]
    return bag_type, weight


def parse(txt):
    bag_type = re.findall("\w+\s\w+(?=\sbags\scontain)", txt)
    bag_type = re.sub(' ', "_", bag_type[0])

    bag_contents = re.findall("\d+\s\w+\s\w+", txt)
    bag_contents = [parse_contents(bag) for bag in bag_contents]
    return bag_type, bag_contents


def write_edges(rule):
    bag_type, bag_contents = parse(rule)
    contents = []
    for bag in bag_contents:
        contents.append([bag_type, bag[0], bag[1]])
    return contents


def write_all_edges(rules):
    contents = []
    for rule in rules:
        contents.extend(write_edges(rule))
    return contents


edges = write_all_edges(rules)
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# part 1

# bags_with_shiny = nx.ancestors(G, "shiny_gold")
# print(len(bags_with_shiny))

# part 2


def find_bags(graph, start, multiplier = 1):
    # print("process::", start, multiplier)
    total = multiplier
    if graph.out_degree(start):
        bags_successors = nx.DiGraph.successors(graph, start)
        bags_to_check = {}
        for bag in bags_successors:
            bags_to_check[bag] = nx.Graph.get_edge_data(G, start, bag)['weight']
        # bags_successors = {bag: nx.Graph.get_edge_data(G, start, bag)['weight'] for bag in bags_successors}
        # print(bags_to_check)
        for bag, weight in bags_to_check.items():
            bags_within = find_bags(graph, bag, weight)
            # print(bags_within)
            total += multiplier * bags_within
            # print('-------------', bag, weight, multiplier, bags_within)
        # print("i tried--", total)
    else:
        # print("i tried----", total)
        return total
    return total


bags_within_shiny = nx.descendants(G, "shiny_gold")
# print(bags_within_shiny)
total = find_bags(G, "shiny_gold")
print(total - 1)