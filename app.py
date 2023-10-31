from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import seaborn as sns


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_form():
    out_of, right_corner, right_wing, top, left_wing, left_corner = process_data()
    shooting_percentages = [right_corner, right_wing, top, left_wing, left_corner]
    shooting_percentages = [(int(item) / int(out_of)) * 100 for item in shooting_percentages]
    chart_filename = create_shooting_chart(shooting_percentages)

    return render_template('result.html', chart_filename=chart_filename)


def process_data():
    out_of = request.form.get('OutOf')
    right_corner = request.form.get('RightCorner')
    right_wing = request.form.get('RightWing')
    top = request.form.get('Top')
    left_wing = request.form.get('LeftWing')
    left_corner = request.form.get('LeftCorner')
    return out_of, right_corner, right_wing, top, left_wing, left_corner


def create_shooting_chart(shooting_percentages):
    # Define positions and percentages
    positions = ['Right Corner', 'Right Wing', 'Top', 'Left Wing', 'Left Corner']

    plt.figure(figsize=(8, 5))
    sns.barplot(x=positions, y=shooting_percentages, palette='viridis')

    plt.title('Shooting Percentages by Position')
    plt.xlabel('Position')
    plt.ylabel('Shooting Percentage')
    plt.ylim(0, 100)
    plt.xticks(rotation=45)

    chart_filename = 'static/shooting_chart.png'
    plt.savefig(chart_filename)
    plt.close()

    return chart_filename


if __name__ == '__main__':
    app.run(debug=True)
