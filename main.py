from datetime import datetime
from salary import calculate_salary
from people import get_employees

if __name__ == '__main__':
    print("=== Running 'Accounting' program ===")
    print("Current date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    calculate_salary()
    get_employees()
