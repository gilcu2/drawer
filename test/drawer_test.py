import jsonsocket

class TestDrawer:

    def test_drawer(self):
        print("Run")
        data = {
            'name': 'Patrick Jane',
            'age': 45,
            'children': ['Susie', 'Mike', 'Philip']
        }
        host = 'localhost'
        port = 9999
        client = jsonsocket.Client()
        client.connect(host, port)
        client.send(data)
        response = client.recv()
