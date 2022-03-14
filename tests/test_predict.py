from cyberbullying.utils import get_trained_model

def test_response():
    model = get_trained_model()
    response = model.predict_phrase('text')

    assert(type(response)==dict)
    assert('prediction' in  response.keys())
    assert('text' in  response.keys())
