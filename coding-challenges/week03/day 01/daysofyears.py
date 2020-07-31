class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = [int(i) for i in date.split('-')]
        day_of_year = (datetime.datetime(y,m,d) - datetime.datetime(y, 1, 1)).days + 1
        return day_of_year