import pandas as pd

def mean():
    a = []
    f = pd.read_csv('training_data.csv', header=None, names=['Open','High','Low','Close'])
    for i,j,m,n in zip(f['High'],f['Low'],f['Open'],f['Close']):
        value = (i-j)/m*100
        a.append(value)

    A = pd.Series(a).mean()

    return A

if __name__ == '__main__':
    mean()