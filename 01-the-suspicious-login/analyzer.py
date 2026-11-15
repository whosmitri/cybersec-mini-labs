import re
from collections import Counter

# contadores de autenticação bem-sucedidas e malsucedidas
failed_password_attempts = 0
accepted_login_attempts = 0

# lista de IPs
ips = []

# lista de usuários
users = []

# lê auth.log
with open("auth.log", "r") as log_file:
    lines = log_file.readlines()

# percorre cada linha do arquivo
for line in lines:
    line = line.lower()
    # conta autenticações bem-sucedidas e malsucedidas
    if "failed password" in line:
        failed_password_attempts += 1
    elif "accepted" in line:
        accepted_login_attempts += 1

    # identifica os IPs presentes nos registros
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    ips_matches = re.findall(ip_pattern, line)

    # verifica se encontrou IPs e adiciona à lista
    if ips_matches:
        ips.extend(ips_matches)

    # identifica os usuários envolvidos

    # todo usuário vem depois de "for" ou "user" e antes de "from" (mas alguns não tem palavra após eles)
    # alguns são "invalid user"
    user_pattern = r"(?:user|for)\s+((?:invalid\s+user\s+)?\w+)(?=\s+from|\n)"
    users_matches = re.findall(user_pattern, line)

    # verifica se encontrou usuários e adiciona à lista
    if users_matches:
        users.extend(users_matches)

# conta ocorrência de cada usuário
user_counter = Counter(users)

# resumo no terminal
print("======= RELATÓRIO DE AUTENTICAÇÃO =======")

print(f"\nAutenticações malsucedidas: {failed_password_attempts}")
print(f"\nAutenticações bem-sucedidas: {accepted_login_attempts}")

print(f"\nIPs identificados:")
for ip in set(ips):
    print(ip)

print(f"\nUsuários identificados (e suas ocorrências):")

for user, qty in user_counter.most_common():
    print(f"{user:<20} | {qty}")
