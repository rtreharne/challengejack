import numpy as np
import pandas as pd

x = np.linspace(-3, 3, 100)
y = np.sin(x)

if __name__ == "__main__":
    df = pd.DataFrame({"x": x, "y": y})
    df.to_csv("data.csv", index=False)
