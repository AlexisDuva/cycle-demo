from app import app


def test_hello_returns_200_and_body():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_data(as_text=True) == "Hello World"
