import altair as alt

def plot_bar_confidence(source):

    plot = alt.Chart(source).mark_bar().encode(
        x="type",
        y="confidence",
        tooltip=['type', 'confidence'],
        color=alt.condition(
            alt.datum.confidence > 0,
            alt.value("red"),  # The positive color
            alt.value("steelblue")  # The negative color
        )
    ).configure_axis(
        labelFontSize=14,
        titleFontSize=14
    ).properties(
        width=800, height=600
    ).interactive()

    return plot