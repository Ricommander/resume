import yaml
import os
from collections import OrderedDict

# Sensitive data (use locally only)
PHONE_NUMBER = "+49-177-333-4444"
EMAIL = "meinemail@postfach.de"

# Custom Dumper to preserve key order
class OrderedDumper(yaml.Dumper):
    def represent_dict(self, data):
        return self.represent_mapping('tag:yaml.org,2002:map', data.items())

OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)

# Function to update the YAML file
def update_yaml_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)

    # Ensure the data is loaded as an OrderedDict
    if isinstance(data, dict):
        data = OrderedDict(data)

    # Replace placeholders with actual values
    if 'cv' in data:
        data['cv']['phone'] = PHONE_NUMBER
        data['cv']['email'] = EMAIL

    # Overwrite the file with the updated data while preserving order
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, Dumper=OrderedDumper, allow_unicode=True, sort_keys=False)

# Main function
def main():
    # Base directory for searching YAML files (project root)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                print(f"Updating file: {file_path}")
                update_yaml_file(file_path)

if __name__ == "__main__":
    main()