class TraceRetriever:

    def __init__(self, memory):

        self.memory = memory

    def retrieve_similar(self, request):

        return self.memory.search(request["messages"])