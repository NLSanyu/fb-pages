from decouple import config
import facebook

page_token = config('PAGE_ACCESS_TOKEN')
page_id = config('PAGE_ID')

graph = facebook.GraphAPI(access_token=page_token, version="3.1")
print(graph)
page_info = graph.get_object(id=page_id, fields='about, website')
print(page_info)
posts = graph.get_object(id=page_id,
                        fields='posts.limit(100)')
print(posts)