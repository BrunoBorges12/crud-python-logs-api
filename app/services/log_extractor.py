import re

def log_extractor():
    log_file = 'logs_servidor/server_logs.txt'
    log_entries = []
  
    try:
        pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}),(\d{3}) - (\w+) - (.+)')
        with open(log_file, 'r') as file:
            for line in file:
                match = pattern.match(line)
                if match:
                    date, number, log_type, message = match.groups()
                    log_data = {
                        'data': date.split(' ')[0],
                        'hora': date.split(' ')[1],
                        'number': number,
                        'nivel': log_type,
                        'texto': message.strip()
                    }
                    log_entries.append(log_data)
            return log_entries
    except FileNotFoundError as e:
        raise FileNotFoundError("O arquivo de log não foi encontrado ou está indisponível.") from e
    except Exception as e:
        raise FileNotFoundError("O arquivo de log está corrompido ou em um formato inválido.") from e
    
print(log_extractor())