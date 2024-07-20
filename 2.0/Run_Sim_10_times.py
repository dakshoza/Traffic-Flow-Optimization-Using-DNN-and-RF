import subprocess
import sys
import re, os

# Assuming your original script is named 'traffic_simulation.py'
original_script = './supervisedAIMain.py'

# Read the content of the original script
with open(original_script, 'r') as file:
    content = file.read()

# Prepare a list to store results
results = []

# Run the simulation 10 times
for i in range(10):
    # signal_timer = 3 + i * 0.5
    
    # Modify the content to update the signal timer
    # modified_content = content.replace(
    #     'if signalTimer >= 3:',
    #     f'if signalTimer >= {signal_timer}:'
    # )
    
    # Modify the content to print the score in a specific format
    modified_content = content.replace(
        'print(f"Score : {score}")',
        'print(f"SIMULATION_SCORE:{score}")'
    )
    
    # Write the modified content to a temporary file
    temp_script = f'temp_traffic_simulation_{i}.py'
    with open(temp_script, 'w') as file:
        file.write(modified_content)
    
    # Run the modified script and capture the output
    print(f"Running simulation {i+1}")
    result = subprocess.run([sys.executable, temp_script], capture_output=True, text=True)
    
    # Extract the score from the output
    score_match = re.search(r'SIMULATION_SCORE:(\d+)', result.stdout)
    score = int(score_match.group(1)) if score_match else None
    
    # Store the results
    results.append((score))
    
    # Clean up the temporary file
    os.remove(temp_script)

print("All simulations completed.")

# Print the results
print("\nResults:")
print("Signal Timer | Score")
print("-" * 20)
for score in results:
    print(f"{score}")

# Optionally, save results to a file
with open('./findings/supervised_10iters.txt', 'w') as f:
    f.write("Score\n")
    for score in results:
        f.write(f"{score}\n")

print("\nResults have been saved ")