





class Util:
    @staticmethod
    def print_file_content(file_path):
        with open(file_path, 'r') as file:
            print(file.read())