from cyberbullying.utils import predict

def test_response():
    response = predict('text to predict')

    assert(type(response)==dict)
    #assert('prediction' in  response.keys())
    #assert('text' in  response.keys())
