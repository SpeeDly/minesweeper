from unittest import mock

from minesweeper.webui.webui import webUI


HOST = 'http://127.0.0.1'
PORT = '5000'
INIT_ENDPOINT = '{}:{}/create/1'.format(HOST, PORT)
UPDATE_ENDPOINT = '{}:{}/update/1'.format(HOST, PORT)
FINISH_ENDPOINT = '{}:{}/finish/1'.format(HOST, PORT)


@mock.patch('requests.post')
def test_init(mock_request):
    dummy_json = {'dummy_data': 3}
    webUI.init(1, {'dummy_data': 3})
    mock_request.assert_called_with(INIT_ENDPOINT, json=dummy_json)


@mock.patch('requests.post')
def test_update(mock_request):
    dummy_json = {'dummy_data': 3}
    webUI.update(1, {'dummy_data': 3})
    mock_request.assert_called_with(UPDATE_ENDPOINT, json=dummy_json)


@mock.patch('requests.post')
def test_finish(mock_request):
    dummy_json = {'status': 0}
    webUI.finish(1, 0)
    mock_request.assert_called_with(FINISH_ENDPOINT, json=dummy_json)


@mock.patch('minesweeper.webui.webui.WebUI.handle_server_exception')
@mock.patch('requests.post')
def test_exception_handling(mock_request, mock_exception_handler):
    mock_request.side_effect = Exception
    webUI.init(1, 0)
    webUI.update(1, 0)
    webUI.finish(1, 0)
    assert mock_exception_handler.call_count == 3
