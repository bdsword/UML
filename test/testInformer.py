from Informer import Informer


class ATestInformer(Informer):
    def __init__(self):
        super(ATestInformer, self).__init__()

testInformer = ATestInformer()
testInformer.add_event('hello')
print(dir(testInformer))