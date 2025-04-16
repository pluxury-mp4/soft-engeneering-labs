# Вам доступен CSV-файл data.csv, содержащий информацию в csv формате.

def read_csv():
    file_name = "data.csv"
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        data = []
        for line in lines[1:]:
            values = line.strip().split(',')
            data.append(dict(zip(headers, values)))
    return data

result = read_csv()
print(result)