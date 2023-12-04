def load_data():
    with open('cards') as f:
        data = []
        for line in f.readlines():
            data.append(line.strip())
        return data


if __name__ == '__main__':
    load_data()