import argparse
import math
from collections import namedtuple

def playground_part2(input_path) -> int:
    # X, Y, Z
    circuits = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            circuits.append(line.split(","))

    # Compute the euclidean distance between each point
    distances = []
    for i in range(len(circuits)):
        for j in range(i + 1, len(circuits)):
            c1 = circuits[i]
            c2 = circuits[j]
            dx = int(c1[0]) - int(c2[0])
            dy = int(c1[1]) - int(c2[1])
            dz = int(c1[2]) - int(c2[2])
            euclidean_distance = math.sqrt(dx*dx + dy*dy + dz*dz)
            Distance = namedtuple('Distance', ['circuit_1', 'circuit_2', 'distance'])
            curr_dist = Distance(i, j, euclidean_distance)
            distances.append(curr_dist)
    
    # Sort the distances
    sorted_distances = sorted(distances, key=lambda x: x.distance)

    i, j = 0, 0
    circuit_clusters = []
    while i <= 1000:
        c1 = sorted_distances[j].circuit_1
        c2 = sorted_distances[j].circuit_2

        # Add the first couple of circuits
        if len(circuit_clusters) == 0:
            circuit_clusters.append([c1, c2])
            j += 1
            i += 1
            continue
        
        placed = False
        for cl in circuit_clusters:
            if c1 in cl and c2 not in cl:
                cl.append(c2)
                i += 1
                placed = True
                break
            elif c2 in cl and c1 not in cl:
                cl.append(c1)
                i += 1
                placed = True
                break
            elif c1 in cl and c2 in cl:
                placed = True
                i += 1
                break
        
        if not placed:
            circuit_clusters.append([c1, c2])
            i += 1

        j += 1

    circuit_length = [len(cl) for cl in circuit_clusters]
    sorted_circuit_length = sorted(circuit_length, reverse=True) 

    print(sorted_circuit_length)

    return sorted_circuit_length[0] * sorted_circuit_length[1] * sorted_circuit_length[2]


def playground_part1(input_path) -> int:
    # X, Y, Z
    circuits = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            circuits.append(line.split(","))

    # Compute the euclidean distance between each point
    distances = []
    Distance = namedtuple('Distance', ['circuit_1', 'circuit_2', 'distance'])
    for i in range(len(circuits)):
        for j in range(i + 1, len(circuits)):
            c1 = circuits[i]
            c2 = circuits[j]
            dx = int(c1[0]) - int(c2[0])
            dy = int(c1[1]) - int(c2[1])
            dz = int(c1[2]) - int(c2[2])
            euclidean_distance = math.sqrt(dx*dx + dy*dy + dz*dz)
            curr_dist = Distance(i, j, euclidean_distance)
            distances.append(curr_dist)
    
    # Sort the distances
    sorted_distances = sorted(distances, key=lambda x: x.distance)

    i = 0
    circuit_clusters = []
    while i < 1000:
        c1 = sorted_distances[i].circuit_1
        c2 = sorted_distances[i].circuit_2
        
        already_placed = False
        cl_c1 = -1
        cl_c2 = -1
        for z, cl in enumerate(circuit_clusters):
            if c1 in cl and c2 in cl:
                already_placed = True
                break
            elif c1 in cl and c2 not in cl:
                cl_c1 = z
            elif c2 in cl and c1 not in cl:
                cl_c2 = z
        
        if not already_placed:
            if cl_c1 == -1 and cl_c2 == -1:
                # Add new cluster
                circuit_clusters.append({c1, c2})
            elif cl_c1 != -1 and cl_c2 == -1:
                # Add circuit 2 into cluster with circuit 1
                circuit_clusters[cl_c1].add(c2)
            elif cl_c2 != -1 and cl_c1 == -1:
                # Add circuit 1 into cluster with circuit 2
                circuit_clusters[cl_c2].add(c1)
            elif cl_c1 != -1 and cl_c2 != -1:
                # Merge two clusters
                merged = circuit_clusters[cl_c1] | circuit_clusters[cl_c2]
                for idx in sorted([cl_c1, cl_c2], reverse=True):
                    del circuit_clusters[idx]
                circuit_clusters.append(merged)
        i += 1

    circuit_length = [len(cl) for cl in circuit_clusters]
    sorted_circuit_length = sorted(circuit_length, reverse=True) 

    return sorted_circuit_length[0] * sorted_circuit_length[1] * sorted_circuit_length[2]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to input file")
    args = parser.parse_args()
    input_path = args.input

    # input_path = "/Users/alessandrocaula/Documents/Devs/Git-Repos/ProgrammingAlgoAndChallenges/Advent_of_Code_2025/Day_8/input.txt"
    
    part_1_res = playground_part1(input_path)
    print("Part 1: ", part_1_res)

    # part_2_res = laboratories_part2(input_path)
    # print("Part 2: ", part_2_res)

if __name__ == "__main__":
    main()