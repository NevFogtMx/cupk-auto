from factory import create_app
app = create_app()


if __name__ == "__main__":
    app.run(debug=True, port=8877, host='0.0.0.0')