from app import app
import abc
import dash_html_components as html


class Page(abc.ABC):
    def __init__(self) -> None:
        super().__init__()
        self.app = app
        self.init_model()
        self.view = self.init_view()
        self.init_controller()

    @abc.abstractmethod
    def init_model(self) -> None:
        ''' load data here '''
        pass

    @abc.abstractmethod
    def init_view(self) -> html.Div:
        ''' setup dash layout here '''
        return html.Div()

    @abc.abstractmethod
    def init_controller(self) -> None:
        ''' register callbacks here using self.app '''
        pass

    def idx(self, name: str) -> str:
        '''
        make a dash id unique by prepending the page class instance id to it
        '''
        return f'{id(self)}_{name}'
