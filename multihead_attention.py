# Inspired to make visualization from https://machinelearningmastery.com/a-gentle-introduction-to-positional-encoding-in-transformer-models-part-1/

import numpy as np
import matplotlib.pyplot as plt

def positional_encoding(seq_length, d_model):
    """
    Creates a pattern of numbers that encodes position information.

    Parameters:
    - seq_length: How many items are in your input sequence
    - d_model: The size of your model's working space

    Returns:
    - pos_encoding: A matrix of size (seq_length × d_model) containing the position patterns
    """
    # Step 1: Create an empty matrix to store the position patterns
    pos_encoding = np.zeros((seq_length, d_model))

    # Step 2: Calculate the position numbers and division terms
    position = np.arange(seq_length)[:, np.newaxis]  
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))  # Shape: (d_model // 2,)

    # Step 3: Fill the matrix with sine and cosine patterns
    pos_encoding[:, 0::2] = np.sin(position * div_term)  
    pos_encoding[:, 1::2] = np.cos(position * div_term)  

    return pos_encoding

# Parameters
seq_length = 100  
d_model = 512     

# Generate positional encoding
pos_encoding = positional_encoding(seq_length, d_model)

# Visualization
plt.figure(figsize=(10, 8))
plt.matshow(pos_encoding, fignum=1, cmap='viridis')
plt.colorbar()
plt.title("Positional Encoding Matrix", pad=20)
plt.xlabel("Model Dimension (d_model)")
plt.ylabel("Sequence Position")
plt.show()
