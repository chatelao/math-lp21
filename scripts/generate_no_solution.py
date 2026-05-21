import re
import glob
import os

def generate_no_solution(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    for line in lines:
        if line.startswith('# '):
            title = line.strip('# \n')
            output_lines.append(f'# {title} (Aufgabenblatt)\n')
        elif line.startswith('| Nr.'):
            output_lines.append('| Nr. | Aufgabe | Lösung |\n')
        elif line.startswith('| :---'):
            output_lines.append('| :--- | :--------------------------- | :------------------------------------------- |\n')
        elif line.startswith('|'):
            # It's a table row
            parts = line.split('|')
            if len(parts) >= 4:
                nr = parts[1].strip()
                aufgabe = parts[2].strip()
                # Create a row with Nr, Aufgabe and empty Lösung
                output_lines.append(f'| {nr} | {aufgabe} | |\n')
        else:
            output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

if __name__ == '__main__':
    # Find all source files matching the pattern
    files = glob.glob('LEKTION*_MIT_LOESUNG.md')
    for input_file in files:
        output_file = input_file.replace('_MIT_LOESUNG.md', '.md')
        print(f"Generating {output_file} from {input_file}...")
        generate_no_solution(input_file, output_file)
