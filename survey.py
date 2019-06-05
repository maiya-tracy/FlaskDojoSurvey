from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
    print(request.form)
    name_from_form = request.form['your_name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comment_from_form = request.form['comment']
    snack_from_form = request.form.getlist('snack')
    os_from_form = request.form['radios']
    return render_template("show.html", name_on_template=name_from_form,
    location_on_template=location_from_form, language_on_template = language_from_form,
    comment_on_template = comment_from_form, snack_on_template = snack_from_form,
    os_on_template = os_from_form)

if __name__ == "__main__":
    app.run(debug=True)
