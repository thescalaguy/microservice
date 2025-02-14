from second.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(port=9001, host="0.0.0.0")
