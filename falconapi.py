import falcon
import json
import os
from serialization import load_pipeline

class ModerationResource:
    def on_get(self, req, resp):
        """Handles GET requests"""

        score = clf.predict([req.params['message']])

        if req.accept == "image/png":
            if score[0]:
                image_path = 'assets/troll.png'
            else:
                image_path = 'assets/unicorn.png'
            resp.content_type = 'image/png'
            resp.stream = open(image_path, 'rb')
            resp.stream_len = os.path.getsize(image_path)
        else:
            result = {
                'score': str(score[0])
            }
            
            resp.body = json.dumps(result)

clf = load_pipeline('.', 'toxicity_linear_char_oh_d')
api = falcon.API()
api.add_route('/moderate', ModerationResource())
