import sys
import os
from datetime import datetime

# Конфигурация путей
VERSION_FILE = 'version'  # Файл версии в корне проекта
VERSION_LOG_FILE = '.github/version_log'  # Лог изменений версий
LOGS_FILE = '.github/version_commands.log'  # Лог команд

def get_current_timestamp():
    """Возвращает текущее время в формате 'дд.мм.гггг чч:мм:сс'"""
    return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

def ensure_directory_exists(filepath):
    """Создает директорию, если она не существует"""
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def prepend_to_file(filename, content):
    """Добавляет строку в начало файла"""
    ensure_directory_exists(filename)
    
    existing_content = ''
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            existing_content = f.read()
    
    with open(filename, 'w') as f:
        f.write(f"{content}\n{existing_content}")

def read_current_version():
    """Читает текущую версию из файла"""
    try:
        with open(VERSION_FILE, 'r') as f:
            version = f.read().strip()
            if not version:
                raise ValueError("Version file is empty")
            
            # Проверка формата версии (MAJOR.MINOR.PATCH)
            parts = version.split('.')
            if len(parts) != 3 or not all(p.isdigit() for p in parts):
                raise ValueError("Invalid version format")
            
            return version
    except (FileNotFoundError, ValueError):
        # Инициализация при первом запуске
        default_version = '0.1.0'
        write_version(default_version)
        prepend_to_file(VERSION_LOG_FILE, 
                       f"[{default_version}] - Initial version - {get_current_timestamp()}")
        return default_version

def write_version(version):
    """Записывает новую версию в файл"""
    with open(VERSION_FILE, 'w') as f:
        f.write(version)

def update_version(version_type):
    """Обновляет версию в соответствии с типом изменения"""
    current = read_current_version()
    major, minor, patch = map(int, current.split('.'))
    
    if version_type == 'patch':
        patch += 1
    elif version_type == 'minor':
        minor += 1
        patch = 0
    elif version_type == 'major':
        major += 1
        minor = 0
        patch = 0
    
    new_version = f'{major}.{minor}.{patch}'
    write_version(new_version)
    
    # Логирование изменения
    timestamp = get_current_timestamp()
    log_entry = (f"[{new_version}] <- [{current}] {version_type} update - {timestamp}")
    prepend_to_file(VERSION_LOG_FILE, log_entry)
    
    print(f"Version updated: {current} → {new_version}")
    return new_version

def git_commit_version_update(old_version, new_version, change_type):
    """Создает коммит с обновлением версии"""
    commit_msg = f"[{new_version}] < [{old_version}] {change_type} update"
    os.system(f'git add {VERSION_FILE} {VERSION_LOG_FILE}')
    os.system(f'git commit -m "{commit_msg}"')

def handle_version_update(change_type):
    """Обрабатывает обновление версии с интеграцией в Git"""
    old_version = read_current_version()
    new_version = update_version(change_type)
    git_commit_version_update(old_version, new_version, change_type)
    return new_version

def print_version_history(n=5):
    """Печатает последние изменения версий"""
    try:
        with open(VERSION_LOG_FILE, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
            print("\nVersion history:")
            for line in lines[:n]:
                print(f"  {line}")
    except FileNotFoundError:
        print("Version history is empty")

def main():
    if len(sys.argv) < 2:
        print("Usage: python version_manager.py [command]")
        print("Commands: patch, minor, major, history")
        return

    command = sys.argv[1]
    
    if command in ('patch', 'minor', 'major'):
        new_version = handle_version_update(command)
        
        # Для CI/CD - вывод новой версии в формате для GitHub Actions
        if 'GITHUB_ACTIONS' in os.environ:
            print(f"::set-output name=new_version::{new_version}")
            print(f"::set-output name=old_version::{read_current_version()}")
            
    elif command == 'history':
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        print_version_history(n)
    else:
        print(f"Unknown command: {command}")

if __name__ == '__main__':
    main()
