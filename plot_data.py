import get_data
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt
def plot_sepal_width_vs_length():
    data = get_data.iris()
    print(data.head())
    alt.Chart(data).mark_point().encode(
        x="sepalLength:Q",
        y="sepalWidth:Q"
    ).properties(
        title="Sepal Width vs. Sepal Length"
    ).interactive().save("visualizations/sepal_width_vs_length.html")

def plot_sepal_width_by_species():
    sns.boxenplot(x='species', y='sepalWidth', data=get_data.iris())
    plt.title("Sepal Width By Species")
    plt.xlabel("Species")
    plt.ylabel("Sepal Width")
    plt.savefig("visualizations/sepal_width_by_species.jpg", bbox_inches='tight')


def main():
    sns.set()
    plot_sepal_width_vs_length()
    plot_sepal_width_by_species()

if __name__ == '__main__':
    main()