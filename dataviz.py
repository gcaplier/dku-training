def plot_3d(df, x, y, z, country):
    
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xs = df[x]
    ys = df[y]
    zs = df[z]

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_zlabel(z)
    ax.set_title(f"{country} Transactions Only")

    ax.scatter(xs, ys, zs)

    picture = io.BytesIO()
    plt.savefig(picture, format='png')
    
    return picture