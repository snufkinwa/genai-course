# Nice addtional read https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention

import numpy as np
import matplotlib.pyplot as plt


def compute_attention_scores(query, key, value, mask=None):
    """
    Compute scaled dot-product attention scores.


    Parameters:
    - query: Tensor of shape (batch_size, num_heads, seq_length, d_k)
    - key: Tensor of shape (batch_size, num_heads, seq_length, d_k)
    - value: Tensor of shape (batch_size, num_heads, seq_length, d_v)
    - mask: Optional mask tensor


    Returns:
    - attention_output: Weighted sum of values
    - attention_weights: Attention probability distribution
    """
    # TODO: Compute dot product of query and key
    scores = np.matmul(query, key.transpose(0, 1, 3, 2))

    # TODO: Scale the scores
    d_k = query.shape[-1]
    scaled_scores = scores / np.sqrt(d_k)


    # TODO: Apply mask if provided
    if mask is not None:
        #Large negative number to default to 0
       scaled_scores += mask * -1e9


    # TODO: Apply softmax to get attention weights
    exp_scores = np.exp(scaled_scores - np.max(scaled_scores, axis=-1, keepdims=True))  
    attention_weights = exp_scores / np.sum(exp_scores, axis=-1, keepdims=True)   


    # TODO: Compute weighted sum of values
    attention_output = np.matmul(attention_weights, value)


    return attention_output, attention_weights


def visualize_attention_with_words(attention_weights, words, title="Attention Weights Heatmap"):
    """
    Visualize attention weights using a heatmap with words as labels.

    Parameters:
    - attention_weights: Attention probability distribution (batch_size, num_heads, seq_length, seq_length)
    - words: List of words corresponding to the sequence.
    - title: Title for the heatmap.
    """
    # Squeeze to remove batch and head dimensions (assume batch_size=1, num_heads=1)
    attention_weights = np.squeeze(attention_weights)

    plt.figure(figsize=(8, 6))
    plt.matshow(attention_weights, fignum=1, cmap="viridis")
    plt.colorbar()
    plt.title(title, pad=20)
    plt.xlabel("Keys (Words)")
    plt.ylabel("Queries (Words)")
    plt.xticks(ticks=np.arange(len(words)), labels=words, rotation=90)
    plt.yticks(ticks=np.arange(len(words)), labels=words)
    plt.show()

def test_attention_with_words():
    # Define test inputs
    words = ["The", "cat", "chased", "the", "mouse"]
    seq_length = len(words)
    d_k = 4
    d_v = 4

    # Create random embeddings for query, key, value
    np.random.seed(0)
    query = np.random.rand(1, 1, seq_length, d_k) 
    key = np.random.rand(1, 1, seq_length, d_k)
    value = np.random.rand(1, 1, seq_length, d_v)

    # Mask 
    mask = None

    # Compute attention
    attention_output, attention_weights = compute_attention_scores(query, key, value, mask)

    # Print results
    print("Attention Weights:\n", attention_weights)

    # Visualize attention weights with words
    visualize_attention_with_words(attention_weights, words, title="Attention Weights for Sentence")

# Run the test
test_attention_with_words()