from decouple import config
import facebook

page_token = config('PAGE_ACCESS_TOKEN')
graph = facebook.GraphAPI(access_token=page_token, version="3.1")
print(graph)
page_info = graph.get_object(id=105141914536236)
print(page_info)
