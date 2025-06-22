from .cleaner import clean_train_columns
from core.loader_base import load_data
from config import FILES

def load_train_data():
    trains = load_data(FILES['trainsData'],sep='|') 
    trains = clean_train_columns(trains)
    return trains
