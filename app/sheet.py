import gspread
import os
from uuid import UUID
from datetime import datetime
from sheet import CREDS

scopes = ['https://www.googleapis.com/auth/spreadsheets']


class SquadSheet(object):
    def __init__(self):
        gc = gspread.service_account_from_dict(CREDS)
        self.sheet = gc.open('PancakeSquadSales').get_worksheet(0)

    def store_txn(self, id: str, txn_hash: str, price_bnb: str, price_usd: str):
        created_at = datetime.now().isoformat()
        val = [id, txn_hash, price_bnb, price_usd, created_at]
        self.sheet.append_row(val)


if __name__ == "__main__":
    ss = SquadSheet()
