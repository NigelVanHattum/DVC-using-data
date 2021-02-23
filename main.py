import dvc.api


def print_url():
    resource_url = dvc.api.get_url(
        'data/Example-data.txt',
        repo='https://github.com/NigelVanHattum/DVC-data')
    print(resource_url)


def print_contents():
    contents = dvc.api.read('data/Example-data.txt',
                            repo='https://github.com/NigelVanHattum/DVC-data')
    print(contents)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_url()
    print_contents()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
