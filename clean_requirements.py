def clean_requirements_txt():
    cleaned_data = []
    with open("requirements.txt", "r") as file:
        data = file.readlines()  # reads lines and store in a list
        cleaned_data = [requirement[:requirement.find("=")]+">=0" for requirement in data]

    with open("requirements.txt", 'w') as file:
        for data in cleaned_data:
            file.write(data+'\n')  # overwrites the existing content of file

if __name__ == "__main__":
    clean_requirements_txt()