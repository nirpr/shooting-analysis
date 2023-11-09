from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import seaborn as sns
import position as pos

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process_form():
    pos_lst = process_data()
    shooting_percentage = [position.shooting_percentage() for position in pos_lst]
    chart_filename = create_shooting_chart(shooting_percentage)
    return render_template('result.html', chart_filename=chart_filename)


def process_data():
    out_of = int(request.form.get('OutOf'))
    right_corner_makes = int(request.form.get('RightCorner'))
    right_wing_makes = int(request.form.get('RightWing'))
    top_makes = int(request.form.get('Top'))
    left_wing_makes = int(request.form.get('LeftWing'))
    left_corner_makes = int(request.form.get('LeftCorner'))

    right_corner_type = request.form.get('RightCornerDistance')
    right_wing_type = request.form.get('RightWingDistance')
    top_type = request.form.get('TopDistance')
    left_wing_type = request.form.get('LeftWingDistance')
    left_corner_type = request.form.get('LeftCornerDistance')

    positions = {'right corner': (right_corner_makes, right_corner_type),
                 'right wing': (right_wing_makes, right_wing_type), 'top': (top_makes, top_type),
                 'left wing': (left_wing_makes, left_wing_type), 'left corner': (left_corner_makes, left_corner_type)}

    pos_lst = [pos.Position(makes, out_of - makes, position, miss_type) for position, (makes, miss_type) in
               positions.items()]

    return pos_lst


def create_shooting_chart(shooting_percentages):
    # Define positions and percentages
    positions = ['Right Corner', 'Right Wing', 'Top', 'Left Wing', 'Left Corner']

    plt.figure(figsize=(8, 5))
    sns.barplot(x=positions, y=shooting_percentages, palette='viridis')

    plt.title('Shooting Percentages by Position')
    plt.xlabel('Position')
    plt.ylabel('Shooting Percentage')
    plt.ylim(0, 100)
    plt.xticks()

    chart_filename = 'static/shooting_chart.png'
    plt.savefig(chart_filename)
    plt.close()

    return chart_filename


if __name__ == '__main__':
    app.run(debug=True)
