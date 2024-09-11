import matplotlib

matplotlib.use('TkAgg')  # Yoki 'Qt5Agg', 'Agg', va hokazo
import matplotlib.pyplot as plt
import numpy as np


def draw_chessboard():
    chessboard = np.zeros((8, 8))
    chessboard[1::2, ::2] = 1
    chessboard[::2, 1::2] = 1

    plt.figure(figsize=(4, 4))
    plt.imshow(chessboard, cmap='gray', interpolation="nearest")
    plt.xticks([])
    plt.yticks([])
    plt.title("Chessboard", fontsize=20)
    plt.show()


draw_chessboard()
