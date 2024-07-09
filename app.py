import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from matplotlib.patches import Ellipse
import seaborn as sns

def initialize_data():
    np.random.seed(42)  # Consistent random seed for reproducibility
    data = np.vstack([
        np.random.multivariate_normal([0, 0], [[1, 0.2], [0.2, 1]], 500),
        np.random.multivariate_normal([3, 4], [[1, -0.3], [-0.3, 1]], 500)
    ])
    return data

def gaussian_ellipse(mean, cov, color):
    v, w = np.linalg.eigh(cov)
    v = 2. * np.sqrt(2.) * np.sqrt(v)
    angle = np.arctan2(w[0][1], w[0][0]) * 180 / np.pi
    return Ellipse(xy=mean, width=v[0], height=v[1], angle=angle, edgecolor=color, lw=2, facecolor=color, alpha=0.3)

def run_em(data, n_iterations=20):
    n, d = data.shape
    n_components = 2
    weights = np.array([0.5, 0.5])
    means = np.array([data[np.random.choice(n)], data[np.random.choice(n)]])
    covariances = np.array([np.eye(d) for _ in range(n_components)])
    all_results = []

    for _ in range(n_iterations):
        # E-step
        responsibilities = np.array([weights[j] * multivariate_normal.pdf(data, mean=means[j], cov=covariances[j])
                                     for j in range(n_components)]).T
        responsibilities /= responsibilities.sum(axis=1, keepdims=True)

        # M-step
        weights = responsibilities.sum(axis=0) / n
        means = np.dot(responsibilities.T, data) / responsibilities.sum(axis=0)[:, None]
        for j in range(n_components):
            diff = data - means[j]
            covariances[j] = np.dot(diff.T, responsibilities[:, j][:, None] * diff) / responsibilities[:, j].sum()

        all_results.append((means.copy(), covariances.copy(), responsibilities.copy()))

    return all_results


def plot_results(data, means, covariances, responsibilities):
    plt.figure(figsize=(10, 8))
    sns.set_style(style="darkgrid")  # Set Seaborn style for a cleaner look

    # Define colors for the clusters
    colors = ['blue', 'red']
    cluster_assignments = np.argmax(responsibilities, axis=1)
    
    # Plot data points with colors based on their cluster assignment
    for idx, color in enumerate(colors):
        cluster_data = data[cluster_assignments == idx]
        sns.scatterplot(x=cluster_data[:, 0], y=cluster_data[:, 1], color=color, alpha=0.5, s=50, label=f'Cluster {idx + 1}')

    # Plot ellipses for each Gaussian component
    for mean, cov, color in zip(means, covariances, colors):
        ell = Ellipse(xy=mean, width=2 * np.sqrt(5.991 * cov[0, 0]), height=2 * np.sqrt(5.991 * cov[1, 1]),
                      angle=np.degrees(np.arctan2(*cov[:2, 0][::-1])), color=color, fill=False, lw=2)
        plt.gca().add_patch(ell)
        plt.scatter(*mean, color=color, s=100, edgecolor='k')  # Center of Gaussian

    plt.xlim(data[:, 0].min() - 1, data[:, 0].max() + 1)
    plt.ylim(data[:, 1].min() - 1, data[:, 1].max() + 1)
    plt.title('EM Algorithm: Gaussian Mixture Model')
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.legend()
    st.pyplot(plt)

# Streamlit App Logic
data = initialize_data()
all_results = run_em(data)

iteration = st.slider('Select Iteration', 0, 19, 0)
means, covariances, responsibilities = all_results[iteration]
plot_results(data, means, covariances, responsibilities)
