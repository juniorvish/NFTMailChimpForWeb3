```python
import csv
from typing import List

class WalletHandler:
    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def collect_addresses(self) -> List[str]:
        with open(self.csv_file, mode='r') as file:
            reader = csv.reader(file)
            return [row[0] for row in reader]

    def create_list(self, addresses: List[str]) -> None:
        with open(self.csv_file, mode='w') as file:
            writer = csv.writer(file)
            for address in addresses:
                writer.writerow([address])
```