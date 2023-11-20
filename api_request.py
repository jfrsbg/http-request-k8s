import httpx
import polars as pl

class ConsumeAPI():
    def __init__(self):
        self.get_data()
    
    def get_data(self):
        #consume the result from API and write it as CSV for later download
        result = httpx.get('http://localhost:5000/api/product', timeout=30)
        df = pl.DataFrame(result.json())
        df.write_csv('report.csv')
        
        return pl.read_csv('report.csv')

if __name__ == '__main__':
    consume = ConsumeAPI()
    print(consume.get_data())