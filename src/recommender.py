from sklearn.metrics.pairwise import cosine_similarity

def compute_similarity(matrix):
    """
    Computes cosine similarity between products.
    """
    return cosine_similarity(matrix)


def recommend_products(similarity_matrix, product_index, top_n=5):
    """
    Returns indices of top-N similar products.
    """
    scores = list(enumerate(similarity_matrix[product_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return scores[1:top_n+1]
