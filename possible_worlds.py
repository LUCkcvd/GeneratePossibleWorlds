import random
import time

def load_edges(file_path):
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            u, v, probability = line.strip().split()
            edges.append((int(u), int(v), float(probability)))
    return edges

def generate_and_save_worlds(edges, num_worlds=1000, seed=42, output_file_path="possible_worlds.txt"):
    random.seed(seed)  # Ensures reproducibility
    start_time = time.time()
    
    with open(output_file_path, 'w') as file:
        for world_index in range(num_worlds):
            world = []
            for u, v, probability in edges:
                if random.random() < probability:
                    world.append((u, v, probability))
            
            # Write the current world directly to the file
            file.write(f"### World {world_index + 1} ###\n")
            for u, v, probability in world:
                file.write(f"{u} {v} {probability}\n")
            file.write("\n")
            
            # Calculate and display estimated time remaining
            elapsed_time = time.time() - start_time
            avg_time_per_world = elapsed_time / (world_index + 1)
            time_remaining = avg_time_per_world * (num_worlds - world_index - 1)
            print(f"World {world_index + 1}/{num_worlds} generated. Estimated time remaining: {time_remaining:.2f} seconds.", end='\r')
    
    print("\nAll worlds generated.")

# Usage example
edges = load_edges("probability_undirect_graph.txt")
generate_and_save_worlds(edges)

